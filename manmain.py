from tkinter import *
import pickle
import webbrowser

#kek

def add_item():
    item = entry.get()
    listbox.insert(END, item)
    entry.delete(0, END)

def remove_item():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)

def save_item():
    items = list(listbox.get(0, END))
    with open("cicamica.pkl", "wb") as cica:
        pickle.dump(items, cica)
    with open("cucumucu.txt", "w", encoding="utf-8") as cucu:
        for item in items:
            print(item, file=cucu)

def load_list():
    try:
        with open("cicamica.pkl", "rb") as cica:
            items = pickle.load(cica)
            for item in items:
                listbox.insert(END, item)
    except FileNotFoundError:
        pass

def net():
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

root = Tk()
root.title("sopping liszt")
root.geometry("500x500")

bg_color = "#a4907c"
button_color = "#c8b6a6"

root.configure(bg = bg_color)

entry = Entry(root)
entry.configure(bg = bg_color, width = 30)
entry.pack()

add_button = Button(root, bg = button_color, text = "add", command=add_item)
remove_button = Button(root, bg = button_color, text = "remove", command=remove_item)
save_button = Button(root, bg = button_color, text = "save", command=save_item)
browse_button = Button(root, bg = button_color, text = "browse", command=net)

add_button.pack()
remove_button.pack()
save_button.pack()
browse_button.pack()

listbox = Listbox(root, height=50, width=30)
listbox.configure(bg=bg_color)
listbox.pack()

load_list()

root.mainloop()
