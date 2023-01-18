# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 18:04:20 2023

@author: asadbek
"""

# def yosh_hisoblagich(ism,yosh):
#     """Foydalanuvhini ismini so'rab
#         Uning yoshini hisobledigan dastur"""
#     print(f"{ism.title()} {2023-yosh}-yoshda")
# yosh_hisoblagich('asadbek',41) 
   

# def kv_kub(son):
#     """Foydalanuvchidan son so'rab kavadratini
#     Hamda kubini konsolga chiqaruvchi funksiya"""
#     print(f"{son}-ning kvadrati {son**2}")
#     print(f"{son}-ning kubi {son**3}")
    
    
# kv_kub(5)   
# kv_kub(11) 


# def juf_toq(son):
#     """Foydalanuvchidan son so'rab uni
#     juft yoki toqligini biluvchi funksiya"""
    
#     if son%2:
#         print("Toq son")
#     else:
#         print("Juft son")
        
        
        
# juf_toq(5)
# juf_toq(8)
# juf_toq(125)


# def katta_kichik(son1,son2):
#     """Foydalanuvchidan sonla so'rab kattasini konsolga 
#     chiqaruvchi funksiya"""

#     if son1>son2:
#         print(son1)
#     if son1<son2:
#         print(son2)
#     else:
#         print("Sonlar teng")
# katta_kichik(8, 15)
# katta_kichik(14, 7)
# katta_kichik(78,78)        
        




def solishtir(x,y):
    """Ikki sonni solishtiruvchi funksiya"""
    if x>y:
        print(f"{x}>{y}")
    elif x<y:
        print(f"{y}>{x}")
    else:
        print(f"{x}={y}")

solishtir(10,20)
solishtir(-9,12)
solishtir(1223*5,5**4)



def daraja(x,y=2):
    print(f"{x} ning {y}-darajasi {x**y} ga teng")

daraja(5,2)
daraja(3,3)
daraja(94,4)
daraja(6)


def bolinish_alomatlari(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(20)


        