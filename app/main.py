from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.engines.dorker import DorkingEngine
from app.engines.social import SocialScanner # Akan dibuat di part berikutnya
import uvicorn

app = FastAPI(title="SPY-SOURCE OSINT ENGINE")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

dorker = DorkingEngine()

@app.get("/investigate")
async def investigate(target: str):
    if not target:
        raise HTTPException(status_code=400, detail="Target is required")
    
    # 1. Jalankan Dorking
    dork_results = dorker.search(target)
    
    # 2. Rangkum Hasil untuk AI Analysis
    # (Di sini kita menyiapkan data mentah untuk disuapkan ke Gemini)
    
    return {
        "status": "success",
        "target": target,
        "results": {
            "dorking": dork_results,
            "social_media": [], # Placeholder
            "leaks_found": len(dork_results)
        }
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)
