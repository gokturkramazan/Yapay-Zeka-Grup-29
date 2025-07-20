
def zorluk_sec(accuracy, moral_status, academic_level, memory_level):
    """
    Kullanıcının başarı düzeyi, moral durumu, akademik seviyesi ve hafıza kapasitesine
    göre adaptif zorluk seviyesini belirler.

    Girdi:
        - accuracy: float (0.0 - 1.0 arası kullanıcı başarımı)
        - moral_status: str ("düşük", "orta", "yüksek")
        - academic_level: str ("düşük", "orta", "yüksek")
        - memory_level: str ("düşük", "orta", "yüksek")

    Çıktı:
        - str: "easy", "medium", ya da "hard"
    """

    # Başlangıç zorluk puanı
    zorluk_puani = 0

    # Accuracy değerlendirmesi
    if accuracy < 0.5:
        zorluk_puani += 0  # çok düşük başarı → kolay seviye
    elif accuracy < 0.75:
        zorluk_puani += 1  # orta başarı → orta seviye
    else:
        zorluk_puani += 2  # yüksek başarı → zor seviye

    # Moral durumu değerlendirmesi
    if moral_status == "düşük":
        zorluk_puani += 0  # moral düşükse oyuncuyu zorlamamalı
    elif moral_status == "orta":
        zorluk_puani += 1
    else:
        zorluk_puani += 2

    # Akademik seviye
    if academic_level == "düşük":
        zorluk_puani += 0
    elif academic_level == "orta":
        zorluk_puani += 1
    else:
        zorluk_puani += 2

    # Hafıza seviyesi
    if memory_level == "düşük":
        zorluk_puani += 0
    elif memory_level == "orta":
        zorluk_puani += 1
    else:
        zorluk_puani += 2

    # Toplam puana göre zorluk seviyesini belirle
    if zorluk_puani <= 3:
        return "easy"
    elif zorluk_puani <= 6:
        return "medium"
    else:
        return "hard"
