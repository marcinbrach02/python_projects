# moduł Tkinter - pierwsze okno
# import tkinter as tk
# gui = tk.Tk()
# gui.geometry("400x300")
# gui.title("HardCoder Window")
# gui.mainloop()


# dodawanie widgetów - obiektów
# import tkinter as tk
# gui = tk.Tk()
# gui.geometry("400x300")
# gui.title("HardCoder Window")

# button = tk.Button(gui, text="Click Me!")
# button.place(x=5,y=10)
# button2 = tk.Button(gui, text="Click Me2!")
# button2.place(x=5,y=40)

# gui.mainloop()


#inne typy widgetów
# import tkinter as tk
# gui = tk.Tk()
# gui.geometry("200x500")
# gui.title("HardCoder Window")

# button = tk.Button(gui, text="Click Me!").place(x=5, y=10)
# checkbox = tk.Checkbutton(gui, text="Accept this!").place(x=5,y=40)
# label = tk.Label(gui, text="This is label. Exists.").place(x=5, y=70)
# slider = tk.Scale(gui, from_=0, to=50, orient="horizontal").place(x=5, y=100)
# radio1 = tk.Radiobutton(gui, text="Option 1", value="checked").place(x=5, y=150)
# radio2 = tk.Radiobutton(gui, text="Option 2", value="unchecked").place(x=5, y=180)
# entry = tk.Entry(gui).place(x=5, y=210)
# spinbox = tk.Spinbox(gui, from_=3, to=10).place(x=5, y=240)

# gui.mainloop()


#listbox
# import tkinter as tk
# gui = tk.Tk()
# gui.geometry("400x300")
# gui.title("HardCoder Window")

# avaliable_values = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# listbox = tk.Listbox(gui)
# for item in avaliable_values:
#     listbox.insert(tk.END, item)
# listbox.place(x=5, y=10)

# gui.mainloop()


# combobox z modułu ttk
# import tkinter as tk
# import tkinter.ttk as ttk

# gui = tk.Tk()
# gui.geometry("400x300")
# gui.title("HardCoder Window")

# avaliable_values = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
# combo = ttk.Combobox(gui, values = avaliable_values)
# combo.place(x=5, y=10)
# gui.mainloop()


# funkcja pack()
# import tkinter as tk

# gui = tk.Tk()
# gui.geometry("400x300")
# gui.title("HardCoder Window")

# button = tk.Button(gui, text="Button1").pack()
# button2 = tk.Button(gui, text="Button2").pack(side=tk.LEFT)
# button3 = tk.Button(gui, text="Button3").pack(side=tk.LEFT)
# gui.mainloop()


# tworzenie obiektów w pętli
# import tkinter as tk
# gui = tk.Tk()
# gui.geometry("400x300")
# gui.title("HardCoder Window")

# for button_text in ["Button1", "Button2", "Button3"]:
#     new_button = tk.Button(gui, text=button_text).pack()

# gui.mainloop()



# interakcja z widgetami - funkcja konsoli
# import tkinter as tk

# gui = tk.Tk()
# gui.geometry("200x300")
# gui.title("HardCoder Window")
# def my_on_button():
#     print("Clicked!")
# button = tk.Button(gui, text="Click me", command=my_on_button).pack()
# gui.mainloop()


#interakcja - button + label
# import tkinter as tk
# gui = tk.Tk()
# gui.geometry("200x300")
# gui.title("HardCoder Window")

# label = tk.Label(gui, text="Initial text", bg="red", fg="blue")
# label.pack()
# def button_pressed():
#     label.config(text="CHANGED", bg="yellow")

# button = tk.Button(gui, text="ChangeLabel", command=button_pressed)
# button.pack(fill=tk.X)
# gui.mainloop()


#scale+label
# import tkinter as tk
# gui = tk.Tk()
# gui.geometry("200x300")
# gui.title("HardCoder Window")

# label = tk.Label(gui, text="Value: 0")
# label.pack()
# def slider_changed(value):
#     label.config(text="Value: "+str(value))

# slider = tk.Scale(gui, from_=10, to=-10, command=slider_changed)
# slider.pack()
# gui.mainloop()



#pobieranie wartości z widgetów - okno logowania
# import tkinter as tk
# gui = tk.Tk()

# login_frame = tk.Frame(gui)
# login_label = tk.Label(login_frame, text="Login")
# login_entry = tk.Entry(login_frame)
# login_label.pack(side=tk.LEFT)
# login_entry.pack(side=tk.RIGHT)
# login_frame.pack()

# password_frame = tk.Frame(gui)
# password_label = tk.Label(password_frame, text="Password")
# password_entry = tk.Entry(password_frame, show="*")
# password_label.pack(side=tk.LEFT)
# password_entry.pack(side=tk.RIGHT)
# password_frame.pack()
# users = {}

# def add_user():
#     login=login_entry.get()
#     password = password_entry.get()
#     if login not in users.keys():
#         users[login] = password
#         print("Added user: " + login)
#     else:
#         print("User " + login + " already exist!")

# button = tk.Button(gui, text="OK, please login!", command=add_user)
# button.pack()
# gui.mainloop()


# canvas - rysowanie w tkinter
# import tkinter as tk
# gui = tk.Tk()

# canvas = tk.Canvas(gui, width=500, height=300)
# canvas.create_rectangle(10,10,50,100, fill="red")
# canvas.create_polygon(100,10, 150,20, 70,100, fill="green")
# canvas.create_oval(10, 150, 50, 250, fill="blue")

# img = tk.PhotoImage(file="corgi_icon.png")
# canvas.create_image(200, 250, image=img)
# canvas.pack()


# tkinter + turtle
# import tkinter as tk
# import turtle

# gui = tk.Tk()
# canvas = tk.Canvas(gui, width=500, height=300)
# canvas.pack()

# t = turtle.RawTurtle(canvas)

# def go_forward():
#     t.forward(100)

# button = tk.Button(gui, text="Forward", command=go_forward)
# button.pack()


# tkinter + turtle - panel sterowania
import tkinter as tk
import turtle

gui = tk.Tk()
canvas = tk.Canvas(gui, width=500, height=300)
canvas.pack()
t = turtle.RawTurtle(canvas)
t.left(90)
speed = 5

def go():
    t.forward(speed)

def back():
    t.backward(speed)

def left():
        t.left(30)

def right():
        t.right(30)

def change_speed(val):
    global speed
    speed=int(val)

frame = tk.Frame()

go = tk.Button(frame, text="Go", command=go).pack()
left = tk.Button(frame, text="Left", command=left).pack()
right = tk.Button(frame, text="Right", command=right).pack()
back = tk.Button(frame, text="Go Back", command=back).pack()
frame.pack()

slider = tk.Scale(gui, from_=0, to=100, orient=tk.HORIZONTAL, command=change_speed)
slider.pack(side=tk.BOTTOM)
