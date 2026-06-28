import tkinter as tk
from tkinter import ttk, messagebox
import math


# =========================
# Hàm đổi độ sang độ - phút
# =========================
def degree_to_dm(angle):
    degree = int(angle)
    minute = round((angle - degree) * 60)

    if minute == 60:
        degree += 1
        minute = 0

    return degree, minute


# =========================
# Hàm tính góc
# =========================
def tinh_goc():
    try:
        value = float(txt_value.get())
        loai = cbo_type.get()

        if loai == "sin":
            if not -1 <= value <= 1:
                raise ValueError("Giá trị sin phải từ -1 đến 1.")
            angle = math.degrees(math.asin(value))

        elif loai == "cos":
            if not -1 <= value <= 1:
                raise ValueError("Giá trị cos phải từ -1 đến 1.")
            angle = math.degrees(math.acos(value))

        elif loai == "tan":
            angle = math.degrees(math.atan(value))

        elif loai == "cot":
            if value == 0:
                raise ValueError("cot không được bằng 0.")
            angle = math.degrees(math.atan(1 / value))

        else:
            raise ValueError("Chưa chọn loại.")

        deg, minute = degree_to_dm(angle)

        lbl_result.config(
            text=f"Góc a = {angle:.8f}°\n≈ {deg}° {minute}'",
            fg="blue"
        )

    except Exception as e:
        messagebox.showerror("Lỗi", str(e))


# =========================
# Giao diện
# =========================
root = tk.Tk()
root.title("TÍNH GÓC TỪ HÀM LƯỢNG GIÁC")
root.geometry("420x280")
root.resizable(False, False)

title = tk.Label(root,
                 text="TÍNH GÓC a",
                 font=("Arial", 16, "bold"),
                 fg="red")
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame,
         text="Chọn hàm:",
         font=("Arial", 11)).grid(row=0, column=0, padx=5, pady=5)

cbo_type = ttk.Combobox(
    frame,
    values=["sin", "cos", "tan", "cot"],
    width=10,
    state="readonly"
)
cbo_type.current(0)
cbo_type.grid(row=0, column=1, padx=5)

tk.Label(frame,
         text="Giá trị:",
         font=("Arial", 11)).grid(row=1, column=0, padx=5, pady=5)

txt_value = tk.Entry(frame, width=15, font=("Arial", 11))
txt_value.grid(row=1, column=1)

btn = tk.Button(root,
                text="TÍNH GÓC",
                font=("Arial", 12, "bold"),
                bg="#4CAF50",
                fg="white",
                width=15,
                command=tinh_goc)

btn.pack(pady=15)

lbl_result = tk.Label(root,
                      text="Kết quả sẽ hiển thị ở đây",
                      font=("Arial", 12),
                      fg="green")

lbl_result.pack()

root.mainloop()