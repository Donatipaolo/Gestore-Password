from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import newkeyservice
import variables


def cambia_chaive() :
    global key 
    finestre = Tk()
    finestre.withdraw()
    filepath = filedialog.askopenfilename(title="seleziona la chiave")
    variables.keypath = filepath
    with open(filepath, 'rb') as file:
            variables.key = file.read()
            


def cambia_database() :
    global database
    finestre = Tk()
    finestre.withdraw()
    variables.database = filedialog.askopenfilename(title="seleziona database")
    
    
    

        
def key_and_database():
    
    def aggiorna_dati():
                try : 
                    data = variables.database.split('/')
                    
                    
                    label0.config(text="database :" + str(data[len(data)-1]))
                except :
                    label0.config(text="database : None")
                try :
                    keydata = variables.keypath.split('/')

                    
                    label1.config(text="key : " + str(keydata[(len(keydata))-1]))
                except :
                    label1.config(text="key : None")
        
                
    
    
    
    key_and_database_root = Tk()
    key_and_database_root.title("key e database")
    key_and_database_root.geometry("400x225")
    key_and_database_root.resizable(False,False)
    #creazione e impostazioni finestra
    
    
    key_and_database_root.columnconfigure(1,weight=1)
    key_and_database_root.rowconfigure(0,weight=1)
    key_and_database_root.rowconfigure(1,weight=1)
    key_and_database_root.rowconfigure(2,weight=1)
    #impostazioni della griglia
    
    #variabili utilizzate
    
    
    
    label0 = Label(key_and_database_root,pady=20,padx=20)
    label1 = Label(key_and_database_root,pady=20,padx=20)
    b_modifica_database = ttk.Button(key_and_database_root,text="modifica database",command=lambda : (cambia_database(), aggiorna_dati()))
    b_modifica_key = ttk.Button(key_and_database_root,text="modifica key",command=lambda: (cambia_chaive(), aggiorna_dati()))
    b_new_key = ttk.Button(key_and_database_root,text="crea una nuova chiave",command= lambda: newkeyservice.new_key1())
    #widget utilizzati
    
    label0.grid(column=0,row=0)
    label1.grid(column=0,row=1)
    b_modifica_database.grid(column=1,row=0)
    b_modifica_key.grid(column=1,row=1)
    b_new_key.grid(column=0,row=2,columnspan=2)
    #gestione layout
        
    aggiorna_dati()
    
    key_and_database_root.mainloop()
    
