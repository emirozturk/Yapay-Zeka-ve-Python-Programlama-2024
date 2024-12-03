def fakt(sayi):
    carpim = 1
    for i in range(1,sayi+1):
        carpim*=i
    return carpim

def rfakt(sayi):
    if sayi == 0 or sayi == 1:
        return 1
    return rfakt(sayi-1)*sayi

def perm(n,r):
    return fakt(n)/fakt(n-r)

def komb(n,r):
    return perm(n,r)/fakt(r)

def kat_hesapla(tas_sayisi):
    toplam = 0
    kat_sayisi = 0
    while(toplam<tas_sayisi):
        toplam += kat_sayisi**2
        kat_sayisi+=1
    return kat_sayisi

def isci_hesabi(tas_sayisi):
    """
    Piramidin tam 24 yılda bittiğini ve işçilerin günde 10 saat çalıştıklarını düşünelim. İşçilerin bir saatte ortalama kaç blok yerleştirdiklerini bulan SaatBasinaBlok fonksiyonu yazınız (1 yıl = 365 gün + 6 saat kabul edilecek).
    """
    return tas_sayisi/(24*(365.25)*10)