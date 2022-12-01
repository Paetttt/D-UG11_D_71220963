print('Halo selamat datang di bioskop!')
print('Dimanakah kamu ingin menonton?')
print('1.) XXI Empire')
print('2.) XXI Amplaz')
print('3.) XXI JCM')

bioskop = int(input('Masukkan pilihanmu: '))

print('Mau nonton film apa nih? Ada film: ')
print('1. Frozen')
print('2. Keramat')
print('3. KKN di desa penari')

if bioskop == 1:
    print('XXI Empire')
elif bioskop == 2:
    print('XXI Amplaz')
elif bioskop == 3 :
    print('XXI JCM')


film = int(input('Pilih nomor film: '))
if film == 1:
     print('1. Frozen')
elif film == 2:
    print('2. Keramart')
elif film == 3:
    print('3. KKN di desa penari')



# elif film == 2:
#     print('XXI Amplaz')