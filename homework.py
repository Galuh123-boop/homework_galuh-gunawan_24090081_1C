title = 'Penerimaan Mahasiswa Jalur Utbk'
print(title.upper())

biodata = {f'Nama' : 'Asep',
            'Asal Sekolah' : 'SMAN 1 BOJONG',
            'Umur' : 17,
            'Nilai Utbk' : 750,
            }
biodata = {f'Nama' : 'Udin',
            'Asal Sekolah' : 'SMAN 1 BOJONG ',
            'Umur' : 18,
            'Nilai Utbk' : 640,
            }
biodata = {f'Nama' : 'Wahyu',
            'Asal Sekolah' : 'SMAN 1 BOJONG',
            'Umur' : 18,
            'Nilai Utbk' : 820,
            }
biodata = {f'Nama' : 'Apis',
            'Asal Sekolah' : 'SMAN 1 BOJONG',
            'Umur' : 17,
            'Nilai Utbk' : 590,
            }

nama = str(input('Masukan Nama : '))
asal_sekolah = str(input('Masukan Asal Sekolah : '))
umur = int(input('Masukan Umur : '))
nilai = int(input('Masukan Nilai Utbk : ')) 
lolos = True
tidak_lolos = False

if nilai >= 700:
    hasil = ('Lolos Utbk')
else:
    hasil = ('Tidak Lolos Utbk')

print('Nama : ', nama)
print('Asal Sekolah : ', asal_sekolah)
print('Umur : ', umur)
print('Nilai Utbk: ', nilai) 
print(hasil)
