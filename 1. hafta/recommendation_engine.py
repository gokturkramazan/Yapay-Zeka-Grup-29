
import pandas as pd

kullanicilar = [
    {"user_id": 101, "accuracy": 0.43, "reaction_time": 0.9, "moral_status": "orta", "academic_level": "orta", "memory_level": "düşük"},
    {"user_id": 102, "accuracy": 0.92, "reaction_time": 1.4, "moral_status": "yüksek", "academic_level": "yüksek", "memory_level": "orta"},
    {"user_id": 103, "accuracy": 0.86, "reaction_time": 0.8, "moral_status": "düşük", "academic_level": "orta", "memory_level": "orta"},
    {"user_id": 104, "accuracy": 0.79, "reaction_time": 0.7, "moral_status": "orta", "academic_level": "düşük", "memory_level": "yüksek"},
    {"user_id": 105, "accuracy": 0.85, "reaction_time": 0.6, "moral_status": "orta", "academic_level": "orta", "memory_level": "orta"}
]

def öneri_yap(kullanici):
    if kullanici["accuracy"] < 0.5:
        return "Kolay dikkat oyunu"
    elif kullanici["reaction_time"] > 1.2:
        return "Refleks hızlandırıcı oyun"
    elif kullanici["moral_status"] == "düşük":
        return "Motivasyon artırıcı oyun"
    elif kullanici["academic_level"] == "düşük":
        return "Temel beceri egzersizi"
    elif kullanici["memory_level"] == "düşük":
        return "Çalışma belleği artırıcı oyun"
    else:
        return "Gelişmiş 2-Back oyunu"

for k in kullanicilar:
    k["onerilen_egzersiz"] = öneri_yap(k)

df = pd.DataFrame(kullanicilar)
df.to_csv("oneriler.csv", index=False)
print(df)
