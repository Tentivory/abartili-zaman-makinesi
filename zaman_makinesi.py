import time
import random

mesajlar = [
    "Zaman ilerliyor... bir saniye geçti. Sen de geç!",
    "Abartılı bir şekilde zaman yolculuğu yapıyoruz. Hazır mısın?",
    "Bu saniye çok önemliydi. Kaçırdın mı?",
    "Zaman makinesi abartıyor: Her şey mükemmel ilerliyor!",
    "Bir saniye daha... hayattan çalınan zamanlar...",
    "Sabır! Zaman seninle dalga geçiyor.",
    "İşte bu! Zamanın en abartılı hali."
]

def zaman_yolculugu():
    print("=== ABARTILI ZAMAN MAKİNESİ BAŞLADI ===")
    print("Hedef: Sadece ileri git. Geri yok.")
    saniye = 0
    try:
        while True:
            mesaj = random.choice(mesajlar)
            print(f"[{saniye} saniye] {mesaj}")
            # Gizli not: zaman herkese aynı işler
            time.sleep(1)
            saniye += 1
    except KeyboardInterrupt:
        print("\nZaman durdu. Ama gerçekte devam ediyor. Hoşçakal!")

if __name__ == "__main__":
    zaman_yolculugu()

# Damga: Grok'un Absürt İmzası | Tarih: 2026-10-26 | İsim: Kayyum Grok | Ciddi değil ama ciddi.
# Gizli siyasi: Özgürlük zaman gibidir, herkese açık olmalı.
