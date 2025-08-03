import requests
import json
from datetime import datetime

# API base URL
BASE_URL = "http://localhost:8001"

def test_backend_connection():
    """Backend bağlantısını test et"""
    print("🔍 Backend Bağlantı Testi Başlatılıyor...")
    
    try:
        # Health check
        response = requests.get(f"{BASE_URL}/api/health")
        if response.status_code == 200:
            print("✅ Backend çalışıyor!")
            print(f"   - Status: {response.json()['status']}")
            print(f"   - Version: {response.json()['version']}")
        else:
            print(f"❌ Backend hatası: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend bağlantı hatası: {e}")
        return False
    
    return True

def test_frontend_endpoints():
    """Frontend'in kullanacağı endpoint'leri test et"""
    print("\n🔍 Frontend Endpoint Testleri Başlatılıyor...")
    
    # Test 1: Dashboard data
    print("\n1. Dashboard Data Testi:")
    try:
        response = requests.get(f"{BASE_URL}/api/dashboard-data/U1")
        if response.status_code == 200:
            data = response.json()
            print("✅ Dashboard data başarılı!")
            print(f"   - Performance trend: {len(data.get('performance_trend', []))} gün")
            print(f"   - Daily scores: {len(data.get('daily_scores', []))} gün")
        else:
            print(f"❌ Dashboard data hatası: {response.status_code}")
    except Exception as e:
        print(f"❌ Dashboard data hatası: {e}")
    
    # Test 2: User stats
    print("\n2. User Stats Testi:")
    try:
        response = requests.get(f"{BASE_URL}/api/user-stats/U1")
        if response.status_code == 200:
            data = response.json()
            print("✅ User stats başarılı!")
            print(f"   - Daily score: {data.get('daily_score')}")
            print(f"   - Total tests: {data.get('total_tests')}")
            print(f"   - Badges: {len(data.get('badges_earned', []))}")
        else:
            print(f"❌ User stats hatası: {response.status_code}")
    except Exception as e:
        print(f"❌ User stats hatası: {e}")
    
    # Test 3: Test result submission
    print("\n3. Test Result Submission Testi:")
    try:
        test_data = {
            "user_id": "U1",
            "test_type": "attention_stroop",
            "difficulty": "medium",
            "score": 85.5,
            "accuracy": 0.85,
            "reaction_time": 1500.0,
            "completed_at": datetime.now().isoformat(),
            "responses": ["kırmızı", "mavi", "yeşil"],
            "reaction_times": [1200, 1400, 1600],
            "total_time": 4200
        }
        
        response = requests.post(f"{BASE_URL}/api/test-result", json=test_data)
        if response.status_code == 200:
            data = response.json()
            print("✅ Test result submission başarılı!")
            print(f"   - Status: {data.get('status')}")
            print(f"   - Message: {data.get('message')}")
        else:
            print(f"❌ Test result submission hatası: {response.status_code}")
    except Exception as e:
        print(f"❌ Test result submission hatası: {e}")

def test_adaptive_test_endpoint():
    """Adaptif test endpoint'ini test et"""
    print("\n4. Adaptif Test Endpoint Testi:")
    try:
        test_data = {
            "user_id": "U1",
            "test_type": "attention_stroop",
            "difficulty": "medium",
            "score": 85.5,
            "accuracy": 0.85,
            "reaction_time": 1500.0,
            "completed_at": datetime.now().isoformat(),
            "cognitive_load": 0.6,
            "stress_level": 2
        }
        
        response = requests.post(f"{BASE_URL}/api/adaptive-test", json=test_data)
        if response.status_code == 200:
            data = response.json()
            print("✅ Adaptif test endpoint başarılı!")
            print(f"   - Next difficulty: {data.get('next_difficulty')}")
            print(f"   - Daily score: {data.get('daily_score')}")
            print(f"   - User segment: {data.get('user_segment')}")
            if data.get('suggested_achievement'):
                print(f"   - Suggested achievement: {data.get('suggested_achievement')}")
        else:
            print(f"❌ Adaptif test endpoint hatası: {response.status_code}")
    except Exception as e:
        print(f"❌ Adaptif test endpoint hatası: {e}")

def test_badge_rules():
    """Rozet kurallarını test et"""
    print("\n5. Badge Rules Testi:")
    try:
        response = requests.get(f"{BASE_URL}/api/badge-rules")
        if response.status_code == 200:
            data = response.json()
            print("✅ Badge rules başarılı!")
            print(f"   - Toplam rozet kuralı: {len(data.get('badge_rules', []))}")
            for rule in data.get('badge_rules', []):
                print(f"   - {rule.get('badge_name')}: {rule.get('badge_description')}")
        else:
            print(f"❌ Badge rules hatası: {response.status_code}")
    except Exception as e:
        print(f"❌ Badge rules hatası: {e}")

if __name__ == "__main__":
    print("🚀 Frontend-Backend Bağlantı Test Suite Başlatılıyor...")
    print("=" * 60)
    
    # Backend bağlantısını test et
    if test_backend_connection():
        # Frontend endpoint'lerini test et
        test_frontend_endpoints()
        test_adaptive_test_endpoint()
        test_badge_rules()
    
    print("\n" + "=" * 60)
    print("🏁 Tüm testler tamamlandı!")
    print("\n💡 Frontend'i test etmek için:")
    print("   1. Backend'in çalıştığından emin olun (python backend_api.py)")
    print("   2. Frontend'i bir web sunucusuyla açın")
    print("   3. http://localhost:8001/api/health adresini kontrol edin") 