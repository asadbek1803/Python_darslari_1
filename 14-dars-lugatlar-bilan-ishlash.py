# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 23:06:15 2023

@author: asadbek
"""

#--------------------------MAVZU: LUG'ATLAR BILAN ISHLASH ----------------------------


talaba_0 = {'ism':'', 'familya':'', 'yosh': 18}

talaba_0 ['ism'] = 'Akmal'
talaba_0 ['familya'] = 'Shokirov'
talaba_0 ['kurs'] = 1

del talaba_0['kurs']
talaba_0 ['kurs'] = 4

en_uz ={'apple': 'olma',
        'hello': 'salom',
        'book': 'kitob',
        'school':'maktab',
        'library': 'kutubxona'}

# lugat_uz = en_uz.get(input(' '))
# print(lugat_uz.title())





otam = {'ismi':'Alisher',
        't_yil': 1982,
        't_joy':'Farg\'ona'}

onam = {'ismi':'Manzuraxon',
        't_yil':1986,
        't_joy':"Farg'ona"}


ukam = {'ismi':'Durdona',
        't_yil':2010,
        't_joy':"Farg'ona"}


print(f"Dadamning ismi", otam['ismi'], otam['t_yil'], '-yilda' , otam['t_joy'],"da tavallud topgan")
print(f"Onamnning ismi", onam['ismi'], onam['t_yil'], '-yilda' , onam['t_joy'],"da tavallud topgan")
print(f"Ukamning ismi", ukam['ismi'], ukam['t_yil'], '-yilda' , ukam['t_joy'],"da tavallud topgan")




s_ovqat = {'durdona':'sho\'rva',
           'manzuraxon':'salat',
           'alisher':'osh',
           'usmon':'somsa'}

print("Durdonaning sevimli ovqati", s_ovqat['durdona'])
print("Alisherning sevimli ovqati", s_ovqat['alisher'])
print("Usmonning sevimli ovqati",s_ovqat['usmon'])







py_dict = {'String':'Matn',
           'Float': 'O\'nlik son',
           'else':'aks holda',
           'if':'agar'}




kalit = input("So'zni kiriting\n>>").lower()
print(py_dict.get(kalit,"Bunday so'z mavjud emas"))


if py_dict==None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {py_dict} deb tarjima qilinadi")






