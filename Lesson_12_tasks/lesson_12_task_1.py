'''Tapşırıq 1: Səhər yeməyi
make_tea() - 2 saniyə
make_coffee() - 3 saniyə
make_sandwich() - 4 saniyə
Hər biri async funksiya olsun
asyncio.gather ilə birlikdə işlədin
Ümumi vaxtı ölçün
'''

import asyncio
import time

async def make_tea():
    print('Making tea is in progress...')
    await asyncio.sleep(2)
    print('Making tea is finished.')
    return 'Tea'
async def make_coffee():
    print('Making coffee is in progress...')
    await asyncio.sleep(3)
    print('Making coffee is finished.')
    return 'Coffee'

async def make_sandwich():
    print('Making sandwich is in progress...')
    await asyncio.sleep(4)
    print('Making sandwich is finished.')
    return 'Sandwich'

async def main():
    start_time=time.time()

    print('Making breakfast is started\n')
    tasks=[make_tea(), make_coffee(), make_sandwich()]
    results= await asyncio.gather(*tasks)

    end_time=time.time()
    print(f"\nMenu: {results}")
    print(f"Total time: {end_time - start_time:.2f} san")


if __name__ == "__main__":
    asyncio.run(main())