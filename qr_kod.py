# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 08:28:54 2026

@author: user
"""
import qrcode

matn = input("Matn yoki URL kiriting: ")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)

qr.add_data(matn)
qr.make(fit=True)

rasm = qr.make_image(fill_color="black", back_color="white")

rasm.save("QR_KOD.png")

print("QR kod yaratildi va QR_KOD.png fayliga saqlandi.")