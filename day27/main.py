import tkinter

FONT = ("Arial", 12, "normal")

window = tkinter.Tk()
window.title("Miles to Km calculator")
window.minsize(width=150, height=100)
window.config(padx=20, pady=20)

inputs = tkinter.Entry(width=10)
inputs.grid(row=0, column=1)

miles_label=tkinter.Label(text="Miles", font=FONT)
miles_label.grid(row=0, column=2)

is_equal_to_label = tkinter.Label(text="is equal to", font=FONT)
is_equal_to_label.grid(row=1, column=0)

km_transfer_label = tkinter.Label(text=0, font=FONT)
km_transfer_label.grid(row=1, column=1)

km_label = tkinter.Label(text="Km", font=FONT)
km_label.grid(row=1, column=2)

def button_clicked():
    miles = int(inputs.get())
    km = round(miles*1.609,2)
    km_transfer_label.config(text=km)

button = tkinter.Button(text="Calculate!", command=button_clicked)
button.grid(row=2, column=1)

window.mainloop()
