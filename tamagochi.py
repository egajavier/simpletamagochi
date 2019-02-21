pemilik = input('Siapa Nama Kamu ? \n')
print('Halo '+ pemilik +' Selamat Bermain, Silahkan Masukkan Nama Pet Kamu')

name = input('Siapa Nama Pet Kamu ? \n')
pet = {"nama" : name, "health" : 100}

def startGame():
    menu = input('\nApa Yang Ingin Kamu Lakukan ? \n 1. Makan \n 2. Periksa \n 3. Keluar \n')
    if menu == '1':
        print('Nyam... Nyam...')
        makan()
    elif menu == '2':
        print('Tok... Tok...')
        periksa()
    else:
        print('Dadaahh')

def makan():
    pet['health'] += 100
    return startGame()

def periksa():
    print("Nama Pet Kamu Adalah " + pet['nama'] + "Dan Kekuatan Kamu Sebesar", pet['health'])
    return startGame()

startGame()
