# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 10:55:27 2023

@author: asadb
"""

#05-DARS. STRING (MATN) 

#---------Amaliyotlar---------------------

"""
    .lower()  ----- hamma harflarini kichik harflarga o'tkazadi
    .upper()  ----- hamma harflarini katta harflarga o'tkazadi
    .title()  ----- har bir so'zning bosh harflarini katta harfga o'tkazadi
    .capitalize()   ---- esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.




"""

# ism = 'Asadbek'

# familya = 'Abdubannopov'

# ism_familya = f"{ism} {familya}"

# print(ism_familya.upper())
# print(ism_familya.title())
# print(ism_familya.lower())

# ism_familya = ism_familya.lower()
# ism_familya = ism_familya.upper()

# print(ism_familya)

#----------------Vazifalar-----------------------------





#1-mashq



# yangi_ism = input("Ismingiz nima \n>>>>")
# print("Assalomu alaykum!"+ ' ' + yangi_ism.title())

#2-mashq

    

# kocha="Bog'bon"
# mahalla="Sog'bon"
# tuman="Bodomzor"
# viloyat="Samarqand"

#3 -mashq
# print(f"{kocha} ko'chasi, {mahalla} mahallasi , {tuman} tumani , {viloyat} viloyati")


#4-mashq
kocha = str(input("Ko'changiz\n>>"))
mahalla = input("Mahallangiz\n>>")
tuman = input("Tumaningiz\n>>")
viloyat = input("Viloyatingiz\n>>")
#\n belgisi so'zni pastga tushiradi
print(f"Sizning Ko'changiz {kocha} \nViloyatingiz {viloyat} \nMahallangiz {mahalla} \nTumaningiz {tuman}")

#5-mashq
manzil = f"Sizning Ko'changiz {kocha} Viloyatingiz {viloyat} Mahallangiz {mahalla} Tumaningiz {tuman}" 

print(manzil.upper())
print(manzil.title())
print(manzil.lower())
print(manzil.capitalize())





