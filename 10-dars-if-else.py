# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 11:12:27 2023

@author: asadbek

"""
#--------------------------------10 -DARS IF - ELSE SHART OPERATORLARI--------------



moshinalar = []

moshinalar.append('toyota')
moshinalar.append('mazda')
moshinalar.append('hyundai')
moshinalar.append('gm')
moshinalar.append('kia')

for moshin in moshinalar:
    if moshin =='gm':
        print(f"{moshin.upper()}")
    else:
        print(f"{moshin.title()}")


print("\n")
print("-----------------------------------2 - MASALA---------------------------------------")
print("\n")


for moshin in moshinalar:
    if moshin != 'gm':
        print(f"{moshin.upper()}")
        
    else:
        print(f"{moshin.title()}")
        
        
print('\n')  
print("-----------------------------------3-masala------------------------------------")



# name = str(input("Ismingizni kiriting\n>>>"))

# if name.lower() == 'admin':
#     print("Xush kelibsiz! Admin")

# else:
#     print(f"Assalomu alaykum! {name.title()}")




print('\n')

print('-------------------------------------4-MASALA------------------------------------')

# son1 = int(input("Birinchi sonni kiriting\n>>>"))
# son2 = int(input("Ikkinchi sonni kiriting\n>>>"))


# if son1 == son2:
#     print("Sonlar teng!")


print('\n')

print("---------------------------------5-MASALA------------------------------------")


# ason = int(input("Istalgan sonni kiriting\n>>>>"))

# if ason<0:
#     print("Manfiy son")
# else:
#     print("Musbat son")    
    


print('\n')
print("----------------------------6-MASALA-----------------------------------------")

son1 = float(input('Istalgan son kiriting: '))
print(son1**(1/2)) if son1>0 else print('Musbat son kiriting')




      
        