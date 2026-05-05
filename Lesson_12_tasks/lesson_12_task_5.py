'''
Verilən URL-lər
urls = [
 "https://example.com",
 "https://google.com",
 "https://github.com"
]

Tələblər
aiohttp istifadə edin
async with ClientSession yaradın
hər URL üçün async request
göndərin
status code çap edin
asyncio.gather ilə hamısını birlikdə
işlədin

Gözlənilən nəticə
Hər sayt üçün status code görünməlidir.
Məsələn: https://example.com -> 200
'''



import asyncio
import aiohttp

urls = [
    "https://example.com",
    "https://google.com",
    "https://github.com"
]

async def fetch(session, url):
    async with session.get(url) as response:
        status = response.status
        print(f"{url} -> {status}")
        return status

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        
        results = await asyncio.gather(*tasks)
        
        print(f"\nAll status codes: {results}")

if __name__ == "__main__":
    asyncio.run(main())