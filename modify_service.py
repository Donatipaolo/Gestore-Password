from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import variables


def modify_service() :

    def modifica_servizio() : 
        servizio_selezionato = str(combobox.get())
        new_email= str(entry1.get())
        new_pass = entry2.get()

        object = str
        for object2 in servizio_selezionato,new_email,new_pass : 
            if (variables.verifica_correttezza(object=object2) == False) : 
                return
        index = variables.listofservice.index(servizio_selezionato)
        new_file = variables.file.replace(variables.listofservice[index] +","+ variables.listofemail[index] + ","+ variables.listofpassword[index], servizio_selezionato + "," + new_email + "," + new_pass)  
        variables.new_service(new_file,1)
        entry1.delete(0,"end")
        entry2.delete(0,"end")
    
    def elimina_servizio(): 
        servizio_selezionato = str(combobox.get())
        index = variables.listofservice.index(servizio_selezionato)

        if (len(variables.listofservice) > 1) : 
            virgola = ','
        else :
            virgola = ''
        
        new_file = variables.file.replace(virgola + variables.listofservice[index] +","+ variables.listofemail[index] + ","+ variables.listofpassword[index], "")
        variables.new_service(new_file,1)
        messagebox.showinfo("info","il servizio e' stato eliminato correttamente")
        entry1.delete(0,"end")
        entry2.delete(0,"end")
        combobox['values'] = variables.listofservice
        
    modify_service_root = Tk()
    modify_service_root.geometry("400x250")
    modify_service_root.title("modifica servizio")
    modify_service_root.resizable(False,False)
    #impostazioni della finestra
    
    modify_service_root.columnconfigure(0,weight=1)
    modify_service_root.columnconfigure(1,weight=1)
    modify_service_root.rowconfigure(0,weight=4)
    modify_service_root.rowconfigure(1,weight=1)
    #impostazioni del layout
    
    mainframe = Frame(modify_service_root)
    mainframe.grid(column=0,row=0,columnspan=2)
    #mainframe principale
    
    global servizi
    name = StringVar()
    entry1str = StringVar()
    entry2str = StringVar()
    #variabili principali utilizzate
    
    combobox = ttk.Combobox(mainframe, textvariable=name)
    combobox['values'] = variables.listofservice
    combobox['state'] = 'readonly'
    
    label = Label(mainframe,text="seleziona il servizio che vuoi modificare : ",padx=60,pady=9)
    label1 = Label(mainframe,text="email",padx=60,pady=9)
    entry1 = Entry(mainframe,width=30,textvariable=entry1str)
    label2 = Label(mainframe,text="password",padx=60,pady=9)
    entry2 = Entry(mainframe,width=30,textvariable=entry2str)
    b_modify_service = ttk.Button(modify_service_root,text="modifica il servizio",command=modifica_servizio)
    b_stop = ttk.Button(modify_service_root,text="elimina servizio",command=elimina_servizio)
    #widget della finestra
    
    label.pack()
    combobox.pack(fill=X, padx=5,pady=5)
    label1.pack()
    entry1.pack()
    label2.pack()
    entry2.pack()
    b_modify_service.grid(column=0,row=1,padx=15)
    b_stop.grid(column=1,row=1,padx=15)
    #impostazione della pagina

    modify_service_root.mainloop()
    


