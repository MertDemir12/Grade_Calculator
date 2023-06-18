db = {}  # Edebiyat İçin
liste1 = {}  # Matematik İçin
liste2 = {}  # Fizik İçin
liste3 = {}  # Biyoloji İçin
liste4 = {}  # Kimya İçin
liste5 = {}  # Tarih İçin
liste6 = {}  # Coğrafya İçin
liste7 = {}  # Felsefe İçin
liste8 = {}  # İngilizce İçin
liste9 = {}  # Almanca İçin
print("***********************************************************")
print("Karne Hesaplama")
print("***********************************************************")
h = input("İsmin Ve Soyismin: ")
k = int(input("Kaçıncı Sınıfa Gidiyorsun: "))
while(True):
    print("Notları Görmek İçin [N] Yada [n] Yaz!")
    print("Yazılı Notu Eklemek İçin [YE] Yada [ye] Yaz!")
    print("Sözlü Notu Eklemek İçin [SE] Yada [se] Yaz!")
    print("Ortalama Hesaplamak İçin [O] Yada [o] Yaz!")
    print("Çıkmak İçin [Q] Yada [q] Yaz!")
    a = input()
    if(a == "N" or a == "n" and k == 9):
        print("Edebiyat: {}\nMatematik: {}\nFizik: {}\nBiyoloji: {}\nKimya: {}\nTarih: {}\nCoğrafya: {}\nİngilizce: {}\nAlmanca: {}\n".format(db,liste1,liste2,liste3,liste4,liste5,liste6,liste8,liste9))  # Girilen Notları Göstermek İçin
    elif(a == "N" or a == "n" and k == 10):
        print("Edebiyat: {}\nMatematik: {}\nFizik: {}\nBiyoloji: {}\nKimya: {}\nTarih: {}\nCoğrafya: {}\nFelsefe: {}\nİngilizce: {}\nAlmanca: {}\n".format(db,liste1,liste2,liste3,liste4,liste5,liste6,liste7,liste8,liste9))  # Girilen Notları Göstermek İçin
    elif(a == "N" or a == "n" and k == 11 or k == 12):
        print("Edebiyat: {}\nMatematik: {}\nFizik: {}\nBiyoloji: {}\nKimya: {}\nTarih: {}\nFelsefe: {}\nİngilizce: {}\nAlmanca: {}\n".format(db,liste1,liste2,liste3,liste4,liste5,liste7,liste8,liste9))  # Girilen Notları Göstermek İçin
    elif(a == "YE" or a == "ye"):
        while(True):
            print("Hangi Derse Ekleyeceksin?")
            print("Edebiyat İçin [E] Yada [e]Yaz!")
            print("Matematik İçin [M] Yada [m] Yaz!")
            print("Fizik İçin [F] Yada [f] Yaz!")
            print("Biyoloji İçin [B] Yada [b] Yaz!")
            print("Tarih İçin [T] Yada [t] Yaz!")
            if(k == 9 or k == 10):
                print("Coğrafya İçin [C] Yada [c] Yaz!")
            if(k == 10 or k == 11 or k == 12):
                print("Felsefe İçin [FE] Yada [fe] Yaz!")
            print("İngilizce İçin [İ] Yada [i] Yaz!")
            print("Almanca İçin [A] Yada [a] Yaz!")
            print("Geriye Gitmek İçin [G] Yada [g] Yaz!")
            b = input()
            if(b == "E" or b == "e"):  # Edebiyat Notları Girmek İçin
                print("1.Yazılı İse [1] Yaz!\n2.Yazılı İse [2] Yaz!\n")
                c = input()
                if(c == "1"):
                    x = int(input("Kaç Aldın: "))
                    db["1.Yazılı"] = x
                elif(c == "2"):
                    y = int(input("Kaç Aldın: "))
                    db["2.Yazılı"] = y
            elif(b == "M" or b == "m"):  # Matematik Notları Girmek İçin
                print("1.Yazılı İse [1] Yaz!\n2.Yazılı İse [2] Yaz!\n")
                c = input()
                if(c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste1["1.Yazılı"] = x
                elif(c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste1["2.Yazılı"] = y
            elif(b == "F" or b == "f"):  # Fizik Notları Girmek İçin
                print("1.Yazılı İse [1] Yaz!\n2.Yazılı İse [2] Yaz!\n")
                c = input()
                if(c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste2["1.Yazılı"] = x
                elif(c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste2["2.Yazılı"] = y
            elif(b == "B" or b == "b"):  # Biyoloji Notları Girmek İçin
                print("1.Yazılı İse [1] Yaz!\n2.Yazılı İse [2] Yaz!\n")
                c = input()
                if(c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste3["1.Yazılı"] = x
                elif(c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste3["2.Yazılı"] = y
            elif(b == "K" or b == "k"):  # Kimya Notları Girmek İçin
                print("1.Yazılı İse [1] Yaz!\n2.Yazılı İse [2] Yaz!\n")
                c = input()
                if(c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste4["1.Yazılı"] = x
                elif(c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste4["2.Yazılı"] = y
            elif(b == "T" or b == "t"):  # Tarih Notları Girmek İçin
                print("1.Yazılı İse [1] Yaz!\n2.Yazılı İse [2] Yaz!\n")
                c = input()
                if(c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste5["1.Yazılı"] = x
                elif(c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste5["2.Yazılı"] = y
            elif(b == "C" or b == "c"):  # Coğrafya Notları Girmek İçin
                print("1.Yazılı İse [1] Yaz!\n2.Yazılı İse [2] Yaz!\n")
                c = input()
                if(c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste6["1.Yazılı"] = x
                elif(c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste6["2.Yazılı"] = y
            elif(b == "FE" or b == "fe"):  # Felsefe Notları Girmek İçin
                print("1.Yazılı İse [1] Yaz!\n2.Yazılı İse [2] Yaz!\n")
                c = input()
                if(c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste7["1.Yazılı"] = x
                elif(c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste7["2.Yazılı"] = y
            elif(b == "İ" or b == "i"):  # İngilizce Notları Girmek İçin
                print("1.Yazılı İse [1] Yaz!\n2.Yazılı İse [2] Yaz!\n")
                c = input()
                if(c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste8["1.Yazılı"] = x
                elif(c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste8["2.Yazılı"] = y
            elif(b == "A" or b == "a"):  # Almanca Notları Girmek İçin
                print("1.Yazılı İse [1] Yaz!\n2.Yazılı İse [2] Yaz!\n")
                c = input()
                if(c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste9["1.Yazılı"] = x
                elif(c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste9["2.Yazılı"] = y
            elif(b == "G" or b == "g"):  # Geri Gitmek İçin
                break
    elif (a == "SE" or a == "se"):
        while(True):
            print("Hangi Derse Ekleyeceksin?")
            print("Edebiyat İçin [E] Yada [e]Yaz!")
            print("Matematik İçin [M] Yada [m] Yaz!")
            print("Fizik İçin [F] Yada [f] Yaz!")
            print("Biyoloji İçin [B] Yada [b] Yaz!")
            print("Tarih İçin [T] Yada [t] Yaz!")
            if (k == 9 or k == 10):
                print("Coğrafya İçin [C] Yada [c] Yaz!")
            if (k == 10 or k == 11 or k == 12):
                print("Felsefe İçin [FE] Yada [fe] Yaz!")
            print("İngilizce İçin [İ] Yada [i] Yaz!")
            print("Almanca İçin [A] Yada [a] Yaz!")
            print("Geriye Gitmek İçin [G] Yada [g] Yaz!")
            b = input()
            if (b == "E" or b == "e"):  # Edebiyat Sözlü Notları Girmek İçin
                print("1.Sözlü İse [1] Yaz!\n2.Sözlü İse [2] Yaz!\n")
                c = input()
                if (c == "1"):
                    x = int(input("Kaç Aldın: "))
                    db["1.Sözlü"] = x
                elif (c == "2"):
                    y = int(input("Kaç Aldın: "))
                    db["2.Sözlü"] = y
            elif (b == "M" or b == "m"):  # Matematik Sözlü Notları Girmek İçin
                print("1.Sözlü İse [1] Yaz!\n2.Sözlü İse [2] Yaz!\n")
                c = input()
                if (c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste1["1.Sözlü"] = x
                elif (c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste1["2.Sözlü"] = y
            elif (b == "F" or b == "f"):  # Fizik Sözlü Notları Girmek İçin
                print("1.Sözlü İse [1] Yaz!\n2.Sözlü İse [2] Yaz!\n")
                c = input()
                if (c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste2["1.Sözlü"] = x
                elif (c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste2["2.Sözlü"] = y
            elif (b == "B" or b == "b"):  # Biyoloji Sözlü Notları Girmek İçin
                print("1.Sözlü İse [1] Yaz!\n2.Sözlü İse [2] Yaz!\n")
                c = input()
                if (c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste3["1.Sözlü"] = x
                elif (c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste3["2.Sözlü"] = y
            elif (b == "K" or b == "k"):  # Kimya Sözlü Notları Girmek İçin
                print("1.Sözlü İse [1] Yaz!\n2.Sözlü İse [2] Yaz!\n")
                c = input()
                if (c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste4["1.Sözlü"] = x
                elif (c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste4["2.Sözlü"] = y
            elif (b == "T" or b == "t"):  # Tarih Sözlü Notları Girmek İçin
                print("1.Sözlü İse [1] Yaz!\n2.Sözlü İse [2] Yaz!\n")
                c = input()
                if (c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste5["1.Sözlü"] = x
                elif (c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste5["2.Sözlü"] = y
            elif (b == "C" or b == "c"):  # Coğrafya Sözlü Notları Girmek İçin
                print("1.Sözlü İse [1] Yaz!\n2.Sözlü İse [2] Yaz!\n")
                c = input()
                if (c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste6["1.Sözlü"] = x
                elif (c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste6["2.Sözlü"] = y
            elif (b == "FE" or b == "fe"):  # Felsefe Sözlü Notları Girmek İçin
                print("1.Sözlü İse [1] Yaz!\n2.Sözlü İse [2] Yaz!\n")
                c = input()
                if (c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste7["1.Sözlü"] = x
                elif (c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste7["2.Sözlü"] = y
            elif (b == "İ" or b == "i"):  # İngilizce Sözlü Notları Girmek İçin
                print("1.Sözlü İse [1] Yaz!\n2.Sözlü İse [2] Yaz!\n")
                c = input()
                if (c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste8["1.Sözlü"] = x
                elif (c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste8["2.Sözlü"] = y
            elif (b == "A" or b == "a"):  # Almanca Sözlü Notları Girmek İçin
                print("1.Sözlü İse [1] Yaz!\n2.Sözlü İse [2] Yaz!\n")
                c = input()
                if (c == "1"):
                    x = int(input("Kaç Aldın: "))
                    liste9["1.Sözlü"] = x
                elif (c == "2"):
                    y = int(input("Kaç Aldın: "))
                    liste9["2.Sözlü"] = y
            elif (b == "G" or b == "g"):  # Geri Gitmek İçin
                break
    elif(a == "O" or a == "o" and k == 9):  # Not Ortalamasını Hesaplamak İçin
        edebi =  (int(db["1.Yazılı"]) + int(db["2.Yazılı"]) + int(db["1.Sözlü"]) + int(db["2.Sözlü"])) / 4  # Edebiyat İçin
        mat = (int(liste1["1.Yazılı"]) + int(liste1["2.Yazılı"]) + int(liste1["1.Sözlü"]) + int(liste1["2.Sözlü"])) / 4  # Matematik İçin
        fizi = (int(liste2["1.Yazılı"]) + int(liste2["2.Yazılı"]) + int(liste2["1.Sözlü"]) + int(liste2["2.Sözlü"])) / 4  # Fizik İçin
        biyo = (int(liste3["1.Yazılı"]) + int(liste3["2.Yazılı"]) + int(liste3["1.Sözlü"]) + int(liste3["2.Sözlü"])) / 4  # Biyoloji İçin
        kim = (int(liste4["1.Yazılı"]) + int(liste4["2.Yazılı"]) + int(liste4["1.Sözlü"]) + int(liste4["2.Sözlü"])) / 4  # Kimya İçin
        tar = (int(liste5["1.Yazılı"]) + int(liste5["2.Yazılı"]) + int(liste5["1.Sözlü"]) + int(liste5["2.Sözlü"])) / 4  # Tarih İçin
        cog = (int(liste6["1.Yazılı"]) + int(liste6["2.Yazılı"]) + int(liste6["1.Sözlü"]) + int(liste6["2.Sözlü"])) / 4  # Coğrafya İçin
        ing = (int(liste8["1.Yazılı"]) + int(liste8["2.Yazılı"]) + int(liste8["1.Sözlü"]) + int(liste8["2.Sözlü"])) / 4  # İngilizce İçin
        alm = (int(liste9["1.Yazılı"]) + int(liste9["2.Yazılı"]) + int(liste9["1.Sözlü"]) + int(liste9["2.Sözlü"])) / 4  # Almanca İçin
        genel = (edebi + mat + fizi + biyo + kim + tar + cog + ing + alm) / 9  # Genel Ortalama İçin
        print("Ortalaman:")
        print("Edebiyat: {}. Edebiyat Ortalaman: {}".format(db,edebi))
        print("Matematik: {}. Matematik Ortalaman: {}".format(liste1,mat))
        print("Fizik: {}. Fizik Ortalaman: {}".format(liste2,fizi))
        print("Biyoloji: {}. Biyoloji Ortalaman: {}".format(liste3,biyo))
        print("Kimya: {}. Kimya Ortalaman: {}".format(liste4,kim))
        print("Tarih: {}. Tarih Ortalaman: {}".format(liste5,tar))
        print("Coğrafya: {}. Coğrafya Ortalaman: {}".format(liste6,cog))
        print("İngilizce: {}. İngilizce Ortalaman: {}".format(liste8,ing))
        print("Almanca: {}. Almanca Ortalaman: {}".format(liste9,alm))
        print("Genel Ortalaman: {}".format(genel))
    elif(a == "O" or a == "o" and k == 10):
        edebi = (int(db["1.Yazılı"]) + int(db["2.Yazılı"]) + int(db["1.Sözlü"]) + int(db["2.Sözlü"])) / 4  # Edebiyat İçin
        mat = (int(liste1["1.Yazılı"]) + int(liste1["2.Yazılı"]) + int(liste1["1.Sözlü"]) + int(liste1["2.Sözlü"])) / 4  # Matematik İçin
        fizi = (int(liste2["1.Yazılı"]) + int(liste2["2.Yazılı"]) + int(liste2["1.Sözlü"]) + int(liste2["2.Sözlü"])) / 4  # Fizik İçin
        biyo = (int(liste3["1.Yazılı"]) + int(liste3["2.Yazılı"]) + int(liste3["1.Sözlü"]) + int(liste3["2.Sözlü"])) / 4  # Biyoloji İçin
        kim = (int(liste4["1.Yazılı"]) + int(liste4["2.Yazılı"]) + int(liste4["1.Sözlü"]) + int(liste4["2.Sözlü"])) / 4  # Kimya İçin
        tar = (int(liste5["1.Yazılı"]) + int(liste5["2.Yazılı"]) + int(liste5["1.Sözlü"]) + int(liste5["2.Sözlü"])) / 4  # Tarih İçin
        cog = (int(liste6["1.Yazılı"]) + int(liste6["2.Yazılı"]) + int(liste6["1.Sözlü"]) + int(liste6["2.Sözlü"])) / 4  # Coğrafya İçin
        fel = (int(liste7["1.Yazılı"]) + int(liste7["2.Yazılı"]) + int(liste7["1.Sözlü"]) + int(liste7["2.Sözlü"])) / 4  # Felsefe İçin
        ing = (int(liste8["1.Yazılı"]) + int(liste8["2.Yazılı"]) + int(liste8["1.Sözlü"]) + int(liste8["2.Sözlü"])) / 4  # İngilizce İçin
        alm = (int(liste9["1.Yazılı"]) + int(liste9["2.Yazılı"]) + int(liste9["1.Sözlü"]) + int(liste9["2.Sözlü"])) / 4  # Almanca İçin
        genel = (edebi + mat + fizi + biyo + kim + tar + cog + fel + ing + alm) / 10  # Genel Ortalama İçin
        print("Ortalaman:")
        print("Edebiyat: {}. Edebiyat Ortalaman: {}".format(db,edebi))
        print("Matematik: {}. Matematik Ortalaman: {}".format(liste1,mat))
        print("Fizik: {}. Fizik Ortalaman: {}".format(liste2,fizi))
        print("Biyoloji: {}. Biyoloji Ortalaman: {}".format(liste3,biyo))
        print("Kimya: {}. Kimya Ortalaman: {}".format(liste4,kim))
        print("Tarih: {}. Tarih Ortalaman: {}".format(liste5,tar))
        print("Coğrafya: {}. Coğrafya Ortalaman: {}".format(liste6,cog))
        print("Felsefe: {}. Felsefe Ortalaman: {}".format(liste7,fel))
        print("İngilizce: {}. İngilizce Ortalaman: {}".format(liste8,ing))
        print("Almanca: {}. Almanca Ortalaman: {}".format(liste9,alm))
        print("Genel Ortalaman: {}".format(genel))
    elif(a == "O" or a == "o" and k == 11 or k == 12):
        edebi = (int(db["1.Yazılı"]) + int(db["2.Yazılı"]) + int(db["1.Sözlü"]) + int(db["2.Sözlü"])) / 4  # Edebiyat İçin
        mat = (int(liste1["1.Yazılı"]) + int(liste1["2.Yazılı"]) + int(liste1["1.Sözlü"]) + int(liste1["2.Sözlü"])) / 4  # Matematik İçin
        fizi = (int(liste2["1.Yazılı"]) + int(liste2["2.Yazılı"]) + int(liste2["1.Sözlü"]) + int(liste2["2.Sözlü"])) / 4  # Fizik İçin
        biyo = (int(liste3["1.Yazılı"]) + int(liste3["2.Yazılı"]) + int(liste3["1.Sözlü"]) + int(liste3["2.Sözlü"])) / 4  # Biyoloji İçin
        kim = (int(liste4["1.Yazılı"]) + int(liste4["2.Yazılı"]) + int(liste4["1.Sözlü"]) + int(liste4["2.Sözlü"])) / 4  # Kimya İçin
        tar = (int(liste5["1.Yazılı"]) + int(liste5["2.Yazılı"]) + int(liste5["1.Sözlü"]) + int(liste5["2.Sözlü"])) / 4  # Tarih İçin
        fel = (int(liste7["1.Yazılı"]) + int(liste7["2.Yazılı"]) + int(liste7["1.Sözlü"]) + int(liste7["2.Sözlü"])) / 4  # Felsefe İçin
        ing = (int(liste8["1.Yazılı"]) + int(liste8["2.Yazılı"]) + int(liste8["1.Sözlü"]) + int(liste8["2.Sözlü"])) / 4  # İngilizce İçin
        alm = (int(liste9["1.Yazılı"]) + int(liste9["2.Yazılı"]) + int(liste9["1.Sözlü"]) + int(liste9["2.Sözlü"])) / 4  # Almanca İçin
        genel = (edebi + mat + fizi + biyo + kim + tar + fel + ing + alm) / 9  # Genel Ortalama İçin
        print("Ortalaman:")
        print("Edebiyat: {}. Edebiyat Ortalaman: {}".format(db, edebi))
        print("Matematik: {}. Matematik Ortalaman: {}".format(liste1, mat))
        print("Fizik: {}. Fizik Ortalaman: {}".format(liste2, fizi))
        print("Biyoloji: {}. Biyoloji Ortalaman: {}".format(liste3, biyo))
        print("Kimya: {}. Kimya Ortalaman: {}".format(liste4, kim))
        print("Tarih: {}. Tarih Ortalaman: {}".format(liste5,tar))
        print("Felsefe: {}. Felsefe Ortalaman: {}".format(liste7,fel))
        print("İngilizce: {}. İngilizce Ortalaman: {}".format(liste8,ing))
        print("Almanca: {}. Almanca Ortalaman: {}".format(liste9,alm))
        print("Genel Ortalaman: {}".format(genel))
    elif(a == "Q" or a == "q"):  # Kodu Durdurmak İçin
        print('Bay Bay!')
        break
    else:
        print("***********************************************************")
        print("Yanlış Kod!")
        print("***********************************************************")