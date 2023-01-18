# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 16:26:31 2023

@author: asadbek
"""



print("""
      
      
      .....       ......                
      .0000.||||:. 0000.    A A A A A A A A A A A A A
      .0000.     .00000.       A A A A A A A A A
      .0000.     .00000.          A A A A A A
      .0000.     .00000.            A A A A
      .0000.     .00000.              M
      .0000.     .00000.
      .0000.     .00000.    
      .0000.+++++.00000.     @inshaalloh coder: Asadbek Abdubannopov
      .0000.     .00000.
      .0000.     .00000.       
      .0000.     .00000.
      .0000.     .00000.
      
              
      """)



    

                










#---------------#7-dars MAVZU: LIST-------------------


fruits = ['behi','nok','uzum','gilos']
humans = []
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
print("Birinchi meva: ", mevalar[0].title())
print("Ikkinchi meva: ", mevalar[1].upper())
company = ['beeline','uzmobile','uztelecom']



humans.append('Teacher') #.append() methodi bu har doim listni ohirgi qatoriga qo'shadi


humans.insert(-1,'coder') #.insert() methodi bu index bo'yicha siz buyrug'iz bilan


# print(humans)

humans.remove('Teacher')
print(humans)


del company[-1]



bozorlik = ['yog\'', 'go\'sht','un']
mahsulot = bozorlik.pop(2)

print('Men' + mahsulot + 'sotib oldim')

print("Olinmagan mahsulotlar soni: ", bozorlik)

#_-----------------------------Uyga AMALIYOTLAR-------------------
# 1-mashq
ismlar = ['Davron', 'Umidjon', 'Ozodbek']
#2-mashq
print("Salom bugun qaerdasiz",ismlar[0])

print("Bugun qaysi o'yinni o'ynaymiz", ismlar[1])

print("Telefonni qachon almashtiramiz", ismlar[2])
#3-mashq
sonlar = [255,10746,-987,74.5]

print(sonlar[0]+sonlar[1])
print(sonlar[-1]*sonlar[2])

cars = ['buggy', 'gentra','lacetti','captiva']

print(cars.append('malibu'))
cars.append('tico')

del cars[1] # Bu esa elementni index bo'yicha o'chradi

cars.remove('captiva') #bu elementni index bo'yicha o'chrmaydi

cars.insert(1,'malibu 2') #bu elementni qo'shadi index bo'yicha



cars[0] = 'lambarghini' #buggy edi lambarghiniga o'zgardi #elementni o'zgartirish

ismlar.append('Shoxrux') #ismlar ro'yxatiga Shoxruxni qo'shdim

ismlar[-1] = 'Shuxrat'
print(ismlar)

t_shaxslar = ['Imom-al Buxoriy', 'Amir Temur', 'Alisher Navoiy', 'Al-Farg\'oniy']

z_shaxslar =['Bill Geyts', 'Ilon Musk','Pavel Annenkov']

istak = t_shaxslar.pop(0)
istak1 = z_shaxslar.pop(1)
print(f"Men tarixiy shaxslardan " + istak + ' bilan, \nzamonaviy shaxslardan esa ' + istak1 + ' bilan suhbat qurishni istar edim')

friends = []

friends.append('Anvar')
friends.append('Usmon')
friends.append('Nodir')
friends.append('Ali')
friends.append('Jovoir')
friends.append('ozodbek')

friends.remove('ozodbek')
friends.remove('Jovoir')

friends.insert(0,'Umidjon')
friends.insert(5,'Doston')
friends.insert(3,'Zoyir')


mehmonlar = []
mehmonlar.append('Umidjon')


mehmonlar.append(friends.pop(3))
mehmonlar.append(friends.pop(-1))
mehmonlar.append(friends.pop(4))




print("\nKelgan mehmonlar: ", mehmonlar)