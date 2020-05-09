#!/home/jalexander/anaconda3/bin/python3
from tkinter import *
import os
import sys

#IMPORT BACKEND FUNCTIONS FROM FOLDER.
#This is OS independant.
path_to_client_functions = os.path.join(os.path.abspath(".."),"client_backend")
sys.path.insert(1,path_to_client_functions)
import client_functions


window=Tk()
window.title("NO NEW FRIENDS")



#Title to displace which user the chat window is with.
dst_user = Label(window,text="Chat with Server")

#Window to displace chat histor
chat_window = Listbox(window,height=6,width=40)
chat_window_scrollbar = Scrollbar(window)
chat_window_scrollbar.configure(command=chat_window.yview)



#Entry for chat text
text_input = Entry(window,width=40,bg="#d9dbde")

def button_click_send_button():
    messsage = text_input.get()
    client_functions.send_message(messsage,"190.213.190.195",65434,chat_window)


send_button = Button(window,text="SEND",bg="green",command=button_click_send_button)



# GRID POSITIONING
dst_user.grid(row=0,column=0,columnspan=4)
chat_window.grid(row=1,column=0,columnspan=4)
chat_window_scrollbar.grid(row=1,column=4)
text_input.grid(row=2,column=0,columnspan=4,ipady=15)
send_button.grid(row=3,column=0,columnspan=4)

window.mainloop()
