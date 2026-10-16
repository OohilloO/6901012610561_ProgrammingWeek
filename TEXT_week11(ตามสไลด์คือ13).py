import tkinter

def multiply():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    result = num1 * num2
    label.config(text=result)

window = tkinter.Tk()
window.title("My tk App")
window.geometry("500x500")

label = tkinter.Label(window, text="Hello")
label.pack(pady=20)

entry_frame = tkinter.Frame(window)
entry_frame.pack(pady=20)
entry1 = tkinter.Entry(entry_frame, width=10)
entry1.pack(side="left", padx=5)
entry2 = tkinter.Entry(entry_frame, width=10)
entry2.pack(side="left", padx=5)

button = tkinter.Button(window, text="Multiply", command=multiply)
button.pack(pady=40)

window.mainloop()
#หน้าต่างมี label, ช่องกรอกเลข 2 ช่องเรียงข้างกัน และปุ่ม Multiply
#กดปุ่มแล้ว label แสดงผลคูณ