# using Python < 3.x...
import tkinter as tk
import math

class Application:
    ## creating application
    def __init__(self):
        # creating the main window
        self.root = tk.Tk()
        self.root.title("Some Labels, Some Colors")
        self.root.geometry("350x250+50+50")

        maximum = 10

        for row in range(maximum):
            # using a label as a container
            rowLabel = tk.Label(self.root)
            # no border
            rowLabel["borderwidth"] = 0
            rowLabel.pack(expand=tk.YES, side=tk.TOP, fill=tk.BOTH)
            R = (row+1) * 255 / maximum

            for col in range(maximum):
                B = (col+1) * 255 / maximum

                label = tk.Label(rowLabel)
                label["text"      ] = "Row:%d\nCol:%d" % (row+1, col+1)
                label["font"      ] = ("Courier", 8, "normal")
                label["background"] = "#%02x%02x%02x" % (R,200,B)
                label.pack(expand=tk.YES, side=tk.LEFT, fill=tk.BOTH)

                label.bind("<Enter>", self.onEnter)
                label.bind("<Leave>", self.onLeave)
                label.bind("<Button-1>", self.onClick)

    ## mouse is over a widget
    def onEnter(self, event):
        event.widget["relief"] = "raised"
    ## mouse is leaving a widget
    def onLeave(self, event):
        event.widget["relief"] = "flat"

    def onClick(self, event):
        print("%d %d"% (row, col))

    ## waiting for user action
    def mainloop(self):
        self.root.mainloop()

if __name__ == "__main__":
    application = Application()
    application.mainloop()