import httpx
import asyncio

class AsyncHTTPClient:

    def __init__(self):
        self.client = httpx.AsyncClient(timeout=15.0)
        self.max_retries = 3

    async def get(self, url):

        for attempt in range(self.max_retries + 1):

            try:
                response = await self.client.get(url)
                response.raise_for_status()
                return response

            except httpx.RequestError:
                if attempt == self.max_retries:
                    raise

                await asyncio.sleep(2 ** attempt)

    async def close(self):
        await self.client.aclose()


async def fetch(client, url):
    response = await client.get(url)
    data = response.json()

    return {
        "title": data.get("title"),
        "price": data.get("price"),
        "brand": data.get("brand"),
        "category": data.get("category")
    }

async def main():
    client = AsyncHTTPClient
    url = "https://dummyjson.com/products/{}",
    try:
        for i in range(0,20):
            results = await fetch(client, url.format(i))
            print(results)
    except httpx.HTTPStatusError as e:
        print(e)
    except httpx.RequestError as re:
        print(re)
    finally:
        await client.close()

asyncio.run(main())

