import os
os.system("cls")


# 1.m

# class Mahsulot:
#     def __init__(self,n,s,m):
#         self.nom = n
#         self.narx = s
#         self.miqdor = m
#     def sotib_ol(self,miqdor):
#         self.miqdor = self.miqdor - miqdor
#         print("Do'knda hamsulot sotildi!")
    
#     def qolgan_miqdor(self):
#         return self.miqdor
#     def show_info(self):
#         print(f"{self.nom} {self.narx} {self.miqdor}")
    
# d = Mahsulot("Olma",5000,30)
# d.show_info()
# d.sotib_ol(5)
# d.sotib_ol(15)
# d.show_info()
# print(d.qolgan_miqdor())
        


# 2.m

# class Kitob:
#     def __init__(self,n,m,s):
#         self.nomi = n
#         self.muallif = m
#         self.sahifa_soni = s

#     def qisqacha(self):
#         print(f"{self.nomi}-Kitob nomi, {self.muallif} - kitob yozgan shaxs")

#     def katta_kitobmi(self):
#         if self.sahifa_soni >=300:
#             return True
#         else:
#             return False
#     def show_info(self):
#         print(f"{self.nomi} {self.muallif} {self.sahifa_soni}")
    

# a = Kitob("Harry Potter", "J.K. Rowling", 500)
# a.show_info()
# a.qisqacha()
# print(a.katta_kitobmi())


        
# 3.m

# class Avtomobil:
#     def __init__(self,m,y,t):
#         self.model = m
#         self.yil = y
#         self.tezlik = t

#     def tezlashtir(self,tez):
#         self.tezlik +=tez
    
#     def sekinlashtir(self,tez):
#         self.tezlik -=tez
    
#     def show_info(self):
#         print(f"{self.model} {self.yil} {self.tezlik}")

# a = Avtomobil("Cls 63 amg", 2026,350)
# a.tezlashtir(10)
# a.tezlashtir(10)
# a.tezlashtir(30)
# a.show_info()
# a.sekinlashtir(40)
# a.show_info()
        


# 4.m

# class Bank:
#     def __init__(self,i,b):
#         self.ism = i
#         self.balans = b
    
#     def deposit(self,narx):
#         self.balans+=narx
    
#     def yechib_ol(self,narx):
#         if self.balans-narx >=0:
#             self.balans -=narx
#         else:
#             print("Balans yetarli emas")
    
#     def hisobla(self):
#         return self.balans

# a = Bank("Doston",0)
# a.deposit(1000)
# a.yechib_ol(400)
# print(a.hisobla())



# 5.m

# import math
# class Uchburchak:
#     def __init__(self,a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def preimetr(self):
#         natija = self.a + self.b + self.c
#         return natija
#     def maydon(self):
#         p = (self.a + self.b + self.c)/2
#         s = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))
#         return s
    
# u = Uchburchak(3,4,5)
# print(u.preimetr())
# print(u.maydon())


# 6.m

# class Kurs:
#     def __init__(self,n,d):
#         self.nomi = n
#         self.davomiylik = d
#         self.talabalar = []

#     def talaba_qoshish(self,ism):
#         self.talabalar.append(ism)
    
#     def talabalar_soni(self):
#         return len(self.talabalar)
    
# k = Kurs("Najot ta'lim","5-oy")
# k.talaba_qoshish("Ali")
# k.talaba_qoshish("Vali")
# k.talaba_qoshish("doston")
# print(k.talabalar_soni())


# 7.m

# class Kitob:
#     def __init__(self,n,m):
#         self.nomi = n
#         self.muallif = m
    
# class Kutubxona:
#     def __init__(self):
#         self.kitoblar = []

#     def kitob_qoshish(self,kitob):
#         self.kitoblar.append(kitob)

#     def qidirish(self,nom):
#         for kitob in self.kitoblar:
#             if kitob.nomi == nom:
#                 return f"Topildi: {kitob.nomi} - {kitob.muallif}"
#         return "Kitob topilmadi"
    
# k1 = Kitob("Matematika","Karimov")
# k2 = Kitob("Fizika", "Rahimov")

# kutubxona = Kutubxona()
# kutubxona.kitob_qoshish(k1)
# kutubxona.kitob_qoshish(k2)

# print(kutubxona.qidirish("Matematika"))


        
        
        