from tkinter import *
from tkinter import ttk
from cryptography.fernet import Fernet
from tkinter import messagebox
import variables


def new_key1() : 
    
    def create_new_key():
        filename = entry1.get()
        
        try : 
            filename.index("/")
            print("non ci possono essere /")
            return
        except: 
            pass

        
        try : 
            nuova_chiave = Fernet.generate_key()

            with open (filename, 'wb') as file :   
                file.write(nuova_chiave)

            entry1.delete(0,"end")
        except PermissionError: 
            messagebox.showerror("errore"," PermissionError :  avviare il programma in modalita amministratore")
        except :
            print("un altro tipo di errore")



    new_key_root = Tk()
    new_key_root.title("crea una nuova chiave")
    new_key_root.geometry("400x150")
    new_key_root.resizable(False,False)
    #impostazioni della finestra

    new_key_root.columnconfigure(0,weight=1)
    new_key_root.rowconfigure(0,weight=1)
    #impostazioni della griglia

    frame = Frame(new_key_root)
    #frame principale

    entry1str = StringVar()
    #vafiabili utilizzate

    label0 = Label(frame,text="inserisci il nome della chiave da creare")
    entry1 = Entry(frame,textvariable=entry1str,width=35)
    button0 = ttk.Button(frame,text="crea la chiave",command=create_new_key)
    #widget

    frame.grid(row=0,column=0,sticky="nswe")
    label0.pack(pady=10)
    entry1.pack(pady=10)
    button0.pack(pady=10)
    #packing della finestra

    new_key_root.mainloop()
