#!/usr/bin/env python3
"""
Backend sunucusunu çalıştırmak için basit script
"""

import uvicorn
from backend_api import app

if __name__ == "__main__":
    print("🚀 Zihin Yolculuğu Backend API başlatılıyor...")
    print("📍 Sunucu: http://localhost:8000")
    print("📊 Health Check: http://localhost:8000/api/health")
    print("🛑 Durdurmak için Ctrl+C tuşlayın")
    
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000,
        reload=True,  # Geliştirme için otomatik yenileme
        log_level="info"
    ) 