import joblib

dosya = joblib.load("suggestion_model.pkl")
model = dosya["model"]
le_moral = dosya["le_moral"]
le_academic = dosya["le_academic"]
le_memory = dosya["le_memory"]

accuracy = 0.52
reaction_time = 1.3
academic_level = "orta"
memory_level = "düşük"
moral_status = "yüksek"

encoded_input = [
    accuracy,
    reaction_time,
    le_academic.transform([academic_level])[0],
    le_memory.transform([memory_level])[0],
    le_moral.transform([moral_status])[0]
]

tahmin = model.predict([encoded_input])[0]
print("Önerilen görev:", tahmin)
