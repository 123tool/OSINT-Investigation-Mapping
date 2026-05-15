import httpx
import asyncio

class SocialScanner:
    def __init__(self):
        # Daftar platform yang sering digunakan di Indonesia
        self.platforms = {
            "Instagram": "https://www.instagram.com/{}/",
            "TikTok": "https://www.tiktok.com/@{}",
            "Facebook": "https://www.facebook.com/{}",
            "GitHub": "https://github.com/{}",
            "Pinterest": "https://id.pinterest.com/{}/",
            "Twitter/X": "https://twitter.com/{}",
        }
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

    async def check_platform(self, client, name, url, target):
        formatted_url = url.format(target)
        try:
            response = await client.get(formatted_url, timeout=5.0)
            if response.status_code == 200:
                return {"platform": name, "status": "Found", "link": formatted_url}
            return None
        except:
            return None

    async def scan(self, target):
        """Menjalankan scanning secara paralel agar cepat"""
        target_clean = target.replace(" ", "").lower()
        async with httpx.AsyncClient(headers=self.headers, follow_redirects=True) as client:
            tasks = [self.check_platform(client, name, url, target_clean) 
                     for name, url in self.platforms.items()]
            results = await asyncio.gather(*tasks)
            return [r for r in results if r is not None]
