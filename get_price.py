import sys

from requests import Request, Session
import json

session = Session()
coin = "BTC"
if len(sys.argv) > 1:
    coin = str.upper(sys.argv[1])
url = "https://www.ouyicn.work/api/v5/market/books?instId="+coin+"-USDT"
response = session.get(url)
data_list = json.loads(response.text)
if data_list["code"] == '51001':
    print("币种不存在")
    exit(-1)
elif data_list["code"] == '0':
    real_price = data_list["data"][0]["asks"][0][0]
    print(coin, ":", real_price)
else:
    print("未知原因")
    print("response:", data_list)
