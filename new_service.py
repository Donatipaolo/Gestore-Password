from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import variables

def create_service():

    def scrivi_nel_file():
        oggetti = []
        oggetti.append(str(entry1.get()))
        oggetti.append(str(entry2.get()))
        oggetti.append(str(entry3.get()))
        
        for object in oggetti :
            if (variables.verifica_correttezza(object=object) == False) : 
                return
  
        try : 
            variables.listofservice.index(oggetti[0])
            messagebox.showerror("impossibile creare il servizio", "il servizio e' gia esistente")
            return
        except : 
            if (variables.file == "") : 
                virgola = ""
            else :
                virgola= ","

            new_stringa = virgola + oggetti[0] + "," + oggetti[1] + "," + oggetti[2]
            variables.new_service(new_stringa,0)
            entry1.delete(0,"end")
            entry2.delete(0,"end")
            entry3.delete(0,"end")
            
        
    create_service_root = Tk()
    create_service_root.title("crea un servizio")
    create_service_root.geometry("400x250")
    create_service_root.resizable(False,False)
    #creazione e impostazioni finestra
    
    create_service_root.columnconfigure(0,weight=1)
    create_service_root.columnconfigure(1,weight=1)
    create_service_root.rowconfigure(0,weight=4)
    create_service_root.rowconfigure(1,weight=1)
    #configurazione della griglia
    
    mainframe = Frame(create_service_root)
    mainframe.grid(column=0,row=0,columnspan=2)
    #mainframe principale
    
    entry1str = StringVar()
    entry2str = StringVar()
    entry3str = StringVar()
    #variabili utilizzate
    
    b_create_service = ttk.Button(create_service_root,text="crea un nuovo servizio",command=scrivi_nel_file)
    b_stop = ttk.Button(create_service_root,text="annulla",command=lambda : create_service_root.destroy())
    label0 = Label(mainframe,text="nome servizio",pady=10)
    label1 = Label(mainframe,text="email",pady=10)
    label2 = Label(mainframe,text="password",pady=10)
    entry1 = Entry(mainframe,width=30,textvariable=entry1str)
    entry2 = Entry(mainframe,width=30,textvariable=entry2str)
    entry3 = Entry(mainframe,width=30,textvariable=entry3str,)
    #widget utilizzati
    
    b_create_service.grid(column=0,row=1)
    b_stop.grid(column=1,row=1)
    label0.pack()
    entry1.pack()
    label1.pack()
    entry2.pack()
    label2.pack()
    entry3.pack()
    #gestione del layout
    
    create_service_root.mainloop()

