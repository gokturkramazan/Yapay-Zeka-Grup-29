# Takım İsmi 
Yapay Zeka ve Teknoloji Akademisi Bootcamp 2025 Yapay Zeka Alanı Grup 29 

# Takım Üyeleri
- **Hamza Derim** - Product Owner
- **Ramazan Göktürk Şamlıoğlu** - Scrum Master
- **Müzeyyen Miray Kahveci** - Developer
- **Sara Karaçaylı** - Developer
- **Kader Tuğba Yaramış** - Developer

# *CognitiveTrack – Bilişsel Beceri Gelişimi Takip Sistemi*
## **🔍 1. Projenin Amacı**<br>

CognitiveTrack, öğrencilerin veya yetişkin kullanıcıların bilişsel performanslarını günlük kısa testlerle takip eden, kişiye özel egzersizler öneren ve oyunlaştırma ile motivasyonu artıran bir platformdur.
Amaç, yalnızca akademik başarıyı değil, bilişsel gelişimi de yakından izleyip destekleyebilmektir. Bu sayede:
- Nörogelişimsel bozuklukların (disleksi, ADHD vb.) etkileri daha erken saptanabilir,
- Kullanıcılar güçlü/zayıf yönlerini keşfedip buna göre gelişim gösterebilir,
- Veliler ve uzmanlar gelişimi takip edebilir.

## **🎯 2. Hedef Kitle**<br>
- İlkokul – Ortaokul öğrencileri (özellikle dikkat, bellek gelişimi ihtiyacı olanlar)
- Özel gereksinimli bireyler (Disleksi, Dikkat Eksikliği ve Hiperaktivite Bozukluğu vb.)
- Bilişsel egzersiz isteyen yetişkinler (ör. yaşa bağlı zihinsel zindelik çalışmaları)

## **⚙️ 3. Ana Bileşenler ve Özellikler (Proje Sonunda Hedeflenen)**

| Bileşen                | Açıklama                                                                 |
|------------------------|--------------------------------------------------------------------------|
| Günlük Egzersizler     | Stroop, N-back, Flanker, Mental Rotation gibi test temelli mini oyunlar sunar. |
| Zaman Serisi Analizi   | Kullanıcının günlük skorları ile bilişsel beceri gelişimi takip edilir.        |
| AI Destekli Öneri Sistemi | Zayıf yönleri analiz edip kişiye özel egzersizler önerir.                   |
| Rozet/Seviye Sistemi   | Gamification ile kullanıcı motivasyonu artırılır.                           |
| Veli / Uzman Paneli    | Gelişim grafikleri ve yorumlama yardımı sunar.                              |

## 🧩 4. Kullanıcı Akışı
**1.** Kullanıcı (öğrenci/yetişkin) günlük bilişsel test oyunlarını oynar.<br>
**2.** Sistem, bu testlerden gelen verilerle gelişim analizini yapar.<br>
**3.** AI öneri sistemi, kullanıcının zayıf yönlerine odaklı yeni egzersizler sunar.<br>
**4.** Gamification sistemi ile rozetler, seviye atlamalarla kullanıcıyı teşvik eder.<br>
**5.** Veli ya da uzman paneli ile haftalık gelişim raporları ve grafikler sunulur.<br>

## 🧪 5. Kullanılması Planlanan Kaggle/HuggingFace Veri Setleri ve Entegrasyonları

Projede gerçek dünyadan alınmış 5 veri setinin kullanılması planlanıyor. Sprintlerde kullanım durumlarının detaylarını belirteceğiz.

| Dataset                         | Kullanım                                              | Görev                                       |
|----------------------------------|--------------------------------------------------------|----------------------------------------------|
| Stroop & Flanker (Figshare)     | Dikkat ölçen test performans analizi                 | Skor takibi, öneri hazırlığı                |
| n-Back Dataset (Huggingface)    | Çalışma belleği seviyesine göre kullanıcı sınıflandırma | AI için adaptif öneriler                    |
| Reaction Time Dataset (Kaggle)  | Yaş, cinsiyet, cihaz türüne göre hız analizleri       | Segmentasyon & benchmark                    |
| Cognitive Load Dataset          | Zihinsel yük – moral ölçümü                          | Kişiselleştirme, moral desteği              |
| Students Performance Dataset    | Akademik başarı – bilişsel skor ilişkisi             | Başarı sınıflandırması, AI önerileri        |

Bu veri setlerinin projeye bilimsel geçerlik, model eğitimi ve benchmark sağlaması amaçlanıyor.

## 🧰 6. Planlanan Teknoloji Altyapısı

| Katman                    | Teknoloji                                             |
|---------------------------|--------------------------------------------------------|
| Frontend                 | React.js (arayüz) veya Unity WebGL (oyunlar için)     |
| Backend                  | FastAPI veya Node.js                                   |
| AI / ML                  | Scikit-learn, Firebase ML Kit                          |
| Veritabanı               | Firebase Firestore veya MongoDB                        |
| Analitik / Görselleştirme | Chart.js / D3.js                                       |


## 🧠 8. Hedeflenen Eğitimsel Katkı ve Yenilik
- Geleneksel sistemlerin aksine akademik değil bilişsel gelişime odaklanır.
- Bireylerin gelişimini veriyle şeffaf biçimde izleme imkânı verir.
- Oyunlaştırma + yapay zekâ + gelişim takibi üçlüsünü entegre eden yenilikçi bir yapıya sahiptir.
- Nörogelişimsel bozuklukların erken fark edilmesine destek olur.

<br>
<br>

## --- SPRINT 1 ---


