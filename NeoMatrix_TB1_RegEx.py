# Aristo Baadi - 41823010006
# Universitas Mercu Buana
# Tugas Besar 1 - Pemrograman Lanjut

# Menggunakan Regular Expression
import re

# Membuka File Input
with open('neomatrix.txt', 'r') as file: #Sesuaikan dengan directory dan nama file
    lines = file.readlines()

# Membaca File Input
file_input = lines[0].rstrip().split()
n = int(file_input[0])
m = int(file_input[1])

# Mendekode File Input
neomatrix = lines[1:]
decoded_list = list(zip(*neomatrix))
decoded_string = ''.join([''.join(item) for item in decoded_list])

# Menghapus yang bukan Alfanumerik
decoded_string = re.sub(r'[^a-zA-Z0-9]+\b', r' ', decoded_string).strip()

# Print Input yang sudah didekode
print(decoded_string)