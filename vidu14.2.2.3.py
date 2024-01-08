try:
    x = eval(input("nhập x\n"))
    y = eval(input("Nhập y\n"))
    z=x/y
except (NameError,ZeroDivisionError) as er:
    print('errorr :', er)
else:
    print('x/y',z)