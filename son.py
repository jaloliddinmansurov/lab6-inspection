# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:12:21 2026

@author: user
"""

class SonTekshiruvchi:
    def __init__(self, son):
        self.son = son

    def juft_yoki_toq(self):
        if self.son % 2 == 0:
            return "Juft son"
        else:
            return "Toq son"


# Foydalanuvchidan son olish
son = int(input("Son kiriting: "))

# Obyekt yaratish
obj = SonTekshiruvchi(son)

# Natijani chiqarish
print(obj.juft_yoki_toq())