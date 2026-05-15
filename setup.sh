#!/bin/bash
echo "--- SPY-SOURCE OSINT: INSTALLER ---"

# Install Backend
echo "[*] Installing Python dependencies..."
pip install -r requirements.txt

# Install Frontend
echo "[*] Installing React dependencies..."
cd web
npm install
npm install axios react-scripts

echo "--- INSTALLATION DONE ---"
echo "Run Backend: uvicorn app.main:app --reload --port 8001"
echo "Run Frontend: cd web && npm start"
