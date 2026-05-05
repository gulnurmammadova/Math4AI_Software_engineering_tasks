'''Tapşırıq 2: Download
download_file(name) async funksiya
yazın
time.sleep yox, asyncio.sleep istifadə
edin
3 faylı eyni vaxtda yüklədin
Nəticələri siyahı kimi çap edin
Ardıcıl və gather variantını müqayisə
edin'''

import asyncio
import time


async def download_file(name):
    print(f'Downloading file {name}...')
    await asyncio.sleep(2)
    print(f'{name} Downloaded!')
    return name
    
async def main():
    names=['photo.png', 'video.mp4', 'text.txt', 'table.exe', 'presentation.pptx']
    print('>>>>>>>>Sequental downloading is in progress...<<<<<<<<<<<<<')
    start_seq = time.time()
    seq_results = []
    for name in names:
        res = await download_file(name)
        seq_results.append(res)
    end_seq = time.time()
    print(f"Sequental duration: {end_seq - start_seq:.2f} san\n")


    print('>>>>>>>>Downloading with gather is in progress...<<<<<<<<<<<<<')
    start_async = time.time()
    tasks = [download_file(name) for name in names]
    async_results = await asyncio.gather(*tasks)
    end_async = time.time()
    
    print(f"\nFiles (Gather): {async_results}")
    print(f"Gather duration: {end_async - start_async:.2f} san")

if __name__ == "__main__":
    asyncio.run(main())
