from tkinter import *

root = Tk()
root.title("Весы")
root.geometry("320x480")  

items = {"Яблоко": 242,"Дыня": 3065,"Ананас": 1240,"Персик": 175,"Банан": 146,"Авокадо": 238,"Апельсин": 187,"Лимон": 173,"Киви": 85,"Груша": 225}

def show_frame(frame):
    frame.tkraise()
    
root1 = Frame(root, bg="#8B5E5E")
root2 = Frame(root, bg="#8B5E5E")
root3 = Frame(root, bg="#8B5E5E")
root4 = Frame(root, bg="#8B5E5E")
show_frame(root1)

for roots in (root1, root2, root3, root4):
    roots.place(relwidth=1, relheight=1)

label_start = Label(root1, text="ВЕСЫ", font=("Arial Black", 50), fg="black", bg="#8B5E5E")
label_start.pack(pady=120)

btn_start = Button(root1, text="НАЧАТЬ", font=("Arial Black", 16), bg="#E79B9B", fg="black", command=lambda: show_frame(root2))
btn_start.pack(ipadx=20, ipady=10)

label_weights = Label(root2, text="ВЕСЫ", font=("Arial Black", 24), fg="black", bg="#8B5E5E")
label_weights.pack(pady=20)

btn_weigh = Button(root2, text="ВЗВЕШИВАНИЕ", font=("Arial Black", 16), bg="#E79B9B", fg="black", command=lambda: show_frame(root4))
btn_weigh.pack(pady=10, ipadx=10, ipady=8)

btn_info = Button(root2, text="ИНФОРМАЦИЯ", font=("Arial Black", 16), bg="#E79B9B", fg="black", command=lambda: show_frame(root3))
btn_info.pack(pady=10, ipadx=10, ipady=8)

btn_back = Button(root2, text="ВЕРНУТЬСЯ", font=("Arial Black", 16), bg="#E79B9B", fg="black", command=lambda: show_frame(root1))
btn_back.pack(side=BOTTOM, pady=20, ipadx=10, ipady=8)

label_info_weights = Label(root3, text="ВЕСЫ", font=("Arial Black", 24), fg="black", bg="#8B5E5E")
label_info_weights.pack(pady=10)

label_info_title = Label(root3, text="Инструмент для измерения\n"" массы предметов",
                           font=("Arial", 18), fg="white", bg="#8B5E5E")
label_info_title.pack(pady=5)
label_tips = Label(root3, text="Советы по использованию:", font=("Arial Black", 14), fg="black", bg="#8B5E5E")
label_tips.pack(pady=10)

tips = ("• Убедитесь, что весы находятся\n""  на ровной поверхности\n""• Калибруйте перед первым\n""  использованием")
label_tips = Label(root3, text=tips, font=("Arial", 14), fg="white", bg="#8B5E5E")
label_tips.pack(pady=5)

btn_back_info = Button(root3, text="ВЕРНУТЬСЯ", font=("Arial Black", 16), bg="#E79B9B", fg="black", command=lambda: show_frame(root2))
btn_back_info.pack(side=BOTTOM, pady=20, ipadx=10, ipady=8)

label_weigh_items = Label(root4, text="ПРЕДМЕТЫ", font=("Arial Black", 20), fg="black", bg="#8B5E5E")
label_weigh_items.pack(pady=10)

weight_var = StringVar(value="0 г")
weight_label = Label(root4, textvariable=weight_var, font=("Arial Black", 24), fg="black", bg="white", width=7)
weight_label.pack(pady=15)

def show_weight(item_name):
    w = items[item_name]
    weight_var.set(f"{w} г")

buttons_items = Frame(root4, bg="#8B5E5E")
buttons_items.pack(pady=10)

row = 0
col = 0
for idx, item in enumerate(items):
    btn = Button(buttons_items, text=item, font=("Arial Black", 12), bg="#E79B9B", fg="black", width=10, command=lambda name=item: show_weight(name))
    btn.grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 1:
        col = 0
        row += 1

btn_back_weigh = Button(root4, text="ВЕРНУТЬСЯ", font=("Arial Black", 16), bg="#E79B9B", fg="black", command=lambda: show_frame(root2))
btn_back_weigh.pack(side=BOTTOM, pady=20, ipadx=10, ipady=8)

root.mainloop()
