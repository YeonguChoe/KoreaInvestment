from time import sleep
from OAuth인증.OAuth import *
from 실시간시세.DomesticReal import *
from 국내주식시세.Domestic import *
from 국내주식주문.Order import *
import asyncio


async def main():
    t = read_access_token()
    print(get_current_price1(t,"001210"))
    # sell(t, "001210", "938", "1")
    # cancel_order(t, "0000111426")
    # print(list_sell_order(t))
    # print(get_remaining_cash(t))
    # print(get_remaining_stock(t))

if __name__ == "__main__":
    asyncio.run(main())
