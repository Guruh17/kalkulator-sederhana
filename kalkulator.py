import os

#penjumlahan
def tambah(x, y):
    return x+y
#pengurangan
def kurang(x, y):
    return x-y
#perkalian
def kali(x, y):
    return x*y
#pembagian
def bagi(x, y):
    return x/y
#akar
def akar(x):
    return x**0.5
#pangkat
def pangkat(x, y):
    return x**y

#menu
def menu():
    print('------------------------------------------')
    print('-----------KALKULATOR SEDERHANA-----------')
    print('------------------------------------------')
    print('________________Pilih Menu________________')
    print('1. Penjumlahan')
    print('2. Pengurangan')
    print('3. Perkalian')
    print('4. Pembagian')
    print('5. Akar')
    print('6. Pangkat')
    print('0. Keluar')
    print('-----------------------------------------')

#kalkulator
def kalkulator():
    menu()
    pilihan=int(input('Masukkan Pilihan Menu: '))

    os.system('cls')

    if pilihan == 1:
        x=int(input('Masukkan Bil 1: '))
        y=int(input('Masukkan Bil 2: '))
        print(x, '+', y, '=', tambah(x,y))
    elif pilihan == 2:
        x=int(input('Masukkan Bil 1: '))
        y=int(input('Masukkan Bil 2: '))
        print(x, '-', y, '=', kurang(x,y))
    elif pilihan == 3:
        x=int(input('Masukkan Bil 1: '))
        y=int(input('Masukkan Bil 2: '))
        print(x, 'x', y, '=', kali(x,y))
    elif pilihan == 4:
        x=int(input('Masukkan Bil 1: '))
        y=int(input('Masukkan Bil 2: '))
        print(x, ':', y, '=', bagi(x,y))
    elif pilihan == 5:
        x=int(input('Masukkan Bil: '))
        print(x, '^ 1/2', '=', akar(x))
    elif pilihan == 6:
        x=int(input('Masukkan Bil 1: '))
        y=int(input('Masukkan Bil 2: '))
        print(x, '^', y, '=', pangkat(x,y))
    elif pilihan == 0:
        exit()
    else:
        print('Pilihan Mneu Tidak Ada')

if __name__ == '__main__':
    while True:
        kalkulator()