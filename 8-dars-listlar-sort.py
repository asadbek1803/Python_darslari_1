# -*- coding: utf-8 -*-
"""
Created on Thu Jan 12 11:59:58 2023

@author: asadbek
"""


#--------------------#8-DARS-LISTLAR-------------------------------#

# 1- amaliyot
davlatlar = ['Uzbekistan', 'Russia', 'Germany','USA','Brasil']


# 2-amaliyot
print(len(davlatlar))

#3-amaliyot
print(sorted(davlatlar))

#4-amaliyot
print(sorted(davlatlar, reverse=True))

#5- amaliyot
print(davlatlar)
#6-amaliyot
j_sonlar = list(range(120,1202,2))
#7-amaliyot
print(sum(j_sonlar))
#8-amaliyot
print(max(j_sonlar)-min(j_sonlar)) 
#9-amaliyot
print(len(j_sonlar)) 
#10-amaliyot
print(j_sonlar[:20])
print(j_sonlar[-20:])
print(j_sonlar[530:550])

#11-amaliyot
taomlar = ['osh','somsa','chuchvara','mastava','sho\'rva']

nonushta =[]
nonushta = taomlar[:]
#12-amaliyot
nonushta.remove('osh')
nonushta.remove('somsa')
nonushta.append('tort')
nonushta.append('tuxum')
print(f"Kechki taomlar: {taomlar} \nNonushta {nonushta}")
#13-amaliyot
nonushta = tuple(nonushta)
print(type(nonushta))
#14-amaliyot
nonushta[0] = 'qaymoq va non'
# davlatlar.sort() # ro'yxatni alifbo tartibda chiqaradi


# davlatlar.sort(reverse=True) #Teskari tartib

# print(len(davlatlar)) # uzunligini bilish

"""kichik dasturlar"""
# print("Ro'yxatga yoziling!")

# names = []
# familys = []
# ages = []
# numbers = []
# emails = []



# numbers.append(int(input("Telefon raqamingiz\n>>>")))


# names.append(input("Ismingizni kiriting\n>>"))
# if names == numbers:
#     print("Raqamlardan foydalanmang!")
# else:
#     familys.append(input("Familyangizni kiriting\n>>"))
#     if familys == numbers:
#         print("Raqamlardan foydalanmang!")
#     else:
#         ages.append(input("Yoshingiz\n>>>"))
        
#         print("INFO! 18 yoshdan kichiklarga kirish taqiqlanadi ")
        
#         emails.append(input("Elektron pochtangiz\n>>"))
#         print(f"""InFo MaLuMoTnOmA O'zIz hAqIzDa
#                   Ismingiz: {names[0].title()}
#                   Familyangiz: {familys[0].title()}
#                   Yoshingiz: {ages}
#                   Email: {emails}""")                









# sonlar = []
# sonlar = list(range(0,11)) 


# mevalar = []
# mevalar.append('olma')
# mevalar.insert(0,'behi')
# mevalar.append('olcha')
# mevalar.insert(-1,'uzum')


"""kichik dasturlar"""
# # j_sonlar = list(range(0,1200,2))
# print('Ushbu dastur siz yozmoqchi bo\'lgan juft sonlarni chiqaradi' )
# print("Ogohlantirish! Toq son yozmang!")
# son = int(input("Sonni kiriting\n>>>"))


# if son>100:
#     print("Ushbu son belgilangan limitdan oshib ketdi!")
    
# elif son%2:
#     print("Bu juft son emas!")
    
# else:
#     son=list(range(son,100,2))

#     print(son)




"""Kichik dasturlar"""    

# son12 = int(input("Sonni kiriting\n>>>"))

# if son12>100:
#     print("Ushbu son belgilangan limitdan oshib keti")
# elif son12%2:
#     print("Juft son kiritmang") 
# else:
#     son12 = list(range(son12,101,3))    
#     print(son12)
    
    
    
    
"""Kichik dasturlar"""
# new_son = int(input("Juft sonni kiriting\n>>>"))
# if new_son%2:
#    print("Bu juft son emas..")

# else:
#      print("Rahmat!")


# narhlar = [500, 78222, 58111, 8725, 5572]

# arzon = min(narhlar)
# qimmat = max(narhlar)
    
# birga = sum(narhlar)    
# print(f"Eng past narx: {arzon} \nEng qimmat narx: {qimmat} \nJami: {birga}")
    



















