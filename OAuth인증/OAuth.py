import requests
import json

# 개인정보
from credential import *

# OAuth 인증


def get_approval_key():
    body = {
        "grant_type": "client_credentials",
        "appkey": APP_Key,
        "secretkey": APP_Secret,
    }
    URL = url + "/oauth2/Approval"
    res = requests.post(URL, data=json.dumps(body)).json()["approval_key"]
    return res


def get_HASH(body):
    header = {
        "content-type": "application/json",
        "appkey": APP_Key,
        "appsecret": APP_Secret,
    }
    URL = url + "/uapi/hashkey"
    res = requests.post(URL, headers=header, data=json.dumps(body)).json()["HASH"]

    return res


def get_access_token():

    body = {
        "grant_type": "client_credentials",
        "appkey": APP_Key,
        "appsecret": APP_Secret,
    }

    URL = url + "/oauth2/tokenP"
    res = requests.post(URL, data=json.dumps(body)).json()

    return res


def revoke_access_token(token):
    body = {"appkey": APP_Key, "appsecret": APP_Secret, "token": token["access_token"]}
    URL = url + "/oauth2/revokeP"
    res = requests.post(URL, data=json.dumps(body)).json()
    return res


# 추가 함수
def save_access_token(access_token):
    string_access_token = json.dumps(access_token)
    with open("./OAuth인증/access_token.json", "w") as json_file:
        json_file.write(string_access_token)


def read_access_token():
    with open("OAuth인증/access_token.json", "r") as file:
        access_token_dictionary = json.load(file)
    return access_token_dictionary["access_token"]
