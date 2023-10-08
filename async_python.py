import asyncio
import aiohttp 
async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text() 
        
async def main():
    urls = ["https://openai.com", "https://github.com"]
    tasks = [fetch_url(url) for url in urls]
    results = await asyncio.gather(*tasks)
    for url, content in zip(urls, results):
        print(f"{url}: {len(content)} bytes") 
        
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    