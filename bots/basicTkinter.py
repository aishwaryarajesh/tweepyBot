import tkinter
tk=tkinter.Tk()

#creating & adding widgets for twttier
window = tk.Tk()

logo = tk.PhotoImage(file="twitter.gif")

explanation = """At present, we are working on
implementing more Twitter data for your
convenience. Stay tuned for more!"""

window.title("Welcome to My App!")
window.geometry('350x200')
l = tk.Label(window, text="Hello")
l.grid(column=10, row=10)
def click():
    l.configure(text="Button was clicked!!")
b = tk.Button(window, text="Click Me", command=click)
b.grid(column=1, row=0)
window.mainloop()

