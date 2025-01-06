#array 1 dimensi
my_list1 = ["saya", "suka", "coding", "sejak", 2023]

print(my_list1)

#array bersarang 
my_list2 = [["nama", "alamat", "umur"], ["dio", "bekasi", 18]]
print(my_list2)

#negative array
my_list3 = ['p', 'y', 't', 'h', 'o', 'n']
print(my_list3)

#Slicing
list_saya = ['p', 'y', 't', 'h', 'o', 'n']
print(list_saya[2:5])
#slicing dengan deklarasi index ke-1 sampai akhir
list_saya1 = ['p', 'y', 't', 'h', 'o', 'n']
print(list_saya1[1:])
#slicng dengan deklarasi index 0 sampai index ke-4
list_saya2 = ['p', 'y', 't', 'h', 'o', 'n']
print(list_saya2[:4])

#latihan assignment
list_nim = []
list_uts =[]
list_uas = []
nilai_total = []

#execute code with for loop
ulang = 2 #perulangan 2 kali
for i in range(ulang):
    print("data pertama", str(i+1))
    list_nim.append(input("masukkan Nim:"))
    list_uts.append(int(input("masukkan nilai UTS:")))
    list_uas.append(int(input("masukkan nilai UAS:")))
#proses kalkulasi nilai
for i in range(ulang):
    nilai_total.append((list_uts[i] + list_uas[i]) / 2)
#cetak

print("===================================================")
print("NIM      Nilai UTS       Nilai UAS            Total")
print("===================================================")
for i in range(ulang):
    print("%s \t %i \t\t %i \t\t\t %i" % 
    (list_nim[i], list_uts[i], list_uas[i], nilai_total[i]))
print("===================================================")
