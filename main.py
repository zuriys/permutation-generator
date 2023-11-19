def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def permutasi(kata):
    if len(kata) == 1:
        return [kata]
    else:
        result = []
        for i in range(len(kata)):
            char = kata[i]
            sisa_char = kata[:i] + kata[i+1:]
            for perm in permutasi(sisa_char):
                result.append(char + perm)
        return result


def siklisPermutation(n):
    return factorial(n - 1)

def tampilkanSusunan(susunan, n):
    for i in range(n):
        print(susunan[i], end="")
 





def main():

    print("===========================================")
    print("== PERMUTASI APA YANG INGIN ANDA LAKUKAN ==")
    print("===========================================\n")
    print("1.Permutasi Unsur Tak Sama\n2.Permutasi Unsur Sama\n3.Permutasi Siklis\n4.Permutasi tanpa perulangan\n5.Permutasi dengan Perulangan ")
   
    pilihan = input("\nMasukkan Pilihan Anda : ")

    if pilihan == "1":
        print("\n=== Permutasi Unsur Tak sama ===\n")
        n = int(input("Masukkan Nilai n :"))

        hasil_PTS = factorial(n)
        print("Hasil Permutasi dari n : ",hasil_PTS)

        print("\n")

    elif pilihan == "2":
        print("\n=== Permutasi Unsur sama ===\n")
        kata = input("Masukkan Kata : ")

        iris = list(set(permutasi(kata)))
        print("\nJumlah bentuk yang dapat disusun : ",len(iris),"\n")

        for i in range(len(iris)):
            print(i+1,".",iris[i])
        
        print("\n")

    elif pilihan == "3":
        print("\n=== Permutasi Siklis ===\n")

        n = int(input("Masukkan jumlah orang: "))

        if n < 0:
            print("Input tidak valid. Jumlah orang tidak dapat negatif.")
            exit(1)

        totalPermutasi = siklisPermutation(n)

        print("Jumlah susunan berbeda:", totalPermutasi)

        susunan = [chr(ord('A') + i) for i in range(n)]

        print("Susunan-susunan berbeda:")
        nomorSusunan = 1


        for i in range(totalPermutasi):
            print("\nSusunan ke-", nomorSusunan, ": ", end="")
            tampilkanSusunan(susunan, n)
            nomorSusunan += 1
            susunan = susunan[1:] + [susunan[0]]
           
        print("\n")               

    
    elif pilihan == "4":
         print("\n=== Permutasi Tanpa Perulangan ===\n")
         n = int(input("Masukkan Nilai n :"))
         m = int(input("Masukkan Nilai m :"))
         if 0 <= m <= n :
            hasil_PTP = int(factorial(n)/factorial(n-m))
            print("\nHasil Permutasi Tanpa Perulangan dari n & m : ",hasil_PTP)

            print("\n")

         else:
            print("\nJumlah Objek (n) tidak boleh lebih kecil dari pada Objek pemilih (m)\n")

  

    elif pilihan == "5":
        print("\n=== Permutasi Dengan Perulangan ===\n")

        n = int(input("Masukkan Nilai n :"))
        m = int(input("Masukkan Nilai m :"))
        hasil_PDP = n
        
        for i in range(m-1):
            hasil_PDP *= n  
        
        print("\nHasil Permutasi Dengan Perulangan dari n & m : ", hasil_PDP)

        print("\n")

    else:
        print("Pilihan Anda Tidak Tersedia -_-")

        print("\n")
   

    
if __name__ == "__main__":
    main()