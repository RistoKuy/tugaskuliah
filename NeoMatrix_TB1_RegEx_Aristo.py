# Aristo Baadi - 41823010006
# Universitas Mercu Buana
# Tugas Besar 1 - Pemrograman Lanjut

# Menggunakan Regular Expression
import re

# Membuka File Input
with open('neomatrix.txt', 'r') as file:
    lines = file.readlines()

# Membaca File Input
dimensions = lines[0].rstrip().split()
n = int(dimensions[0])
m = int(dimensions[1])

# Mendekode File Input
neomatrix = lines[1:]
transposed_matrix = list(zip(*neomatrix))
decoded_string = ''.join([''.join(item) for item in transposed_matrix])

# Menghapus yang bukan Alfanumerik
decoded_string = re.sub(r'[^a-zA-Z0-9]+\b', r' ', decoded_string).strip()

# Print Input yang sudah didekode
print(decoded_string)