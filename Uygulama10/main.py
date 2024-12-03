"""
import modul
n = 5
r = 3
k = modul.komb(n,r)
p = modul.perm(n,r)
print(k)

from modul import komb,perm

n = 5
r = 3
k = modul.komb(n,r)
p = modul.perm(n,r)
print(k)
"""

"""
Piramidin tabanında kare biçiminde yerleştirilmiş N*N adet, ikinci katında (N-1)*(N-1), üçüncü katında (N-2)*(N-2), ... , N. katında (son kat) 1 taş blok olduğu kabul edilirse, piramitin kaç taş bloktan oluştuğunu ve kaç katlı olduğunu bulan programı yazınız (2.3 milyondan büyük olacak şekilde en az kaç kat olmalıdır).


from modul import kat_hesapla,isci_hesabi
kat_sayisi = kat_hesapla(2_300_000)
print(kat_sayisi)

kac_blok = isci_hesabi(2_300_000)
print(kac_blok)
"""
from modul import rfakt

print(rfakt(0))