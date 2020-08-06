from .models.accounts import User
from .models.accounts import Profile
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .serializer import ProfileSerializer
from .serializer import UserSerializer, TagSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from taggit.models import Tag
import smtplib, ssl
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.shortcuts import get_object_or_404


class ProfileViewSet(ModelViewSet):

    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=True, methods=['get'])
    def highlight(self, request, *args, **kwargs):
        username = request.user
        user = User.objects.get(username=username)
        #  
        print(user)
        try:
            userprofile = Profile.objects.get(user = user)
            content = ProfileSerializer(userprofile).data
            print(content)
        except:
            content = {}
        return  Response(content, status.HTTP_201_CREATED)

    def get_doctors(self, request , *args, **kwargs):
        tags = json.loads(request.query_params.get("tags"))
        queryset_userprofile = Profile.objects.filter(tags__slug__in = tags).distinct()
        try:
            content = ProfileSerializer(queryset_userprofile, many=True).data
            print(content)
        except:
            content = {}
        return  Response(content, status.HTTP_201_CREATED)    
        
class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)  
    queryset = User.objects.all()

    
    @action(detail=True, methods=['post'])
    def update_device_token(self, request, *args, **kwargs):
        device_token = request.data.get('deviceToken', None)
        user_token = request.data.get('userToken', None)
        print(device_token)
        user = request.user
        user.device_token = device_token
        user.save()
        # if uuid:
        #     user = User.objects.get(id = self.data['uuid'])
        #     password = self.data.get('txtPassword', None)
        #     if password:
        #         user.set_password(password)
        #         user.save()
        return Response(json.dumps({"message":"user Token updated successfully"}), status.HTTP_201_CREATED) 


class TagsViewSet(ModelViewSet):
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        queryset = Tag.objects.all()
        serializer = TagSerializer(queryset, many=True)
        return  Response(serializer.data, status.HTTP_201_CREATED)

@permission_classes([AllowAny ,])
@api_view(["POST"])
def forgot_password(self):
    email = self.data['email'] 
    # user = get_object_or_404(User, email=email)
    user = User.objects.filter(email=email)
    if user:
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        receiver_email = email  # Enter your address
        sender_email = "vishesh.verma2412@gmail.com"  # Enter receiver address
        password = 'Jaishriram12!'
        
        message = MIMEMultipart("alternative")
        message["Subject"] = "Chatcast Password reset link"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Reset Link"""
        html = """\
        <html>
        <body>
            <p>Hi,<br>
            Here is the password reset link<br>
            <a href="{}{}">Reset Link </a>
        <body>    
        </html>
        """.format("http://167.172.138.187/forgotpassword/?uuid=", str(user[0].id))

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        message.attach(part2)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        return Response(json.dumps({"message":"email send"}), status.HTTP_201_CREATED) 
    return Response(json.dumps({"error":"email not found"})) 
        
           

   


@permission_classes([AllowAny ,])
@api_view(["POST"])
def reset_password(self):
    uuid = self.data.get('uuid', None)
    if uuid:
        user = User.objects.get(id = self.data['uuid'])
        password = self.data.get('txtPassword', None)
        if password:
            user.set_password(password)
            user.save()
    return Response(json.dumps({"message":"password Changes successfully"}), status.HTTP_201_CREATED)    



@permission_classes([AllowAny ,])
@api_view(["POST"])
def create_user_profile(self):
        authentication_classes = [AllowAny,]
        print(self.data["username"])
        user_data = self.data
        password = user_data["password"]
        email = user_data["email"]
        username = user_data['username']
        first_name = user_data["first_name"]
        last_name = user_data["last_name"]
        user_serializer = UserSerializer(data={
            'password':password,
            'username': username,
            'email': email,
            })
        if user_serializer.is_valid():
            user_instance = user_serializer.save()
            #  
            # tokenr = TokenObtainPairSerializer().get_token(user_instance)  
            # tokena = AccessToken().for_user(user_instance)
            # print("user instance", type(user_instance))
            user_profile_serializer = ProfileSerializer(data={
                'first_name': first_name,
                'last_name': last_name,
                'user': user_instance.id
            })
            if user_profile_serializer.is_valid():
                user_profile_instance  = user_profile_serializer.save()
                print(user_profile_serializer.data)
                token = AccessToken().for_user(user_instance)
                # AccessToken().for_user(user_instance)
                response_data = {
                    "access": token['jti']
                }
                print(json.dumps(response_data))
                return Response(response_data, status.HTTP_201_CREATED)
            else:
                print("because of profile", user_profile_serializer.errors)
                return Response(user_profile_serializer.errors, status.HTTP_400_BAD_REQUEST)
        else:
            print(user_serializer.errors)
            return Response(user_serializer.errors, status.HTTP_400_BAD_REQUEST)