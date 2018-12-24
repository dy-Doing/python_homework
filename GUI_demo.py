import tkinter as tk

top = tk.Tk()

btn = tk.Button()


def clicked():
    print('I was clicked!')


btn['text'] = 'Click me'
btn['command'] = clicked

btn.pack()

tk.mainloop()

# import sys
# sys.path.append('C:/python')
