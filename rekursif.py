def faktorial(n):
    if n==1 or n==0:
        return 1
    else:
        return(n* faktorial(n-1))

#fungsi rekursif telah selesai sampai disini
#berikutnya adalah memanggil fungsi

x=int(input("berapa faktorial?"))
print(x, "!= ", faktorial(x))
