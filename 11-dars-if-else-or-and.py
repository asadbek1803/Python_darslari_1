# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 12:13:41 2023

@author: asadbek

"""


# print("Bu dasturga faqat juft son kiriting")

# j_son = int(input("Juft son kiriting\n>>> "))

# if j_son%2:
    
#     print("Bu juft son emas") 

# else:
#        print("Rahmat!")
       

#--------------------Ishlamadi-------------------------XAtO
# print("Muzeyga kirish uchun chipta narxlarini bilib oling")

# age = int(input("Yoshingiz nechida\n>>> "))

# if age <=4 and age >= 60:
#     narx = 0       
# if age <= 18:
#     narx = 10_000
# if age >=18:
#     narx = 20_000
# if age >=60:
#     narx = 0
# print(f"Sizga kirish {narx} so'm")       
       
       
       
# yosh = int(input("Yoshingiz nechida?"))

# if yosh<=4 or yosh>=60:
#     narh = 0;
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000    
# print(f"Chipta {narh} so'm")       




# mahsulotlar = ['non', 'pepsi','fanta','yo\g','go\'sht','piyoz','olma']

# savat = []

# print("Iltimos 5 ta mahsulot kiriting!")
# for s in range(5):
#     savat.append(input(f"{s+1}-mahsulot nomi\n>>"))
# if mahsulotlar:
#     for wh in mahsulotlar:
#         if wh in savat:
#                 print(f"Do'konimizda {wh} bor")
#         else:
#             print(f"Do'konimizda  mahsulotlar yo'q")
    
    
    
    
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))


# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")
    


# users = ['alisher','aziza','yasina','umar']

# login = input("Yangi login tanlang: ")

# if login.lower() in users:
#     print('Login band, yangi login tanlang!')
# else:
#     print(f"Xush kelibsiz, {login.title()}!")    
    
    
    
    
    
son = int(input("Istalgan butun son kiriting: "))

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")    
    
    
    
    
    


