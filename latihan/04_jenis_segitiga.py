a = float(input("Masukkan sisi pertama: "))
b = float(input("Masukkan sisi kedua: "))
c = float(input("Masukkan sisi ketiga: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Segitiga sama sisi.")
    elif a == b or a == c or b == c:
        print("Segitiga sama kaki.")
    else:
        print("Segitiga sembarang.")
else:
    print("Bukan segitiga.")