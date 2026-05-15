from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

class DorkingEngine:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.cse_id = os.getenv("GOOGLE_CSE_ID")
        if self.api_key and self.cse_id:
            self.service = build("customsearch", "v1", developerKey=self.api_key)
        else:
            self.service = None

    def generate_queries(self, target):
        """Membuat list dorking spesifik target Indonesia"""
        return [
            f'site:*.go.id "{target}"',
            f'site:*.ac.id "{target}"',
            f'filetype:pdf "{target}" "NIK" OR "NOMOR HP"',
            f'filetype:xlsx "{target}" "DAFTAR" OR "DATABASE"',
            f'site:facebook.com "{target}" "081"'
        ]

    def search(self, target):
        if not self.service:
            return {"error": "API Key not configured"}
        
        queries = self.generate_queries(target)
        all_results = []

        for q in queries:
            try:
                res = self.service.cse().list(q=q, cx=self.cse_id).execute()
                if "items" in res:
                    for item in res["items"]:
                        all_results.append({
                            "title": item["title"],
                            "link": item["link"],
                            "snippet": item.get("snippet", ""),
                            "query_used": q
                        })
            except Exception as e:
                print(f"Error on query {q}: {e}")
        
        return all_results
