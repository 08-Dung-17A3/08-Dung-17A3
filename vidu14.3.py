while True:   # ví dụ về syntax error
    try:
        x = int(input("Nhap so X = "))
        break
    except ValueError:
        print('Bị lỗi, xin mời nhập lại')
print("X=",x)
