try:
    # giả sử có 1 số code ở đây có thể ném ra nhiều loại ngoại lệ khác nhau
    value = int(input("Nhập một số : "))
    result = 10 / value
except ValueError:
    #Bắt và xử lí ngoại lệ khi giá trị nhập không phải là số
    print(" Đó không phải là một giá trị số hợp lệ .")
except ZeroDivisionError:
    # bắt và xử lý ngoại lệ khi chia cho 0
    print("Lỗi chia cho 0.")
except:
    # Bất kì ngoại lệ nào khác không được xác định cụ thể ở trên
    print("Một lỗi không xác định đã xảy ra.")
else:
    #chạy nếu không có ngoại lệ nào xảy ra
    print("Không có lỗi xảy ra.Kết quả là:",result)
finally:
    #chạy không phụ thuộc vào việc có lỗi xảy ra hay không
    print("Hoàn thành xử lý ngoại lệ.")
