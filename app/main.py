import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

# Import internal modules
from app.engines.dorker import DorkingEngine
from app.engines.social import SocialScanner
from app.utils.formatter import AIFormatter

app = FastAPI(
    title="SPY-SOURCE OSINT ENGINE",
    description="Unified Intelligence Aggregator by Indonesia OSINT",
    version="1.0.0"
)

# Konfigurasi CORS agar Frontend React bisa mengakses Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inisialisasi Engine
dorker = DorkingEngine()
social_scanner = SocialScanner()

@app.get("/")
async def root():
    return {
        "status": "Online",
        "system": "SPY-SOURCE OSINT",
        "author": "Rolandino / Indonesia OSINT"
    }

@app.get("/investigate")
async def investigate(target: str):
    """
    Endpoint utama untuk melakukan investigasi menyeluruh.
    """
    if not target:
        raise HTTPException(status_code=400, detail="Target identity is required")

    try:
        # 1. Jalankan Google Dorking (.go.id & .ac.id focus)
        dork_results = dorker.search(target)

        # 2. Jalankan Social Media Enumeration secara Asynchronous
        social_results = await social_scanner.scan(target)

        # 3. Generate AI-Ready Prompt untuk analisis lanjutan
        ai_prompt = AIFormatter.format_for_ai(target, dork_results, social_results)

        return {
            "status": "success",
            "target": target,
            "summary": {
                "documents_found": len(dork_results),
                "profiles_found": len(social_results)
            },
            "results": {
                "dorking": dork_results,
                "social_media": social_results,
                "ai_ready_prompt": ai_prompt
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    # Menjalankan server di port 8001
    uvicorn.run(app, host="0.0.0.0", port=8001)
