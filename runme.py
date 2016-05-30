import tkinter
from tkinter import *
from user import senderBtn
class GUI():
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('600x600')
        self.main_window.title('Personal Messenger Sender by Tyree Stevenson')
        self.label = tkinter.Label(self.main_window,  text='Personal Messenger Sender')
        self.promptRecipient = tkinter.Label(self.main_window, text='Enter Recipients UserName:')
        self.getRecipient = tkinter.Entry(self.main_window,width=10)
        self.promptMessage = tkinter.Label(self.main_window, text='Enter Message:')
        self.getMessage = tkinter.Entry(self.main_window, width=40)
        self.recipient = self.getRecipient.get()
        self.message = self.getMessage.get()
        self.sendButton = Button(self.main_window, text="Send Button", command=self.send)
        self.label.grid_configure(row=0,column=34)
        self.promptRecipient.grid_configure(row=100,column=28)
        self.getRecipient.grid_configure(row=100, column=34)
        self.promptMessage.grid_configure(row=200,column= 28)
        self.getMessage.grid_configure(row=200,column= 34)
        self.sendButton.grid_configure(row = 300, column =34)
        tkinter.mainloop()
    def send(self):
        self.recipient = self.getRecipient.get()
        self.message = self.getMessage.get()
        senderBtn(self.recipient,self.message)

def main():
    window = GUI()
if __name__ == '__main__':
    main()

























