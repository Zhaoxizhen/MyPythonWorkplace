from tkinter import *
from tkinter.scrolledtext import ScrolledText


def save_btn_onclick():
    with open(filename_text.get(), 'w') as file:
        file.write(content_text.get('1.0', END))


def open_btn_onclick():
    with open(filename_text.get()) as file:
        content_text.delete('1.0', END)
        content_text.insert(INSERT, file.read())


if __name__ == '__main__':
    top = Tk()
    filename_text = Entry()
    filename_text.pack(side=LEFT, fill=X, expand=True)
    content_text = ScrolledText()
    content_text.pack(side=BOTTOM, fill=BOTH, expand=True)
    open_btn = Button(text='open', command=open_btn_onclick).pack(side=LEFT)
    save_btn = Button(text='save', command=save_btn_onclick).pack(side=LEFT)
    top.mainloop()


