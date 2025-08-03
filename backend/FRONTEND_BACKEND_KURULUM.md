# Frontend-Backend Bağlantı Kurulum Kılavuzu

## 🚀 Hızlı Başlangıç

### 1. Backend'i Başlatın
```bash
python backend_api.py
```
Backend `http://localhost:8001` adresinde çalışacak.

### 2. Frontend'i Başlatın
```bash
cd frontend
python -m http.server 8080
```
Frontend `http://localhost:8080` adresinde çalışacak.

### 3. Test Edin
- Backend: http://localhost:8001/api/health
- Frontend: http://localhost:8080

## 📋 Sistem Gereksinimleri

### Backend Gereksinimleri
```bash
pip install fastapi uvicorn pydantic pandas numpy python-multipart
```

### Frontend Gereksinimleri
- Modern web tarayıcısı (Chrome, Firefox, Safari, Edge)
- Python HTTP sunucusu (basit test için)

## 🔧 API Endpoint'leri

### Backend API (Port 8001)

| Endpoint | Method | Açıklama |
|----------|--------|----------|
| `/api/health` | GET | API sağlık kontrolü |
| `/api/dashboard-data/{user_id}` | GET | Dashboard verileri |
| `/api/user-stats/{user_id}` | GET | Kullanıcı istatistikleri |
| `/api/test-result` | POST | Test sonucu gönderme |
| `/api/adaptive-test` | POST | Adaptif test önerileri |
| `/api/badge-rules` | GET | Rozet kuralları |
| `/api/project-rules` | GET | Proje kuralları |

### Frontend (Port 8080)
- Ana sayfa: `http://localhost:8080/index.html`
- Dashboard: Otomatik olarak backend'den veri çeker

## 🔗 Bağlantı Testleri

### Backend Test
```bash
python test_frontend_backend_connection.py
```

### Manuel Test
```bash
# Backend sağlık kontrolü
curl http://localhost:8001/api/health

# Dashboard verisi
curl http://localhost:8001/api/dashboard-data/U1

# Kullanıcı istatistikleri
curl http://localhost:8001/api/user-stats/U1
```

## 🛠️ Sorun Giderme

### Backend Başlatılamıyor
**Hata:** `[Errno 10048] error while attempting to bind on address ('0.0.0.0', 8001)`

**Çözüm:**
1. Port 8001'i kullanan diğer uygulamaları kapatın
2. Farklı bir port kullanın (backend_api.py dosyasında değiştirin)
3. Frontend'deki API_BASE_URL'i güncelleyin

### Frontend Backend'e Bağlanamıyor
**Hata:** `Failed to fetch` veya `CORS error`

**Çözüm:**
1. Backend'in çalıştığından emin olun
2. CORS ayarlarının doğru olduğunu kontrol edin
3. API_BASE_URL'in doğru olduğunu kontrol edin

### Dashboard Verisi Yüklenmiyor
**Hata:** `Dashboard verisi yüklenirken hata oluştu`

**Çözüm:**
1. Backend'in çalıştığını kontrol edin
2. Network sekmesinde API çağrılarını kontrol edin
3. Console'da hata mesajlarını kontrol edin

## 📊 Test Senaryoları

### 1. Temel Bağlantı Testi
1. Backend'i başlatın: `python backend_api.py`
2. Frontend'i başlatın: `cd frontend && python -m http.server 8080`
3. http://localhost:8080 adresine gidin
4. Dashboard'ın yüklendiğini kontrol edin

### 2. Test Sonucu Gönderme
1. Frontend'de "Testi Başlat" butonuna tıklayın
2. Testi tamamlayın
3. Sonucun backend'e gönderildiğini kontrol edin
4. Dashboard'ın güncellendiğini kontrol edin

### 3. Rozet Sistemi Testi
1. Yüksek puanlı bir test tamamlayın
2. Rozet kazanıp kazanmadığınızı kontrol edin
3. Dashboard'da rozetlerin göründüğünü kontrol edin

## 🔧 Geliştirici Notları

### Backend Yapılandırması
- **Port:** 8001 (değiştirilebilir)
- **CORS:** Tüm origin'lere izin verilir (geliştirme için)
- **Logging:** Uvicorn logları konsola yazdırılır

### Frontend Yapılandırması
- **API URL:** `http://localhost:8001/api`
- **Kullanıcı ID:** `U1` (varsayılan)
- **Test Türü:** `attention_stroop` (varsayılan)

### Veri Akışı
1. Frontend → Backend: Test sonuçları
2. Backend → Frontend: Dashboard verileri, öneriler
3. Backend → Frontend: Rozet önerileri

## 🎯 Başarı Kriterleri

✅ Backend çalışıyor ve health check geçiyor  
✅ Frontend backend'e bağlanabiliyor  
✅ Dashboard verisi yükleniyor  
✅ Test sonuçları gönderiliyor  
✅ Rozet sistemi çalışıyor  
✅ Adaptif öneriler çalışıyor  

## 🚨 Güvenlik Notları

- **Geliştirme Ortamı:** CORS tüm origin'lere açık
- **Production:** Spesifik domain'ler belirtilmeli
- **Veri:** Şu anda dosya tabanlı, production'da veritabanı kullanılmalı

## 📞 Destek

Sorun yaşarsanız:
1. Console loglarını kontrol edin
2. Network sekmesinde API çağrılarını inceleyin
3. Backend loglarını kontrol edin
4. Test scriptini çalıştırın: `python test_frontend_backend_connection.py` 