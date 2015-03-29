import tkinter

class simpleapp_tk(tkinter.Tk):
	def __init__(self, parent):
		tkinter.Tk.__init__(self, parent)
		self.parent = parent
		self.initialize()

	def initialize(self):
		self.grid()

		self.entryVariable = tkinter.StringVar()
		self.entry = tkinter.Entry(self, textvariable=self.entryVariable)
		self.entry.grid(column=0,row=0,sticky='EW')
		self.entry.bind("<Return>", self.OnPressEnter)
		self.entryVariable.set(u"Enter text here.")

		button = tkinter.Button(self, text=u"Click me !", command=self.OnButtonClick)

		button.grid(column=1, row=0)

		self.labelVariable = tkinter.StringVar()
		label = tkinter.Label(self, textvariable=self.labelVariable, anchor='w', fg='white', bg='blue')
		label.grid(column=0, row=1, columnspan=2, stick='EW')
		self.labelVariable.set(u"Hello !")

		self.grid_columnconfigure(0,weight=1)

		self.resizable(True, False)
		self.update()
		self.geometry(self.geometry())
		self.entry.focus_set()
		self.entry.selection_range(0, tkinter.END)

	def OnButtonClick(self):
		self.labelVariable.set( self.entryVariable.get()+" (You click the button)")
		print("You click the button!")
		self.entry.focus_set()
		self.entry.selection_range(0, tkinter.END)

	def OnPressEnter(self,event):
		self.labelVariable.set( self.entryVariable.get()+" (You pressed the enter!)")
		print("You pressed enter!")
		self.entry.focus_set()
		self.entry.selection_range(0, tkinter.END)

	def OnMouseClick(self):
		print("You Mouse Clicked")
		

if __name__ == "__main__":
	app = simpleapp_tk(None)
	app.title('My application')
	app.mainloop()