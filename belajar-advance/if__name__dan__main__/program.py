# Apa itu __name__ ?
#
# Hal penting harus dipahami :
# 1.  Setiap Python membaca sebuah file (source code)
#     ia akan membuat beberapa variable khusus, salah
#     satunya __name__
# 2.  Python akan mengeksekusi semua code yang ada di 
#     file tersebut
print("")
print("Yang berjalan adalah = {}".format(__name__))
print("Sebelum import numpy")

import numpy as np

print("sebelum menjalankan fungsi numpy")

def fungsi_np():
    print("Hasil kali array([1,2,3]) * 2 = {}".format(np.array([1,2,3]) *2))

print("Sebelum menjalankan __name__ == '__main__'")

if __name__ == '__main__':
    fungsi_np()
    print("program.py sedang dijalankan langsung")
else:
    print("program.py Sedang di impor")

print("")