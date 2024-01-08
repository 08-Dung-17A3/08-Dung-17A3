try:
    x = eval(input("Nhập x\n"))
    y = eval(input("Nhập y\n"))
    z=x/y
except NameError as erl:
    print('error : ',erl)
except ZeroDivisionError as er2:
    print("error ", er2)
else:
    print('x/y', z)