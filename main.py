import qrcode
from tkinter import *
from tkinter import messagebox

def generate():
    text = msg.get()
    save_as = save_name.get()

    if not text:
        messagebox.showerror('Error', 'Please enter text or URL')
        return

    if not save_as:
        messagebox.showerror('Error', 'Please enter a file name')
        return

    img = qrcode.make(text)
    img.save(f'{save_as}.png')
    messagebox.showinfo('Success', 'File Saved!')

def show():
    text = msg.get()

    if not text:
        messagebox.showerror('Error', 'Please enter text or URL')
        return

    img = qrcode.make(text)
    img.show()

# Renamed 'cp' to 'app'
app = Tk()
app.title('QR Code Generator')
app.geometry('700x250')
app.config(bg='#e52165')

frame = Frame(app, bg='#e52165')
frame.pack(expand=True)

Label(frame, text='Enter the Text or URL:', font=('Arial Black', 16), bg='#e52165').grid(row=0, column=0, sticky='w')
msg = Entry(frame)
msg.grid(row=0, column=1)

Label(frame, text='File Name(Save As):', font=('Arial Black', 16), bg='#e52165').grid(row=1, column=0, sticky='w')
save_name = Entry(frame)
save_name.grid(row=1, column=1)

btn_show = Button(app, text='Show QR code', bd='5', command=show, width=15)
btn_show.pack()

btn_save = Button(app, text='Save QR code', command=generate, bd='5', width=15)
btn_save.pack()

app.mainloop()
