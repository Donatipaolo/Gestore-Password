from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from database_e_key import *
from modify_service import modify_service
from new_service import create_service
from cryptography.fernet import Fernet
import variables



def update_all_data():
    global abc
    variables.leggi_dal_file()
    file = variables.file
    
    
    variables.listofservice = []
    variables.listofemail = []
    variables.listofpassword = []
    try :
        files = file.split(",")
        for i in range(0, len(files),3) :
            variables.listofservice.append(files[i])            
            variables.listofemail.append(files[i+1])
            variables.listofpassword.append(files[i+2])
        
    except : 
       pass 
        
    listbox.delete(0, 'end')  # Clear the existing items in the listbox
    for service in variables.listofservice:
        listbox.insert('end', service)
    
    try : 
        data = ""
        data = variables.database.split('/')
               
    except :
        pass
    try :
        keydata = ""
        keydata = variables.keypath.split('/')
            
    except :
        pass
    try : 
    
        label1.config(text="database : " + str(data[len(data)-1]) + "\nkey : " + str(keydata[(len(keydata))-1]))
    except : 
        pass
    root.after(1000, update_all_data)

def servizio():
    try : 
        service_index = listbox.curselection()
        
        if len(service_index) != 0:
            label0.config(text=variables.listofservice[int(service_index[0])]+ "\nemail : " + variables.listofemail[int(service_index[0])] + "\npassword : " + variables.listofpassword[int(service_index[0])])
    except :
        pass
    root.after(100, servizio)
    
root = Tk()
root.title("gestore password")
root.geometry("700x350")
root.resizable(False,False)
#creo e imposto la finestra

    
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
#impostazioni della griglia
    
frame1 = Frame(root)
frame2 = Frame(root)
frame1.grid(column=0,row=0,sticky="nswe")
frame2.grid(column=1,row=0,sticky="nswe")
#mainframe principali
    

#variabili utilizzate

label0 = Label(frame2,pady=20)  
label1 = Label(frame2,text="database : " + str(variables.database) + "\nkey : " + str(variables.key),pady=20)
b_new_service = ttk.Button(frame2,text="crea un nuovo servizio",width=30,command=create_service)
b_modify_service = ttk.Button(frame2,text="modifica un servizio",width=30,command=modify_service)
b_key_and_database = ttk.Button(frame2,text="modifica chiave o database",width=30,command=key_and_database)
listbox = Listbox(frame1,selectmode="single")
#widget utilizzati
    
label0.pack()
label1.pack()
b_new_service.pack(pady=20)
b_modify_service.pack(pady=20)
b_key_and_database.pack(pady=20)
listbox.pack(side=TOP,fill=BOTH,expand=True)
#impostazioni layout

update_all_data()
servizio()


root.mainloop()
