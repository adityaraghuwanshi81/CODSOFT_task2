import tkinter as tk
import math


root = tk.Tk()
root.title("Advanced Calculator - CodSoft")
root.geometry("420x620")
root.configure(bg="#1E1E1E")
root.resizable(False, False)

expression = ""

def press(value):
    global expression
    expression += str(value)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def equal():
    global expression
    try:
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def sqrt():
    global expression
    try:
        result = str(math.sqrt(float(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def square():
    global expression
    try:
        result = str(float(expression) ** 2)
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def sin():
    global expression
    try:
        result = str(math.sin(math.radians(float(expression))))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def cos():
    global expression
    try:
        result = str(math.cos(math.radians(float(expression))))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def tan():
    global expression
    try:
        result = str(math.tan(math.radians(float(expression))))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def log():
    global expression
    try:
        result = str(math.log10(float(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""

def ln():
    global expression
    try:
        result = str(math.log(float(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set("Error")
        expression = ""


equation = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=equation,
    font=("Arial", 24),
    bd=10,
    relief=tk.RIDGE,
    justify="right",
    bg="white"
)
display.grid(row=0, column=0, columnspan=5, pady=15, padx=10)


btn = {
    "font": ("Arial", 14, "bold"),
    "width": 6,
    "height": 2,
    
}


tk.Button(root, text="C", command=clear, bg="red", fg="white", **btn).grid(row=1, column=0)
tk.Button(root, text="⌫", command=backspace, bg="orange", fg="white", **btn).grid(row=1, column=1)
tk.Button(root, text="√", command=sqrt, bg="#555", fg="white", **btn).grid(row=1, column=2)
tk.Button(root, text="x²", command=square, bg="#555", fg="white", **btn).grid(row=1, column=3)
tk.Button(root, text="/", command=lambda: press("/"), bg="#2196F3", fg="white", **btn).grid(row=1, column=4)


tk.Button(root, text="7", command=lambda: press(7), **btn).grid(row=2, column=0)
tk.Button(root, text="8", command=lambda: press(8), **btn).grid(row=2, column=1)
tk.Button(root, text="9", command=lambda: press(9), **btn).grid(row=2, column=2)
tk.Button(root, text="*", command=lambda: press("*"), bg="#2196F3", fg="white", **btn).grid(row=2, column=3)
tk.Button(root, text="%", command=lambda: press("%"), bg="#2196F3", fg="white", **btn).grid(row=2, column=4)


tk.Button(root, text="4", command=lambda: press(4), **btn).grid(row=3, column=0)
tk.Button(root, text="5", command=lambda: press(5), **btn).grid(row=3, column=1)
tk.Button(root, text="6", command=lambda: press(6), **btn).grid(row=3, column=2)
tk.Button(root, text="-", command=lambda: press("-"), bg="#2196F3", fg="white", **btn).grid(row=3, column=3)
tk.Button(root, text="^", command=lambda: press("**"), bg="#2196F3", fg="white", **btn).grid(row=3, column=4)


tk.Button(root, text="1", command=lambda: press(1), **btn).grid(row=4, column=0)
tk.Button(root, text="2", command=lambda: press(2), **btn).grid(row=4, column=1)
tk.Button(root, text="3", command=lambda: press(3), **btn).grid(row=4, column=2)
tk.Button(root, text="+", command=lambda: press("+"), bg="#2196F3", fg="white", **btn).grid(row=4, column=3)
tk.Button(root, text="=", command=equal, bg="green", fg="white", **btn).grid(row=4, column=4)


tk.Button(root, text="0", command=lambda: press(0), **btn).grid(row=5, column=0)
tk.Button(root, text=".", command=lambda: press("."), **btn).grid(row=5, column=1)
tk.Button(root, text="π", command=lambda: press(str(math.pi)), bg="#555", fg="white", **btn).grid(row=5, column=2)
tk.Button(root, text="e", command=lambda: press(str(math.e)), bg="#555", fg="white", **btn).grid(row=5, column=3)
tk.Button(root, text="(", command=lambda: press("("), **btn).grid(row=5, column=4)


tk.Button(root, text=")", command=lambda: press(")"), **btn).grid(row=6, column=0)
tk.Button(root, text="sin", command=sin, bg="#9C27B0", fg="white", **btn).grid(row=6, column=1)
tk.Button(root, text="cos", command=cos, bg="#9C27B0", fg="white", **btn).grid(row=6, column=2)
tk.Button(root, text="tan", command=tan, bg="#9C27B0", fg="white", **btn).grid(row=6, column=3)
tk.Button(root, text="log", command=log, bg="#9C27B0", fg="white", **btn).grid(row=6, column=4)


tk.Button(root, text="ln", command=ln, bg="#9C27B0", fg="white", width=34, height=2,
          font=("Arial", 14, "bold")).grid(row=7, column=0, columnspan=5, pady=5)

root.mainloop()