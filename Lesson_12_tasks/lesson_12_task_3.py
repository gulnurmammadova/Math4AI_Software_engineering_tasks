'''Tapşırıq 3: create_task
send_email() - 3 saniyə
save_log() - 1 saniyə
Hər ikisini create_task ilə başladın
Sonra await ilə nəticələri gözləyin
Hansı daha tez bitir, müşahidə edin'''

import asyncio
import time

async def send_email():
    print('Sending email...')
    await asyncio.sleep(3)
    print('Email is sent!')

async def save_log():
    print('Saving log...')
    await asyncio.sleep(1)
    print('Log is saved!')

async def main():
    start_time= time.time()
    task1= asyncio.create_task(send_email())
    task2=asyncio.create_task(save_log())

    await task1
    await task2
    end_time=time.time()

    print(f'Total duration: {end_time-start_time:.2f}')
if __name__ == '__main__':
   asyncio.run(main())

