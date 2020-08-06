import axios from "axios";
// http://192.168.0.3:8000
export const BASEURL = "167.172.138.187:8000/"
// export const BASEURL = "192.168.0.102:8000/"
// export const BASEURL = "192.168.0.102:8000/"

// "http://192.168.0.9:8000/user/reset_password"

export const LOGIN_URL ="http://".concat(BASEURL.concat("api/v1/login"));
export const CHATSHOW_LIST_URL = "http://".concat(BASEURL.concat("chat/chatcategory/"))
export const QUESTIONS_URL = "http://".concat(BASEURL.concat("chat/questions/"))
export const REGISTER_URL = "http://".concat(BASEURL.concat("user/register"))
export const CHATSHOW_URL = "http://".concat(BASEURL.concat("chat/chatshow/"))
export const USER_LIST_URL = "http://".concat(BASEURL.concat("user/user_list"))
export const ADD_HOST_URL = "http://".concat(BASEURL.concat("chat/addhost"))
export const REMOVE_HOST_URL = "http://".concat(BASEURL.concat("chat/removehost"))

export const CHAT_MESSAGES_URL = "http://".concat(BASEURL.concat("chat/message/"))
export const FORGOT_PASSWORD = "http://".concat(BASEURL.concat("user/forgot-password"))
export const COMMENT_ROOM = "http://".concat(BASEURL.concat("chat/commentRoom/"))
export const SUBSCRIBE_URL = "http://".concat(BASEURL.concat("chat/subscribe"))

export const UPDATE_DEVICE_ID = "http://".concat(BASEURL.concat("user/update-device-token"))

// export const REGISTER_URL = "http://127.0.0.1:8000/user/register";
// export const REQUEST_PASSWORD_URL = "api/auth/forgot-password";

// export const ME_URL = "http://127.0.0.1:8000/user/get_user";
// export const VALIDATION_URL = "http://127.0.0.1:8000/user/load_data";
// export const PREDICTIVE_URL = "http://127.0.0.1:8000/user/load_modeling_code";
// export const USER_THREAD_URL = "http://127.0.0.1:8000/api/chat/get_user_thread";
// export const TAGS_URL = "http://127.0.0.1:8000/user/get_tags";
// export const GET_DOCTORS = "http://127.0.0.1:8000/user/get_doctors"
// export const CREATE_THREAD = "http://127.0.0.1:8000/api/chat/thread"


export function updateDeviceToken(data) {
  console.log(data, 'update device id')
  return axios.post(UPDATE_DEVICE_ID, data, { headers: { Authorization: 'Bearer '.concat(data.userToken) } } );
}

export function login(username, password) {
  console.log(username, password, LOGIN_URL ,'I am here')
  return axios.post(LOGIN_URL, {username: username, password:password});
}


export function addSubscriber(data, access) {
  console.log(data, access,'inside add host')
  return axios.post(SUBSCRIBE_URL,data, { headers: { Authorization: 'Bearer '.concat(access) } } );
}


export function createPrvateChatRoom(data, access){
  console.log(data, COMMENT_ROOM ,'I am create room')
  return axios.post(COMMENT_ROOM, data, { headers: { Authorization: 'Bearer '.concat(access) } } );
}

export function forgotPassword(data) {
  console.log(data, FORGOT_PASSWORD ,'I am here forgot password')
  return axios.post(FORGOT_PASSWORD, data);
}

export function addHost(data, access) {
  console.log(data, access,'inside add host')
  return axios.post(ADD_HOST_URL,data, { headers: { Authorization: 'Bearer '.concat(access) } } );
}

export function removeHost(data, access) {
  console.log(data, access,'inside add host')
  return axios.post(REMOVE_HOST_URL,data, { headers: { Authorization: 'Bearer '.concat(access) } } );
}

export function getUserList(access){
  console.log(USER_LIST_URL)
  return axios.get(USER_LIST_URL,{ headers: { Authorization: 'Bearer '.concat(access) } } )
}
export function signup(data) {
  // console.log(username, password, LOGIN_URL ,'I am here')
  console.log(data);
  return axios.post(REGISTER_URL, data);
}

export function createChat(data, access) {
  // console.log(username, password, LOGIN_URL ,'I am here')
  console.log(data, 'creat data');
  return axios.post(CHATSHOW_URL, data ,{ headers: { Authorization: 'Bearer '.concat(access)}});
}

export function getChatShowCategory(access){
  console.log(access, 'inside curd');
  return axios.get(CHATSHOW_LIST_URL, { headers: { Authorization: 'Bearer '.concat(access) } });
  // return axios.get(CHATSHOW_LIST_URL);

}
export function getChatShow(category_id, access){
  console.log(access, 'inside curd getshow');
  return axios.get(CHATSHOW_URL + category_id + "/", { headers: { Authorization: 'Bearer '.concat(access) } });
  // return axios.get(CHATSHOW_LIST_URL);

}
export function getChatShowMessages(chat_show_id, access){
  console.log(access, 'inside curd getshow');
  return axios.get(CHAT_MESSAGES_URL + chat_show_id + "/", { headers: { Authorization: 'Bearer '.concat(access) } });
  // return axios.get(CHATSHOW_LIST_URL);

}

export function getQuestions(threadId, access){
  console.log(QUESTIONS_URL)
  return axios.get(QUESTIONS_URL + threadId + "/", { headers: { Authorization: 'Bearer '.concat(access) } });
}
export function createQuestions(data, access){
  console.log(QUESTIONS_URL, data, access)
  return axios.post(QUESTIONS_URL ,data,{ headers: { Authorization: 'Bearer '.concat(access) } } );
}

