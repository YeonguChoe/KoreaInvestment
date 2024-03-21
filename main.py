from time import sleep
from OAuth.OAuth import *
from RealTime.DomesticReal import *
from DomesticStockInfo.Domestic import *
from DomesticStockOrder.Order import *
import asyncio


async def main():
####################################################################################################
# Token information (Leave it like this)
    # get_access_token()
    # get_approval_key()
    t = read_access_token()
    k = read_approval_key()
####################################################################################################
# write your trading script starting here!!!
    

if __name__ == "__main__":
    asyncio.run(main())
