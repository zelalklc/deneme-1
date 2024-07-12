import random
liste_tshirt = ["animeli t-shirt","turuncu t-shirt","yine beyaz t-shirt","2. animeli t-shirt","yeşil gömlekli kombin"]
print(random.choice(liste_tshirt))
liste_pant= ["siyh paraşüt","yeşil paraşüt","mavi kot","siyah kot","nike eşofman","adidas eşofman"]
print(random.choice(liste_pant))



try:
    while True:
        def sayiUret(baslangic, bitis):
            return random.sample(range(baslangic, bitis), 1)


        def randomNumber(girdi):
            liste = []

            ba, bi, k = map(int, girdi.split(" "))
            print("1. baski", ba, bi, k)
            start = 0
            while start < k:
                sayi = sayiUret(ba, bi)
                liste.append(sayi)
                start = start + 1
            return liste
        girdi = input("hangi sayılar arası 10 rastgele sayı istersiniz?")
        bul = randomNumber(girdi)
        print(bul)

except:
    print("HAY AKSİİİ HATAAA")
