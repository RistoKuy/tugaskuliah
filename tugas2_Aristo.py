# Aristo Baadi - 41823010006
# Universitas Mercu Buana 
# Tugas 2 - Pemrograman Lanjut

# Pilihan Tugas Part A atau B
print("Pilih part! \n1. Part A\n2. Part B")
pilihan = int(input("Pilihan Anda: "))

#Tugas Part A dan B
import os
os.system('cls')

# Tugas Part A
if pilihan == 1:
    n = int(input("Masukkan n: "))  
    for i in range(n):
        print(i**2)
        
# Tugas Part B
elif pilihan == 2:
    n = int(input("Masukkan n: "))
    for i in range(n):
        if i % 2 == 1 or i == 0:
            print(i**2)
else:
    print("Undefined")
    
    