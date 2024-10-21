my_list = ["Prodi Ti", 1, 2, 3, 4, 1, 2, 3, 4,]
panjang_mylist = len(my_list)
print("my_list: ", my_list)
print("panjang_mylist: ", panjang_mylist)
print("panggil index ke 5: ", my_list[5])
my_list.append("keren")
print("my_list setelah di input nilai baru: ", my_list)
my_list.remove(2)
print("my_list setelah menghapus nilai ke 2 :", my_list)
del my_list[1]
print("my_list setelah menghapus index ke 1:", my_list)
