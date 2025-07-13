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


## 🧠 7. Hedeflenen Eğitimsel Katkı ve Yenilik
- Geleneksel sistemlerin aksine akademik değil bilişsel gelişime odaklanır.
- Bireylerin gelişimini veriyle şeffaf biçimde izleme imkânı verir.
- Oyunlaştırma + yapay zekâ + gelişim takibi üçlüsünü entegre eden yenilikçi bir yapıya sahiptir.
- Nörogelişimsel bozuklukların erken fark edilmesine destek olur.

<br>
<br>

## --- SPRINT 1 - Veri Keşfi, Proje İskeleti ve Prototip Başlangıcı ---
*20 Haziran - 6 Temmuz* <br>
<br>
**Sprint Amacı:**
- Kullanılacak veri setlerini indirip ilk incelemeleri yapmak
- Temel kullanıcı senaryolarını netleştirmek
- Hangi oyunların hangi verilerle eşleşeceğini belirlemek
- Projenin minimum iskelet yapısını (klasör, repo, bağlantı) oluşturmak<br><br>

**Sprint içinde tamamlanması tahmin edilen puan:** 80 Puan<br> <br>
**Puan Tamamlama Mantığı:** İlk sprint için 80 puan, ikinci sprint için 120 puan ve üçüncü sprint için 100 puan hedefi vardır. Bu dönemde bazı ekip üyelerinin final sınavları sebebiyle daha düşük bir puan hedefi belirlenmiştir. İkinci sprintte bu eksiğin kapanmasını amaçlamaktayız. Genel sprint tablosu içerisinde "Proje Yapısı ve Veri Toplama" bölümleri 5'er puan, "Veri Keşfi (EDA)" bölümleri 10'ar puan, "Test & Beceri Eşleşmesi" bölümleri 10'ar puan olarak belirlenmiştir. <br> <br>
**Backlog düzeni ve Story seçimleri:** Backlog'umuz görevlerin parçalar halinde tamamlanması üzerine düzenlenmiş olup tamamlananan görevlerin sonraki sprintlerde ve farklı görevlerde yatay olarak kullanılabilmesine imkan tanıyacak şekilde düzenlenmiştir. 2 farklı ekip ile ilerlemeyi planlamaktayız. <br> 
**Veri Bilimi Ekibi:** Ramazan, Hamza, Miray <br> 
**AI Geliştirme Ekibi:** Sara, Tuğba <br> <br> 
**Sprint Review:** 
- Görev dağılımları yapılmış, product owner, scrum master ve developerlar belirlenmiştir.<br> <br> 
- Proje konu fikirleri öne sunulmuş ve ortak projeye karar verilmiştir.<br> <br> 
- Proje her sprint aşamasına göre hedef odaklı palnlanıp, veri bilimi-yapay zeka hedefleri whatsap üzerinden takım bilgilendirilmiştir.<br> <br> 
- **Sprint review katılımcıları:** Ramazan Göktürk, Hamza DERİM<br> <br> 
- **Sprint Retrospective** Görev dağılımları ve ilerleyiş kapsamlı olarak ekiple paykaşılmıştır. <br> <br> 
- **Veri Bilimci 1**: Hamza DERİM, **Veri Bilimci 2:** Ramazan Göktürk, **Veri Bilimci 3:** Miray Kahveci görevler paylaşılmıştır. <br> <br> 
- **AI Geliştirme Ekibi:** Sara, Tuğba Grupta aktif olmayarak görev almamıştır. <br> <br> 
- CognitiveTrack_Rol_Dagilimi_Kapsamli.docx<br> <br> 

**Daily Scrum:** Daily Scrum toplantıları ve iletişim WhatsApp üzerinden sağlanmaktadır. <br> <br>

**🧩 Genel Sprint Tablosu : CognitiveTrack – Sprint 1**
| **List** (Kategori)        | **Card (Görev)**                                          | **Açıklama / Alt Görevler**                                                                                        | **Sorumlu**               |**Puan**                 
| -------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------- |----------------|
| 📂 Proje Yapısı            | GitHub repo kurulumu                                      | ReadMe’ye proje özellikleri eklenecek.                                                                             | Ramazan                   |5               |
| 📂 Proje Yapısı            | Canva dokümanı/çalışma tahtası hazırlanması               | Projeye katkı sağlayacak görsel tasarım ürünleri için taslak araştırması                                           | Ramazan                   |5               |
| 📦 Veri Toplama            | İlgili veri setlerinin paylaşılması                       | Stroop, N-back, Reaction Time, Cognitive Load, Student Performance veri setleri veri ekibi ile paylaşılacak.       | Hamza                     |5               |
| 📦 Veri Toplama            | Veri setlerinin açıklamalarının çıkarılması               | Her veri setinin açıklaması notebook içerisinde yapılacak.                                                        | Veri Bilimi Ekibi         |5               |
| 📊 Veri Keşfi (EDA)        | Stroop / Flanker veri seti için EDA                       | Ortalama, dağılım, eksik veriler, örnek grafik                                                                     | Veri Bilimi Ekibi         |10              |
| 📊 Veri Keşfi (EDA)        | N-back veri seti için EDA                                 | Doğruluk, n\_level analizi, dağılım                                                                                | Veri Bilimi Ekibi         |10              |
| 📊 Veri Keşfi (EDA)        | Reaction Time veri seti için EDA                          | Cinsiyet, yaş, cihaz tipi kırılımlarında tepki süresi dağılımı                                                     | Veri Bilimi Ekibi         |10              |
| 📊 Veri Keşfi (EDA)        | Student Performance veri seti için EDA                         | Zihinsel yük, stres, frustration değişkenlerinin incelenmesi                                                       | Veri Bilimi Ekibi         |10              |
| 🎮 Test & Beceri Eşleşmesi | Oyun – Veri eşleşme tablosu hazırlanması                  | Hangi oyun (Stroop, n-back...) hangi veri seti ile eşleşiyor ve hangi beceriyi ölçüyor? Tablo halinde döküm.       | AI Geliştirme Ekibi       |10              |
| 🎮 Test & Beceri Eşleşmesi | Oyunlardan hangi metrikler toplanacak?                    | Süre, doğruluk, hatalı cevap sayısı gibi hangi metriklerin kaydedileceği netleştirilecek.                          | AI Geliştirme Ekibi       |10              |

## --- SPRINT 2 - Skor İşleme, Sınıflandırma & Öneri Sistemi Taslağı ---
*7 Temmuz - 20 Temmuz* <br>
<br>
**Sprint Amacı:**
- Veri setlerinden kullanıcı skorlarını sınıflandırmak
- Öneri motorunun temel kurgusunu oluşturmak
- Skor verisi üzerinden temel backend-akışları kurmak
- Sprint 1'den kalan eksiklerin tamamlanması
- Pasif ekip üyeleriyle yolların ayrılması <br><br>

**Sprint içinde tamamlanması tahmin edilen puan:** 120 Puan<br> <br>
**Puan Tamamlama Mantığı:** Bu sprint için proje başında 120 puan belirlemiş olsak da pasif ekip üyeleri sebebiyle ilk sprintteki eksikleri bu bölüme aktarıp revize yoluna gittik.Tahmin edilen puan 140 olarak güncellendi.   <br> <br>
**Backlog düzeni ve Story seçimleri:** Bu bölümde Backlog'umuz görevlerin zaman aralıklarında ekip üyelerine aktarılıp devam etmesi üzerine hiyerarşik şekilde ilerlemesi planlanmıştır. Aynıu şekilde 2 farklı ekip ile ilerlemeyi planlamaktayız. <br> 
**Veri Bilimi Ekibi:** Ramazan, Hamza, Miray <br> 
**AI Geliştirme Ekibi:** Sara, Tuğba <br> <br> 

**🧩 Genel Sprint Tablosu : CognitiveTrack – Sprint 2**
| **List** (Kategori)        | **Card (Görev)**                                          | **Açıklama / Alt Görevler**                                                                                        | **Sorumlu**               |**Puan**                 
| -------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------- |----------------|
| 📦 Veri Hazırlığı            | Skor verilerinin normalize edilmesi                     | Tüm test skorları ortak forma getirilir (z-score, min-max vb.)                                                     | Veri Bilimi Ekibi                  |10   |
| 📦 Veri Hazırlığı            | Eksik ve anomali değerlerin temizlenmesi              | Outlier analizleri yapılır, eksik veri stratejisi belirlenir (drop/impute)                                           | Veri Bilimi Ekibi                  |10 |
| 🧠 Beceri Sınıflandırma       | N-back testine göre çalışma belleği düzeyi sınıflandırması (düşük/orta/yüksek)   | Tüm veri setlerin final versiyonu ai ekibi ile paylaşılacak.                                            | Veri Bilimi Ekibi   |20|
| 🧠 Beceri Sınıflandırma        | Tepki süresi + hata oranı ile dikkat düzeyi analizi  | Reaction Time veri seti ile kullanıcı tipi segmentasyonu (dikkatli, hızlı, hatalı...)                            | Veri Bilimi Ekibi                       |10|
| 🎮 Test & Beceri Eşleşmesi      | Oyun – Veri eşleşme tablosu hazırlanması  | Hangi oyun (Stroop, n-back...) hangi veri seti ile eşleşiyor ve hangi beceriyi ölçüyor? Tablo halinde döküm.                 | Veri Bilimi Ekibi                   |25 |
| 🎮 Test & Beceri Eşleşmesi     | Oyunlardan hangi metrikler toplanacak?              | Doğruluk, n\_level analizi, dağılım                                                                                | AI Geliştirme Ekibii         |25            |
| 🔧 Backend         | Skor verisini kaydeden API (JSON POST)                          | Test sonrası kullanıcıdan gelen skorları backend’e yazan endpoint yapılır                                            | AI Geliştirme Ekibi        |10            |
| 🔧 Backend         | Kullanıcı sınıfını dönen API (ör: "çalışma belleği: orta")      | Model sonuçlarını front-end’e dönen örnek servis kurulur                                                            | AI Geliştirme Ekibi         |10            |
| 🧠 Öneri Motoru Tasarımı | Beceri sınıfına göre öneri eşleştirmeleri tanımlanır      | "Bellek düşükse → N-back öner", "Dikkat düşükse → Stroop ver", gibi kural bazlı ilk öneri seti hazırlanır           | AI Geliştirme Ekibi       |10              |
| 🧠 Öneri Motoru Tasarımı | Öneri motoru için temel JSON yapısı tasarımı              | Frontend’in okuyabileceği formatta öneri verileri nasıl dönecek belirlenir (örnek: oyun adı, zorluk, tekrar sayısı...)| AI Geliştirme Ekibi       |10            |

**Sprint Review:**
