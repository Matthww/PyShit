from tkinter import Frame, Label, Tk


class openWindow(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        Frame.pack(self)
        Label(self, text='Test', width=72).pack()


if __name__ == '__main__':
    root = Tk()
    root.title("Test title")
    root.geometry("1920x1080")
    app = openWindow(root)
    root.mainloop()
