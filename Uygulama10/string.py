#a = 'a'
#abc = "abc"
#a2 = "a"
#abc = 'abcd'
#soz = 'Demiş ki: "asd"'
#print(soz + " " + abc)
#print(abc*5)
#
#cumle = "Bir müsellesin mesaai sathiyesi kaidesi #ile irtifainin hasılı darpının nısfına müsavidir."
#
#print(len(cumle.split(" ")))
#print(cumle.replace("i","e"))
#liste = ["1","2","3","4","5","6","7","8","9","10"]
#cikti = ""
#for eleman in liste:
#    cikti += eleman+"-"
#print(cikti.strip("-"))
#print("-".join(liste))
#print("deneme\nyanilma\tdevam")
#print("C:\\Users\\emiro\\Desktop")
#print(r"C:\Users\emiro\Desktop")
#deneme = "x"
#print(f"{deneme} değerinin sonucu")
#

sesliler = ["a","e","i","ı","o","ö","u","ü"]
cumle = "Bir müsellesin mesaai sathiyesi kaidesi ile irtifainin hasılı darpının nısfına müsavidir."

sayi = 0
for eleman in cumle:
    if eleman in sesliler:
        sayi += 1
print(sayi)