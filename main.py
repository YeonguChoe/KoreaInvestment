from time import sleep
from OAuth.OAuth import *
from RealTime.DomesticReal import *
from DomesticStockInfo.Domestic import *
from DomesticStockOrder.Order import *
import asyncio


async def main():
    t = read_access_token()
    k = read_approval_key()

    get_price(t,"035420")

    # await market_depth(t, k, "005930")
    # get_price(t, "035420")


if __name__ == "__main__":
    asyncio.run(main())
