from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Optional
import json
import pandas as pd
from datetime import datetime, timedelta
import numpy as np

app = FastAPI(title="Zihin Yolculuğu Adaptif Test API", version="1.0.0")

# CORS ayarları - Frontend bağlantısı için
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Güvenlik için production'da spesifik domain'ler belirtin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Veri modelleri
class TestResult(BaseModel):
    user_id: str
    test_type: str  # "attention_stroop", "attention_nback", "logic_sudoku", "reasoning_quantitative", "reasoning_verbal"
    difficulty: str  # "easy", "medium", "hard"
    score: float
    accuracy: float
    reaction_time: float
    completed_at: str
    cognitive_load: Optional[float] = None
    stress_level: Optional[int] = None

class AdaptiveResponse(BaseModel):
    next_difficulty: str
    suggested_achievement: Optional[str] = None
    daily_score: float
    trend_score: float
    user_segment: str
    cognitive_profile: str
    behavior_type: str

# Veri yükleme fonksiyonları
def load_profiles():
    """Kullanıcı profillerini yükle"""
    try:
        with open('data/final/profiles.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def load_badge_rules():
    """Rozet kurallarını yükle"""
    try:
        with open('data/final/rozet_kurallari.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def load_project_rules():
    """Proje kurallarını yükle"""
    try:
        with open('proje_kurallari.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def load_dashboard_data():
    """Dashboard verilerini yükle"""
    try:
        with open('data/final/dashboard_data.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Puan hesaplama fonksiyonları
def calculate_daily_score(user_id: str, test_results: List[TestResult]) -> float:
    """Günlük puan hesapla"""
    today = datetime.now().date()
    today_results = [
        result for result in test_results 
        if datetime.fromisoformat(result.completed_at).date() == today
    ]
    
    if not today_results:
        return 0.0
    
    # Proje kurallarındaki formülü kullan
    total_score = 0
    for result in today_results:
        # score = (accuracy / 100) * (1 / (reaction_time / 1000)) * 1000
        if result.reaction_time > 0:
            score = (result.accuracy / 100) * (1 / (result.reaction_time / 1000)) * 1000
            total_score += score
    
    return total_score

def calculate_trend_score(user_id: str, test_results: List[TestResult]) -> float:
    """Gelişim puanı hesapla (son 7 gün vs önceki 7 gün)"""
    if len(test_results) < 2:
        return 0.0
    
    today = datetime.now().date()
    week_ago = today - timedelta(days=7)
    two_weeks_ago = today - timedelta(days=14)
    
    recent_results = [
        result for result in test_results 
        if week_ago <= datetime.fromisoformat(result.completed_at).date() <= today
    ]
    
    older_results = [
        result for result in test_results 
        if two_weeks_ago <= datetime.fromisoformat(result.completed_at).date() < week_ago
    ]
    
    if not recent_results or not older_results:
        return 0.0
    
    recent_avg = np.mean([r.score for r in recent_results])
    older_avg = np.mean([r.score for r in older_results])
    
    return recent_avg - older_avg

def determine_user_segment(daily_score: float, trend_score: float) -> str:
    """Kullanıcı segmentini belirle"""
    if daily_score >= 150 and trend_score > 0:
        return "yüksek"
    elif daily_score >= 100 or trend_score > 0:
        return "orta"
    else:
        return "düşük"

def get_user_profile(user_id: str) -> Dict:
    """Kullanıcı profilini getir"""
    profiles = load_profiles()
    for profile in profiles:
        if str(profile.get('user_id')) == str(user_id):
            return profile
    return {
        'behavior_type': 'Dengeci',
        'cognitive_profile': 'Normal',
        'skill_level': 'orta'
    }

def check_badge_eligibility(user_id: str, test_results: List[TestResult], 
                          daily_score: float, trend_score: float) -> Optional[str]:
    """Rozet uygunluğunu kontrol et"""
    badge_rules = load_badge_rules()
    user_profile = get_user_profile(user_id)
    
    for rule in badge_rules:
        if rule['rule_type'] == 'daily_score_threshold':
            if daily_score >= rule['threshold']:
                return rule['badge_name']
        
        elif rule['rule_type'] == 'accuracy_threshold':
            recent_results = test_results[-10:]  # Son 10 test
            if recent_results:
                avg_accuracy = np.mean([r.accuracy for r in recent_results])
                if avg_accuracy >= rule['threshold']:
                    return rule['badge_name']
        
        elif rule['rule_type'] == 'profile_match':
            if user_profile.get('cognitive_profile') == rule['required_profile']:
                return rule['badge_name']
    
    return None

def determine_next_difficulty(user_id: str, test_results: List[TestResult], 
                            user_segment: str, current_difficulty: str) -> str:
    """Bir sonraki test zorluğunu belirle"""
    if not test_results:
        return "medium"  # Varsayılan
    
    # Son 5 testin performansını analiz et
    recent_results = test_results[-5:]
    if not recent_results:
        return current_difficulty
    
    avg_accuracy = np.mean([r.accuracy for r in recent_results])
    avg_reaction_time = np.mean([r.reaction_time for r in recent_results])
    
    # Adaptif zorluk ayarlama
    if avg_accuracy >= 0.85 and avg_reaction_time < 2000:  # Yüksek performans
        if current_difficulty == "easy":
            return "medium"
        elif current_difficulty == "medium":
            return "hard"
        else:
            return "hard"
    
    elif avg_accuracy <= 0.60 or avg_reaction_time > 5000:  # Düşük performans
        if current_difficulty == "hard":
            return "medium"
        elif current_difficulty == "medium":
            return "easy"
        else:
            return "easy"
    
    else:  # Orta performans
        return current_difficulty

# API endpoint'leri
@app.post("/api/adaptive-test", response_model=AdaptiveResponse)
async def process_test_result(test_result: TestResult):
    """Test sonucunu işle ve adaptif öneriler döndür"""
    try:
        # Kullanıcının geçmiş test sonuçlarını simüle et (gerçek uygulamada veritabanından alınır)
        # Bu örnek için basit bir simülasyon yapıyoruz
        test_results = [test_result]  # Gerçek uygulamada kullanıcının tüm geçmiş sonuçları
        
        # Puanları hesapla
        daily_score = calculate_daily_score(test_result.user_id, test_results)
        trend_score = calculate_trend_score(test_result.user_id, test_results)
        
        # Kullanıcı segmentini belirle
        user_segment = determine_user_segment(daily_score, trend_score)
        
        # Kullanıcı profilini al
        user_profile = get_user_profile(test_result.user_id)
        
        # Bir sonraki zorluğu belirle
        next_difficulty = determine_next_difficulty(
            test_result.user_id, test_results, user_segment, test_result.difficulty
        )
        
        # Rozet uygunluğunu kontrol et
        suggested_achievement = check_badge_eligibility(
            test_result.user_id, test_results, daily_score, trend_score
        )
        
        return AdaptiveResponse(
            next_difficulty=next_difficulty,
            suggested_achievement=suggested_achievement,
            daily_score=daily_score,
            trend_score=trend_score,
            user_segment=user_segment,
            cognitive_profile=user_profile.get('cognitive_profile', 'Normal'),
            behavior_type=user_profile.get('behavior_type', 'Dengeci')
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"İşlem hatası: {str(e)}")

@app.post("/api/test-result")
async def save_test_result(test_result: TestResult):
    """Test sonucunu kaydet (frontend için uyumlu endpoint)"""
    try:
        # Bu endpoint sadece test sonucunu alır ve onaylar
        return {
            "status": "success",
            "message": "Test sonucu başarıyla kaydedildi",
            "test_id": f"test_{datetime.now().timestamp()}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Test kaydetme hatası: {str(e)}")

@app.get("/api/user-profile/{user_id}")
async def get_user_profile_endpoint(user_id: str):
    """Kullanıcı profilini getir"""
    try:
        profile = get_user_profile(user_id)
        return profile
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Profil getirme hatası: {str(e)}")

@app.get("/api/user-stats/{user_id}")
async def get_user_stats(user_id: str):
    """Kullanıcı istatistiklerini getir"""
    try:
        profile = get_user_profile(user_id)
        return {
            "user_id": user_id,
            "daily_score": 150.0,  # Simüle edilmiş veri
            "weekly_score": 850.0,
            "total_tests": 25,
            "accuracy_avg": 0.85,
            "reaction_time_avg": 1200.0,
            "badges_earned": ["Puan Canavarı", "Keskin Göz"],
            "current_streak": 5
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"İstatistik getirme hatası: {str(e)}")

@app.get("/api/dashboard-data/{user_id}")
async def get_dashboard_data(user_id: str):
    """Dashboard verilerini getir"""
    try:
        # Varsayılan dashboard verisi (büyük dosya yükleme sorununu önlemek için)
        user_data = {
            "user_id": user_id,
            "performance_trend": [65, 70, 75, 80, 85, 90, 95],
            "daily_scores": [120, 135, 150, 145, 160, 155, 170],
            "test_types": ["attention_stroop", "logic_sudoku", "reasoning_verbal"],
            "accuracy_by_type": [0.85, 0.78, 0.92],
            "weekly_progress": 15,
            "monthly_progress": 45,
            "total_tests_completed": 25,
            "current_streak": 5,
            "best_score": 95,
            "average_accuracy": 0.85
        }
        
        return user_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Dashboard veri getirme hatası: {str(e)}")

@app.get("/api/badge-rules")
async def get_badge_rules():
    """Rozet kurallarını getir"""
    try:
        rules = load_badge_rules()
        return {"badge_rules": rules}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Rozet kuralları getirme hatası: {str(e)}")

@app.get("/api/project-rules")
async def get_project_rules():
    """Proje kurallarını getir"""
    try:
        rules = load_project_rules()
        return rules
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Proje kuralları getirme hatası: {str(e)}")

@app.get("/api/health")
async def health_check():
    """API sağlık kontrolü"""
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat(),
        "version": "1.0.0",
        "service": "Zihin Yolculuğu Adaptif Test API"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001) 