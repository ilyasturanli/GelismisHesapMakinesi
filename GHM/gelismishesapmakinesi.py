import math



print("""
*******************************************************
GELİSMİS HESAP MAKİNESİNE HOSGELDİNİZ....

1-)Ebob
2-)2 sayının bölümünden kalanı bulmak icin
3-)Birinci değerin ikinci değere göre logaritmasını hesaplar
4-)Verilen sayının 2 tabanında logaritmasını hesaplar.
5-)Verilen sayının 10 tabanında logaritmasını hesaplar.
6-)1. sayının 2. sayıya göre kuvvetini alır
7-)Verilen sayının karekökünü hesaplar
8-)Verilen sayıyı radyandan dereceye çevirir.
9-)Verilen sayıyı dereceden radyana çevirir
10-)Radyan cinsinden verilen sayının sinüsünü hesaplar.
*******************************************************
""")
sec = int(input("Seciniz = "))
if(sec == 1 or sec == 2 or sec == 3 or sec == 6):
    sayı1 = int(input("Lütfen 1. sayıyı giriniz = "))
    sayı2 = int(input("Lütfen 2. sayıyı giriniz = "))
    if(sec == 1):
        print(math.gcd(sayı1,sayı2))
    elif(sec == 2):
        print(math.fmod(sayı1,sayı2))
    elif(sec == 3):
        print(math.log(sayı1,sayı2))
    elif(sec == 6):
        print(math.pow(sayı1,sayı2))
elif(sec == 4 or sec == 5 or sec == 7 or sec == 8 or sec == 9 or sec == 10):
    sayı1 = int(input("Lütfen 1. sayıyı giriniz = "))
    if(sec == 4):
        print(math.log2(sayı1))
    elif(sec == 5):
        print(math.log10(sayı1))
    elif(sec == 7):
        print(math.sqrt(sayı1))
    elif(sec == 8):
        print(math.degrees(sayı1))
    elif(sec == 9):
        print(math.radians(sayı1))
    elif(sec == 10):
        print(math.sin(sayı1))
else:
    print("Hatali sayı girdiniz...")




