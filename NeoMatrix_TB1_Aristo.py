# Aristo Baadi - 41823010006
# Universitas Mercu Buana
# Tugas Besar 1 - Pemrograman Lanjut

#Class untuk Mendekode Matrix
def decode_matrix(input_matrix):
    # Mengambil jumlah baris dan kolom dari input
    rows, cols = map(int, input_matrix[0].split())

    # Mendeklarasikan matriks kosong
    matrix = []

    # Mengisi matriks dengan input
    for row in input_matrix[1:]:
        matrix.append(list(row))

    # Mendekode teks dari matriks
    decoded_text = ''
    for col in range(cols):
        for row in range(rows):
            # Jika karakter bukan alfanumerik, ganti dengan spasi
            if not matrix[row][col].isalnum():
                decoded_text += ' '
            else:
                decoded_text += matrix[row][col]

    return decoded_text

# Contoh input
input_matrix = [
    '7 3',
    'Tsi',
    'h%x',
    'i #',
    'sM ',
    '$a ',
    '#t%',
    'ir!'
]

# Mendekode dan mencetak hasil
print(decode_matrix(input_matrix))