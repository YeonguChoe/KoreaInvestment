from time import sleep
from OAuth인증.OAuth import *
from 실시간시세.DomesticReal import *
from 국내주식시세.Domestic import *
from 국내주식주문.Order import *
import asyncio


async def main():
    t = read_access_token()
    k = read_approval_key()

    # sell(t, "031860", 316, 1)
    # sell(t, "245620", 691, 2)
    # sell(t, "177350", 785, 1)
    # get_remaining_stock(t)
    list_sell_order(t)
    # cancel_order(t,"0000134331")
    # print(await get_realtime_price(k,"031860"))
    # print(await get_realtime_price(k,"245620"))
    # print(await get_realtime_price(k,"177350"))
    # await report_order_status(k,"005930")
    # list_buy_order(t)
    # cancel_order(t,"0000140020")
    await get_remaining_stock(t,k)



if __name__ == "__main__":
    asyncio.run(main())
