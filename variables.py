from cryptography.fernet import Fernet
from tkinter import messagebox

listofservice = []
listofemail = []
listofpassword = []
database = None
key = None
keypath = None
file = None

def leggi_dal_file() :  
    global file
    
    try :
        fernet = Fernet(key)
        with open(database, 'rb') as file1 : 
            encrypted_data = file1.read()
            decrypted_data = fernet.decrypt(encrypted_data)
            file = decrypted_data.decode()

        file = str(file)
        file1.close()

    except UnicodeDecodeError : 
        print("errore nella decodifica")
    except Exception as e:
        
        file = ""

def new_service(stringa,value):
    global file

    try :
        fernet = Fernet(key)
        
        if int(value) == 0:
            leggi_dal_file()
            fileaus = file
        else :
            fileaus = ""
        with open (database, 'wb') as file1 :
            stringa = fileaus + stringa
            stringa = fernet.encrypt(stringa.encode())

            file1.write(stringa)
            file1.close()

    except :
        pass

def verifica_correttezza(object) : 
    try : 
        str(object).index(" ")
        messagebox.showerror("errore","Errore: non possono essere presenti virgole o spazi")
        return False
    except :
        pass
    try: 
        str(object).index(",")
        messagebox.showerror("errore","Errore: non possono essere presenti virgole o spazi")
        return False
    except : 
        pass

    if (object == ""):
                messagebox.showerror("errore","Errore: elemento non valido")
                return False
    else : 
        return True