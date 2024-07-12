import random
liste_tshirt = ["animeli t-shirt","turuncu t-shirt","yine beyaz t-shirt","2. animeli t-shirt","yeşil gömlekli kombin"]
print(random.choice(liste_tshirt))
liste_pant= ["siyh paraşüt","yeşil paraşüt","mavi kot","siyah kot","nike eşofman","adidas eşofman"]
print(random.choice(liste_pant))

while True:
    kullanici=input("Başlayalım o halde; taş mı, kağıt mı, makas mı?").lower()

    bot = ['taş','kağıt','makas']
    bot = random.choices(bot)
    if kullanici == bot:
        print("EŞİTTTT!!!")
    elif (kullanici == 'taş' and bot == 'makas')or \
         (kullanici == 'kağıt' and bot == 'taş')or \
         (kullanici == 'makas' and bot == 'kağıt'):
        print("bilgisayar:",bot,"'ı seçti.Sen kazandın mutlu musun...")
    else:
        print("bilgisayar:",bot,"'ı seçti.Sen kaybettin.Başka zamana.")
