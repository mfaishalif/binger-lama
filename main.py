def printTanggaPascal(n):
    batasMundur = n
    batasMaju = 1

    while batasMundur > 0 and batasMaju < n+1:
        for i in range(batasMundur):
            print(" ", end="")
        batasMundur -= 1        

        for kolom in range(batasMaju):
            entry = pascalEntry(batasMaju - 1, kolom)
            if kolom == batasMaju - 1:
                print(entry)
            else:
                print(entry, end=" ")
        batasMaju += 1        

def printTanggaPascal(n):
    batasMundur = n        # Inisialisasi spasi awal di sisi kiri
    batasMaju = 1          # Jumlah elemen per baris yang akan dicetak

    # Loop utama untuk membuat baris segitiga Pascal
    while batasMundur > 0 and batasMaju < n+1:
        # Cetak spasi untuk membuat efek tangga
        for i in range(batasMundur):
            print(" ", end="")
        batasMundur -= 1   # Kurangi spasi untuk baris berikutnya

        # Cetak angka-angka dalam baris Pascal
        for kolom in range(batasMaju):
            entry = pascalEntry(batasMaju - 1, kolom)  # Hitung nilai Pascal
            if kolom == batasMaju - 1:
                print(entry)  # Pindah baris setelah elemen terakhir
            else:
                print(entry, end=" ")  # Cetak dengan spasi antar elemen
        batasMaju += 1      # Tingkatkan jumlah elemen untuk baris berikutnya

def pascalEntry(row, col):
    return factorialRekursif(row) // (factorialRekursif(col) * factorialRekursif(row - col))

# Fungsi untuk menghitung nilai di posisi tertentu dalam segitiga Pascal
def pascalEntry(row, col):
    # Gunakan rumus kombinasi: C(row, col) = row!/(col!(row-col)!)
    return factorialRekursif(row) // (factorialRekursif(col) * factorialRekursif(row - col))

def factorialRekursif(n):
    if n < 1:
        return 1
    else:
        return n * factorialRekursif(n-1)

# Fungsi rekursif untuk menghitung faktorial
def factorialRekursif(n):
    if n < 1:
        return 1   # Basis: 0! dan 1! = 1
    else:
        return n * factorialRekursif(n-1)  # Rekursi: n! = n * (n-1)!

def printBilanganGenapRekursif(n):
    if n>=0:
        if n % 2==0:
            print(n)
        printBilanganGenapRekursif(n-1)

# Fungsi rekursif mencetak bilangan genap dari n ke 0
def printBilanganGenapRekursif(n):
    if n>=0:
        if n % 2==0:
            print(n)      # Cetak jika genap
        printBilanganGenapRekursif(n-1)  # Panggil diri sendiri dengan n-1

def printBanyakDigitTidakPrima(n):
    if n <= 0:  
        print(0)
    else:
        while n > 0:
            current = n % 10
            if current == 1 or current == 0:
                print(current)
            else:
                factor = 0
                for i in range(1, current + 1):
                    if current % i == 0:
                        factor += 1
                if factor > 2:
                    print(current)
            n //= 10

# Fungsi untuk memeriksa dan mencetak digit yang bukan bilangan prima
def printBanyakDigitTidakPrima(n):
    if n <= 0:  
        print(0)
    else:
        while n > 0:
            current = n % 10  # Ambil digit terakhir
            # Penanganan khusus untuk 0 dan 1
            if current == 1 or current == 0:
                print(current)
            else:
                # Hitung jumlah faktor untuk menentukan prima
                factor = 0
                for i in range(1, current + 1):
                    if current % i == 0:
                        factor += 1
                # Cetak jika bukan prima (faktor > 2)
                if factor > 2:
                    print(current)
            n //= 10  # Hapus digit terakhir


def rekursifBanyakFaktorTidakPrima(n):
    if n>0:
        if jumlahFaktor(n)>2:
            print(n)
        rekursifBanyakFaktorTidakPrima(n-1)

# Fungsi rekursif untuk mencetak bilangan dengan faktor banyak (bukan prima)
def rekursifBanyakFaktorTidakPrima(n):
    if n>0:
        if jumlahFaktor(n)>2:  # Cek jika jumlah faktor > 2
            print(n)
        rekursifBanyakFaktorTidakPrima(n-1)  # Panggil diri sendiri dengan n-1

def jumlahFaktor(n,pembagi=1):
    if n == 1 or n == 0:
        return 0
    if pembagi<=n:
        if n%pembagi==0:
            return 1+jumlahFaktor(n,pembagi+1)
        else:
            return jumlahFaktor(n,pembagi+1)
    return 0

# Fungsi rekursif untuk menghitung jumlah faktor bilangan
def jumlahFaktor(n,pembagi=1):
    if n == 1 or n == 0:
        return 0  # Basis: 0 dan 1 punya 0 faktor
    if pembagi<=n:
        if n%pembagi==0:  # Jika pembagi adalah faktor
            return 1+jumlahFaktor(n,pembagi+1)
        else:
            return jumlahFaktor(n,pembagi+1)
    return 0  # Basis: pembagi melebihi n

def rekursifInvestasi(p,r,n):
    if n == 1:
        return p * (1 + r)
    
    return rekursifInvestasi(p, r, n - 1) * (1 + r)

# Fungsi menghitung investasi dengan bunga majemuk rekursif
def rekursifInvestasi(p,r,n):
    if n == 1:  # Basis: tahun pertama
        return p * (1 + r)
    # Rekursi: tahun ke-n = hasil tahun n-1 * (1 + bunga)
    return rekursifInvestasi(p, r, n - 1) * (1 + r)

def isPrime(n):
    factorCounter = 0
    for i in range(1,n+1):
        if n%i==0:
            factorCounter+=1
    if factorCounter>2 or n==0 or n==1:
        return False
    else:
        return True

# Fungsi mengecek apakah bilangan prima
def isPrime(n):
    factorCounter = 0
    for i in range(1,n+1):
        if n%i==0:
            factorCounter+=1
    # Prima jika hanya punya 2 faktor (1 dan diri sendiri)
    if factorCounter>2 or n==0 or n==1:
        return False
    else:
        return True

def isEven(n):
    if n%2==0:
        return True
    else:
        return False

def isOdd(n):
    if n%2!=0:
        return True
    else:
        return False

def printOddRight(n):
    counterSpace = 0
    oddCounter = 1
    for i in range(n):
        for j in range(counterSpace):
            print(" ",end='')
        counterSpace+=1
        while(isOdd(oddCounter)==False):
            oddCounter+=1
        print(oddCounter)
        oddCounter+=1

# Fungsi untuk mencetak angka ganjil dengan alignment kanan
def printOddRight(n):
    counterSpace = 0       # Penghitung spasi di sebelah kiri
    oddCounter = 1        # Penghitung angka ganjil
    
    for i in range(n):
        # Cetak spasi untuk alignment kanan
        for j in range(counterSpace):
            print(" ",end='')
        counterSpace += 1  # Tambah spasi untuk baris berikutnya
        
        # Cari angka ganjil berikutnya
        while(isOdd(oddCounter)==False):  # Asumsi fungsi isOdd ada di tempat lain
            oddCounter += 1
        print(oddCounter)  # Cetak angka ganjil
        oddCounter += 1    # Lanjut ke angka berikutnya

def printPrimeLeft(n):
    counterSpace = n
    primeCounter = 1
    for i in range(n):
        for j in range(counterSpace):
            print(" ",end='')
        counterSpace-=1
        while(isPrime(primeCounter)==False):
            primeCounter+=1
        print(primeCounter)
        primeCounter+=1

# Fungsi untuk mencetak bilangan prima dengan alignment kiri
def printPrimeLeft(n):
    counterSpace = n       # Spasi awal di sebelah kiri
    primeCounter = 1       # Penghitung bilangan prima
    
    for i in range(n):
        # Cetak spasi yang berkurang setiap baris
        for j in range(counterSpace):
            print(" ",end='')
        counterSpace -= 1  # Kurangi spasi untuk baris berikutnya
        
        # Cari bilangan prima berikutnya
        while(isPrime(primeCounter)==False):
            primeCounter += 1
        print(primeCounter)  # Cetak bilangan prima
        primeCounter += 1    # Lanjut ke angka berikutnya

def validasi4Digit(n):
    count = 0
    while n >0:
        count+=1
        n//=10
    
    if count==4:
        return True
    else: return False

# Validasi apakah bilangan 4 digit
def validasi4Digit(n):
    count = 0
    # Hitung jumlah digit dengan loop pembagian
    while n > 0:
        count += 1
        n //= 10
    
    return count == 4  # Return True jika tepat 4 digit

def rekursifPrintGenap(n):
    if n>0:
        if n%2==0:
            print(n)
        rekursifPrintGenap(n-1)

# Rekursif untuk mencetak bilangan genap dari n ke 0
def rekursifPrintGenap(n):
    if n>0:
        if n%2==0:
            print(n)  # Cetak jika genap
        rekursifPrintGenap(n-1)  # Panggil diri sendiri dengan n-1

def isPalindromeInt(x):
        if x < 0:
            return False
        
        original = x
        reversed_num = 0
        
        while x > 0:
            digit = x % 10
            reversed_num = reversed_num * 10 + digit
            x //= 10  
        
        return original == reversed_num

# Cek apakah integer merupakan palindrome
def isPalindromeInt(x):
    if x < 0:
        return False  # Bilangan negatif bukan palindrome
    
    original = x
    reversed_num = 0
    
    # Balik angka dengan operasi modulus dan pembagian
    while x > 0:
        digit = x % 10
        reversed_num = reversed_num * 10 + digit
        x //= 10  
    
    return original == reversed_num  # Bandingkan angka asli dan kebalikannya

def isPalindromeString(s):
    counterFront = 0
    counterBack = len(s)-1

    while (counterFront <= counterBack):
        if s[counterFront] == s[counterBack]:
            counterFront+=1
            counterBack-=1
        else: return False

    return True 

# Cek apakah string merupakan palindrome
def isPalindromeString(s):
    counterFront = 0
    counterBack = len(s)-1

    # Bandingkan karakter dari depan dan belakang
    while (counterFront <= counterBack):
        if s[counterFront] == s[counterBack]:
            counterFront += 1
            counterBack -= 1
        else: 
            return False  # Tidak sama = bukan palindrome
    return True

def viewArr(n, arr):
    if n > len(arr):
        print("index out of bounds")
    else:
        i = len(arr)-n
        if i<len(arr):
            print(arr[i], end=" ")
            viewArr(n-1, arr)

# Fungsi untuk melihat array dari indeks akhir
def viewArr(n, arr):
    if n > len(arr):
        print("index out of bounds")
    else:
        i = len(arr)-n  # Hitung indeks mulai dari belakang
        if i<len(arr):
            print(arr[i], end=" ")  # Cetak elemen
            viewArr(n-1, arr)       # Rekursi dengan n-1

def viewArrReverse(n, arr):
    if n > len(arr):
        print("index out of bounds")
    else:
        if n>0:
            print(arr[n-1], end=" ")
            viewArrReverse(n-1, arr)

# Fungsi untuk melihat array secara terbalik
def viewArrReverse(n, arr):
    if n > len(arr):
        print("index out of bounds")
    else:
        if n>0:
            print(arr[n-1], end=" ")  # Cetak dari indeks n-1
            viewArrReverse(n-1, arr)  # Rekursi dengan n-1

def find_max(arr, n):
    if n > 0 and n<=len(arr):
        if n == 1:
            return arr[0]
        
        prev_max = find_max(arr, n - 1)
        
        if arr[n-1] > prev_max:
            return arr[n-1]
        else:
            return prev_max
    else:
        print("out of bounds")

# Mencari nilai maksimum dalam array secara rekursif
def find_max(arr, n):
    if n > 0 and n<=len(arr):
        if n == 1:  # Basis: hanya 1 elemen
            return arr[0]
        
        prev_max = find_max(arr, n - 1)  # Cari maks dari n-1 elemen
        
        # Bandingkan dengan elemen ke-n
        return arr[n-1] if arr[n-1] > prev_max else prev_max
    else:
        print("out of bounds")

def nbOfDigit(n):
    n = abs(n)

    if n < 10:
        return 1
    else:
        return 1 + nbOfDigit(n//10)


def sameFactor(n, k):
    if n>k:
        biggest = n
    else: biggest = k

    for i in range(1,biggest+1):
        if ((n%i==0) and (k%i==0)) and i != 1 and i != n and i != k:
            print(i, end=" ")

def smallestSameFactor(n, k):
    if n>k:
        biggest = n
    else: biggest = k

    i = 1
    while i<biggest+1:
        if ((n%i==0) and (k%i==0)) and i != 1 and i != n and i != k:
            return i

        i+=1
    return 0

# Fungsi untuk mencari faktor persekutuan terkecil (bukan 1, n, atau k)
def smallestSameFactor(n, k):
    if n>k:
        biggest = n
    else: 
        biggest = k

    i = 1
    while i<biggest+1:
        # Cari faktor persekutuan yang bukan 1, n, atau k
        if ((n%i==0) and (k%i==0)) and i != 1 and i != n and i != k:
            return i  # Return faktor pertama yang ditemukan
        i+=1
    return 0  # Return 0 jika tidak ada

def numOfDigit(n):
    if n < 0:
        n*=-1

    count = 0
    while n>0:
        count+=1
        n=n//10
    return count

# Fungsi rekursif menghitung jumlah digit (implementasi iteratif)
def numOfDigit(n):
    if n < 0:
        n*=-1  # Handle bilangan negatif

    count = 0
    while n>0:
        count+=1
        n=n//10  # Kurangi digit dengan pembagian integer
    return count

def numOfUniqDigit(n):
    lookUpTable = [0,0,0,0,0,0,0,0,0,0]

    if n < 0:
        n*=-1
    if n == 0:
        return 1

    count = 0
    while n>0:
        index = n%10
        if lookUpTable[index] == 0:
            count+=1
            lookUpTable[index]+=1
        n=n//10
    return count

# Fungsi menghitung digit unik menggunakan lookup table
def numOfUniqDigit(n):
    lookUpTable = [0,0,0,0,0,0,0,0,0,0]  # Penyimpanan digit 0-9

    if n < 0:
        n*=-1  # Handle bilangan negatif
    if n == 0:
        return 1  # Kasus khusus untuk 0

    count = 0
    while n>0:
        index = n%10  # Ambil digit terakhir
        if lookUpTable[index] == 0:
            count+=1
            lookUpTable[index]+=1  # Tandai digit yang sudah muncul
        n=n//10
    return count

def sumOfDigits(value):
    if (value == 0):
        return 0
    else:
        return sumOfDigits(value // 10) + (value % 10)

# Fungsi rekursif penjumlahan digit (ADA POTENSI BUG)
def sumOfDigits(value):
    if (value == 0):
        return 0
    else:
        # Seharusnya menggunakan integer division (//) bukan float division (/)
        return sumOfDigits(value / 10) + (value % 10)

def fibonacci(n):
    if n<=1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

# Fungsi fibonacci rekursif klasik (inefisien untuk n besar)
def fibonacci(n):
    if n<=1:
        return 1  # Basis: fibonacci(0) dan fibonacci(1) = 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)  # Rekursi ganda

def printDeretFibonacci(n):
    if n>1:
        printDeretFibonacci(n-1)
    print(fibonacci(n))

# Mencetak deret fibonacci secara rekursif
def printDeretFibonacci(n):
    if n>1:
        printDeretFibonacci(n-1)  # Rekursi untuk mencetak sebelumnya
    print(fibonacci(n))  # Cetak nilai fibonacci(n)

#Modul_Praktikum_7_2
#Soal No 5
def recursiveSearchArr(arr, n, key):
    if n>=0 and n<=len(arr):
        if n == 0:
            return False  
        
        current_element = arr[n-1]
        if current_element == key:
            return True  
        
        return recursiveSearchArr(arr, n-1, key)
    else: 
        print("out of bounds")

# Pencarian rekursif dalam array
def recursiveSearchArr(arr, n, key):
    if n>=0 and n<=len(arr):
        if n == 0:
            return False  # Basis: tidak ditemukan
        if arr[n-1] == key:
            return True  # Elemen ditemukan
        return recursiveSearchArr(arr, n-1, key)  # Cek elemen sebelumnya
    else: 
        print("out of bounds")

#Soal No 6
def cek_duplikat(data, n):
    # Fungsi rekursif bantu untuk membandingkan elemen pada indeks i dan j
    def telusuriDuplikat(i, j):
        # Basis: Jika i sudah mencapai elemen terakhir, tidak ada duplikasi yang ditemukan
        if i >= n - 1:
            return False
        # Jika j sudah melewati batas array, pindah ke indeks berikutnya untuk i dan set j menjadi i+2
        if j >= n:
            return telusuriDuplikat(i + 1, i + 2)
        # Jika ditemukan elemen yang sama antara data[i] dan data[j], maka ada duplikasi
        if data[i] == data[j]:
            return True
        # Lanjutkan pengecekan dengan menaikkan j
        return telusuriDuplikat(i, j + 1)
    
    # Mulai pengecekan dari pasangan indeks pertama (0 dan 1)
    return telusuriDuplikat(0, 1)

#Soal No 7
def cariFaktor(i,n):
    if i > abs(n):
        return
    if abs(n) % i == 0:
        if i == abs(n):
            print(f"{-i}, {i}", end="")
        else:
            print(f"{-i}, {i}, ", end="")
    cariFaktor(i + 1,n)

def cariFaktor(i,n):
    if i > abs(n):
        return
    if abs(n) % i == 0:
        # Cetak pasangan faktor positif dan negatif
        if i == abs(n):
            print(f"{-i}, {i}", end="")
        else:
            print(f"{-i}, {i}, ", end="")
    cariFaktor(i + 1,n)  # Rekursi ke faktor berikutnya

def tampilkan_faktor(n):
    cariFaktor(1,n)  

# Fungsi untuk menampilkan semua faktor bilangan (+/-)
def tampilkan_faktor(n):
    cariFaktor(1,n)  # Mulai pencarian dari 1

def perkalianFaktorPrima(i,n,result):
    if i > n:
        return result
    if n % i == 0 and isPrime(i):
        result *= i
    i += 1
    return perkalianFaktorPrima(i, n, result)

# Fungsi perkalian faktor prima
def perkalianFaktorPrima(i,n,result):
    if i > n:
        return result  # Basis: return hasil akhir
    if n % i == 0 and isPrime(i):
        result *= i  # Kalikan jika i adalah faktor prima
    i += 1
    return perkalianFaktorPrima(i, n, result)  # Cek bilangan berikutnya

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Tukar posisi
                swapped = True
        if not swapped:
            break  # Berhenti jika tidak ada pertukaran
    return arr

def hitung_mean(data):
    """Menghitung mean dari data."""
    total = 0
    for nilai in data:
        total += nilai
    return total / len(data)

def hitung_median(data_urut):
    """Menghitung median dari data yang sudah diurutkan."""
    n = len(data_urut)
    if n % 2 == 1:
        # Jika jumlah data ganjil, median adalah nilai tengah
        return data_urut[n // 2]
    else:
        # Jika jumlah data genap, median adalah rata-rata dua nilai tengah
        tengah1 = data_urut[(n // 2) - 1]
        tengah2 = data_urut[n // 2]
        return (tengah1 + tengah2) / 2

def hitung_modus(data):
    """Menghitung modus dari data.
       Jika terdapat lebih dari satu modus, dipilih nilai modus terkecil."""
    frekuensi = {}
    for nilai in data:
        if nilai in frekuensi:
            frekuensi[nilai] += 1
        else:
            frekuensi[nilai] = 1

    # Cari frekuensi maksimum
    max_frek = 0
    for frek in frekuensi.values():
        if frek > max_frek:
            max_frek = frek

    # Ambil semua nilai yang frekuensinya sama dengan nilai maksimum
    modus_list = []
    for nilai, frek in frekuensi.items():
        if frek == max_frek:
            modus_list.append(nilai)

    # Jika terdapat lebih dari satu modus, pilih yang terkecil
    return min(modus_list)

def hitung_kuartil(data):
    """Menghitung Q1, median (Q2), dan Q3 dari data."""
    # Urutkan data terlebih dahulu
    data_urut = sorted(data)
    n = len(data_urut)

    # Hitung median (Q2)
    Q2 = hitung_median(data_urut)

    # Bagi data untuk lower half dan upper half
    if n % 2 == 1:
        # Jika jumlah data ganjil, abaikan elemen tengah saat pembagian
        lower_half = data_urut[:n // 2]
        upper_half = data_urut[n // 2 + 1:]
    else:
        lower_half = data_urut[:n // 2]
        upper_half = data_urut[n // 2:]

    Q1 = hitung_median(lower_half)
    Q3 = hitung_median(upper_half)

    return Q1, Q2, Q3

# Contoh penggunaan
data = [7, 15, 36, 39, 40, 41, 41, 15]
print("Data:", data)

# Hitung kuartil
Q1, Q2, Q3 = hitung_kuartil(data)
print("Kuartil 1 (Q1):", Q1)
print("Median (Q2):", Q2)
print("Kuartil 3 (Q3):", Q3)

# Hitung mean
mean_val = hitung_mean(data)
print("Mean:", mean_val)

# Hitung modus
modus_val = hitung_modus(data)
print("Modus:", modus_val)