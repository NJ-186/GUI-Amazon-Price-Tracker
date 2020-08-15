from tkinter import *
from bot import AmazonBot
import send_mail
import time

root = Tk()

#Functions
def start_item():
    i=0
    while(i < int(days_text.get())):

        i+=1
        new_bot = AmazonBot()
        current_price = new_bot.start_scrape(link_text.get())
           
        if (float(current_price.replace(',','.')) < float(price_text.get())/1000):
           send_mail.mail(email_text.get(),link_text.get())

           #Alert
           alert_label = Label(root, text='Price Dropped! Mail Sent!!', font=('bold',14), pady=20)
           alert_label.place(x=110,y=320)
           break
        time.sleep(60*60*24)
        

def stop_item():
    exit()
    print('Killing tracking')

#Link
link_text = StringVar()
link_label = Label(root, text='Amazon Link', font=('bold',14), pady=20, padx=30)
link_label.grid(row=0,column=0, sticky='W') #sticky for sticking it to west 'W'
link_entry = Entry(root, textvariable=link_text)
link_entry.grid(row=0,column=1)

#Days
days_text = StringVar()
days_label = Label(root, text='No of Days', font=('bold',14), pady=20, padx=30)
days_label.grid(row=1,column=0, sticky='W') #sticky for sticking it to west 'W'
days_entry = Entry(root, textvariable=days_text)
days_entry.grid(row=1,column=1)

#Price
price_text = StringVar()
price_label = Label(root, text='Favourable Price', font=('bold',14), pady=20, padx=30)
price_label.grid(row=2,column=0, sticky='W') #sticky for sticking it to west 'W'
price_entry = Entry(root, textvariable=price_text)
price_entry.grid(row=2,column=1)


#Email
email_text = StringVar()
email_label = Label(root, text='Email ID', font=('bold',14), pady=20, padx=30)
email_label.grid(row=3,column=0, sticky='W') #sticky for sticking it to west 'W'
email_entry = Entry(root, textvariable=email_text)
email_entry.grid(row=3,column=1)

#Start Button
start_btn = Button(root, text='Start', width=12, command=start_item)
start_btn.grid(row=4,column=0,pady=30,padx=40)

#Stop Button
stop_btn = Button(root, text='Stop', width=12, command=stop_item)
stop_btn.grid(row=4,column=1,pady=30,padx=40)

root.title('Price Tracker')
root.geometry('410x380')

root.mainloop()

# Compile with Pyinstaller

# Windows
#pyinstaller --onefile --windowed part_manager.py

# Mac
#pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py

