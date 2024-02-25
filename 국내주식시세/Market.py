import json
import requests

# 개인정보
from credential import *

# inqure_price


def get_current_price(access_token, ticker):
    header = {
        "content-type": "application/json",
        "authorization": f"Bearer {access_token}",
        "appkey": APP_Key,
        "appsecret": APP_Secret,
        "tr_id": "FHKST01010100",
    }
    URL = url + "/uapi/domestic-stock/v1/quotations/inquire-price"
    query_parameter = {"fid_cond_mrkt_div_code": "J", "fid_input_iscd": ticker}
    res = requests.get(url=URL, headers=header, params=query_parameter).json()
    return res

# inquire_member
# search_info
# inquire_time_indexchartprice
