# date time

import datetime as dt

print("Masukkan tgl lahir anda :")
tanggal     = int(input())
print("Masukkan bulan lahir anda :")
bulan       = int(input())
print("Masukkan tahun lahir anda :")
tahun       = int(input())

tgl_lahir = dt.date(tahun, bulan, tanggal)
print('tgl lahir anda, ', tgl_lahir)

hari_ini    = dt.date.today()
umur_hari   = hari_ini - tgl_lahir
umur_tahun  = umur_hari.days // 365 # operator tsb untuk dapetin nilai integernya


print(f"Umur kamu saat ini {umur_tahun} tahun")

