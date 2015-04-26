import tkinter as Tkinter
from random import randint
from time import sleep
 
textFont1 = ("Arial", 10, "bold italic")
textFont2 = ("Arial", 16, "bold")
textFont3 = ("Arial", 8, "bold")
 
class LabelWidget(Tkinter.Entry):
    def __init__(self, master, x, y, text):
        self.text = Tkinter.StringVar()
        self.text.set(text)
        Tkinter.Entry.__init__(self, master=master)
        self.config(relief="ridge", font=textFont1,
                    bg="#fffffffff", fg="#000000fff",
                    readonlybackground="#ffffff000",
                    justify='center',width=5,
                    textvariable=self.text,
                    state="readonly")
        self.grid(column=x, row=y)
 
class EntryWidget(Tkinter.Entry):
    def __init__(self, master, x, y):
        Tkinter.Entry.__init__(self, master=master)
        self.value = Tkinter.StringVar()
        self.config(textvariable=self.value, width=5,
                    relief="ridge", font=textFont1,
                    bg="#ddddddddd", fg="#000000000",
                    justify='center')
        self.grid(column=x, row=y)
        self.value.set("")
 
class ButtonWidget(Tkinter.Button):
    def __init__(self, master, x, y):
        Tkinter.Button.__init__(self, master=master)
        self.value = Tkinter.StringVar()
        self.config(textvariable=self.value, width=1)
        self.grid(column=x, row=y)
        self.value.set("")



class EntryGrid(Tkinter.Tk):
    ''' Dialog box with Entry widgets arranged in columns and rows.'''
    def __init__(self, colList, rowList, title="Entry Grid"):
        self.cols = colList[:]
        self.colList = colList[:]
        self.colList.insert(0, "")
        self.rowList = rowList
        Tkinter.Tk.__init__(self)
        self.title(title)
 
        self.mainFrame = Tkinter.Frame(self)
        self.mainFrame.config(padx='3.0m', pady='3.0m')
        self.mainFrame.grid()
        self.make_header()
 
        self.gridDict = {}
        for i in range(1, len(self.colList)):
            for j in range(len(self.rowList)):
                w = EntryWidget(self.mainFrame, i, j+1)
                self.gridDict[(i-1,j)] = w.value
                def handler(event, col=i-1, row=j):
                    return self.__entryhandler(col, row)
                w.bind(sequence="<FocusOut>", func=handler)
        self.mainloop()
 
    def make_header(self):
        self.hdrDict = {}
        for i, label in enumerate(self.colList):
            def handler(event, col=i, row=0, text=label):
                return self.__headerhandler(col, row, text)
            w = LabelWidget(self.mainFrame, i, 0, label)
            self.hdrDict[(i,0)] = w
            w.bind(sequence="<KeyRelease>", func=handler)
 
        for i, label in enumerate(self.rowList):
            def handler(event, col=0, row=i+1, text=label):
                return self.__headerhandler(col, row, text)
            w = LabelWidget(self.mainFrame, 0, i+1, label)
            self.hdrDict[(0,i+1)] = w
            w.bind(sequence="<KeyRelease>", func=handler)

        for i in range(6):
            def handler(event, text='testbutton'):
                print('test')
                self.populate()
            b = ButtonWidget(self.mainFrame, i + 1, 13)
            b.bind("<Button-1>", handler)

        for i in range(6):
            def handler(event, text='testbutton'):
                print('test')
                self.populate()
            b = ButtonWidget(self.mainFrame, i + 1, 14)
            b.bind("<Button-1>", handler)
 
    def __entryhandler(self, col, row):
        s = self.gridDict[(col,row)].get()
        print(col, row)
        if s.upper().strip() == "EXIT":
            self.destroy()
        elif s.upper().strip() == "DEMO":
            self.demo()
        elif s.upper().strip() == "POP":
            self.populate()
        elif s.strip():
            print(s)

 
    def demo(self):
        ''' enter a number into each Entry field '''
        for i in range(len(self.cols)):
            for j in range(len(self.rowList)):
                sleep(0.25)
                self.set(i,j,"")
                self.update_idletasks()
                sleep(0.1)
                self.set(i,j,i+1+j)
                self.update_idletasks()
 
    def populate(self):
        line = [[randint(1, 60) for x in range(6)] for x in range(10)]
        line = sorted(line)
        print(line)
        for i in range(len(self.cols)):
            for j in range(len(self.rowList)):
                line[j] = sorted(line[j])
                self.set(i,j,line[j][i])
                self.update_idletasks()



    def __headerhandler(self, col, row, text):
        ''' has no effect when Entry state=readonly '''
        self.hdrDict[(col,row)].text.set(text)
 
    def get(self, x, y):
        return self.gridDict[(x,y)].get()
 
    def set(self, x, y, v):
        self.gridDict[(x,y)].set(v)
        return v
 
if __name__ == "__main__":
    rows = 'A B C D E F G H I J'.split()
    cols = '1 2 3 4 5 PB'.split()
    app = EntryGrid(cols, rows)