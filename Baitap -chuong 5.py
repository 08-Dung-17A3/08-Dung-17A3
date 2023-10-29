#Đây là chương trình thứ 2.
print("đây là chương trình thứ 3")
print("chương trình này được soạn thảo bằng IDE Visual studio code.")
# bài 1.2 viết phương trình tính toán đơn giản
x=10
y=5
tổng=x+y
hiệu=x-y
tích=x*y
thương=x/y
print("tổng của",x,'+',y,'=',tổng)
print("hiệu của",x,'-',y,'=',hiệu)
print("tích của",x,'*',y,'=',tích)
print("thương của",x,'/',y,'=',thương)
# bài 1.3 tính tiền phải trả khi mua hàng
so_luong=5
don_gia=25000
tien_phai_tra=so_luong*don_gia
print("tien_phai_tra",so_luong,'*',don_gia,'=',tien_phai_tra)
# bài 1.4 tính diện tích tam giác biết số đo 3 cạnh a,b,c
a,b,c=map(float,input("mời nhập độ dài 3 cạnh: ").split())
chuvi=a+b+c
p=chuvi/2
import math
dientich=math.sqrt(p*(p-a)*(p-b)*(p-c))
print('Dien tich là %.2f' %dientich)
# Bài 1.1 In ra màn hình chữ "Hello" 
print("** ** ******   **      **     *******"  )
print("** ** **       **      **     **   **")
print("***** ******   **      **     **   **")
print("** ** **       **      **     **   **")
print("** ** ******   ******  ****** *******")


