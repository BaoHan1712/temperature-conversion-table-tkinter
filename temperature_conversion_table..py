import tkinter as tk
# Hàm 
def convert_temperature():
    # Bắt lỗi
    try:
       # Lấy giá trị nhập vào từ ô nhập và chuyển nó thành số thực
        fahrenheit = float(fahrenheit_entry.get())
        celsius = (fahrenheit - 32) * 5.0/9.0
        # làm tròn kết quả đến 3 chữ số thập phân
        celsius_label.config(text=str(round(celsius, 3)) + " Độ C")
        # nếu chương trình lỗi thì chạy cái dòng này
    except ValueError:
        celsius_label.config(text="Giá trị không hợp lệ")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chuyển đổi nhiệt độ")

# Tạo khung màu vàng
frame = tk.Frame(root,bg="#33D1FF", bd=25)
frame.pack(padx=25, pady=25)

# Nhãn và ô nhập nhiệt độ Fahrenheit
fahrenheit_label = tk.Label(frame, text="Nhập độ F", bg="#33D1FF")
fahrenheit_label.grid(row=0, column=0)
fahrenheit_entry = tk.Entry(frame)
fahrenheit_entry.grid(row=0, column=1)

# Nút chuyển đổi
convert_button = tk.Button(frame, text="Chuyển", command=convert_temperature)
convert_button.grid(row=1, columnspan=2, pady=6)

# Nhãn hiển thị nhiệt độ Celsius
celsius_text_label = tk.Label(frame, text="Độ C", bg="#33D1FF", pady= 6)
celsius_text_label.grid(row=2, column=0)
celsius_label = tk.Label(frame, text="", bg="#33D1FF")
celsius_label.grid(row=2, column=1)
# khởi chạy
root.mainloop()