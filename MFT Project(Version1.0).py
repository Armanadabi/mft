from tkinter import *
import os
import json
#main screen
def main_account_screen():
    global txt
    #main screen
    main_screen = Tk()
    main_screen.geometry("300x370")
    main_screen.title("MFT Project  v1.0 ")
 
    #label choose submit or login
    Label(text="Choose Login Or Submit", bg="pink", width="300", height="1", font=("Arial Black", 15,'bold')).pack() 
    Label(text="").pack() 
 
    #login button
    Button(text="Login", height="2", width="30",command=login_screen).pack() 
    Label(text="").pack() 
 
    #submit button
    Button(text="Submit", height="2", width="30",command=submit_screen).pack()
    Label(text="").pack()
    
    
    #delete button
    Button(text="Delete", height="2", width="30",command=delete_screen).pack()
    Label(text="").pack()
    
    
    #exit button
    Button(text="Exit", height="2", width="30",command=main_screen.destroy).pack()
    Label(text="").pack()
    
    #delete file button
    Button(text="Delete File(Admins Only)", height="2", width="30",bg='red',command=delete_file_screen).pack()
    txt=Label(text='')
    txt.pack()
    
    main_screen.mainloop()
#login screen
def login_screen():
    #globalize 
    global usr_entry
    global pw_entry
    global msg_lbl
    
    #login screen
    login_screen = Toplevel()
    login_screen.geometry("300x150")
    login_screen.title("Login")
    
    #username label and entry
    Label(login_screen,text='Username:').pack()
    usr_entry=Entry(login_screen,)
    usr_entry.pack()
    
    #password label and entry
    Label(login_screen,text='Password:').pack()
    pw_entry=Entry(login_screen,show='*')
    pw_entry.pack()
    
    
    #message label and login button
    msg_lbl=Label(login_screen,text='')
    msg_lbl.pack()
    Button(login_screen,text="Login", height="1", width="5",command=verify_login).pack()
#verify login
def verify_login():
    global login_yes_btn
    global error_login_screen
    try:
        u=usr_entry.get()
        p=pw_entry.get()
        with open('users.json') as j:
            s=json.load(j)
        if u in s:
            if s[u]==p:
                msg_lbl.configure(text='Welcome',fg='green')
            else:
                msg_lbl.configure(text='Wrong Username Or Password!',fg='red')
        else:
            msg_lbl.configure(text='Wrong Username Or Password!',fg='red')
    except FileNotFoundError:
        #error box
        error_login_screen = Toplevel()
        error_login_screen.geometry("300x105")
        error_login_screen.title("File Not Find!")
        
        # json msg
        Label(error_login_screen,text='Users.json Not Find! Do You Want To Create One?',fg='purple').pack()
        
        
        
        #yes and no buttons
        login_yes_btn=Button(error_login_screen,text='Yes',width=7,command=Create_json)
        login_yes_btn.place(x=150,y=74)
        
        login_no_btn=Button(error_login_screen,text='No',width=7,command=error_login_screen.destroy)
        login_no_btn.place(x=90,y=74)
#submit screen
def submit_screen():
    #globalize
    global usr_entry_submit
    global pw_entry_submit
    global msg_lbl_submit
    
    #submit screen
    submit_screen = Toplevel()
    submit_screen.geometry("300x150")
    submit_screen.title("SUBMIT")
    
    #username label and entry
    Label(submit_screen,text='Username:').pack()
    usr_entry_submit=Entry(submit_screen,)
    usr_entry_submit.pack()
    
    #password label and entry
    Label(submit_screen,text='Password:').pack()
    pw_entry_submit=Entry(submit_screen,show='*')
    pw_entry_submit.pack()
    
    
    #message label and submit button
    msg_lbl_submit=Label(submit_screen,text='')
    msg_lbl_submit.pack()
    Button(submit_screen,text="SUBMIT", height="1", width="5",command=submit_user).pack()
#submit user
def submit_user():
    try:
        u=usr_entry_submit.get()
        p=pw_entry_submit.get()
        with open('users.json') as j:
            s=json.load(j)
        if u not in s:
            s[u]=p
            with open('users.json','w') as j:
                json.dump(s,j)
            msg_lbl_submit.configure(text='Registered',fg='green')
        else:
            msg_lbl_submit.configure(text='Username Already Exist',fg='red')
    except FileNotFoundError:
        global yes_btn
        global error_screen
        #error box
        error_screen = Toplevel()
        error_screen.geometry("300x105")
        error_screen.title("File Not Find!")
        
        # json msg
        Label(error_screen,text='Users.json Not Find! Do You Want To Create One?',fg='purple').pack()
        
        
        
        #yes and no buttons
        yes_btn=Button(error_screen,text='Yes',width=7,command=Create_json)
        yes_btn.place(x=150,y=74)
        
        no_btn=Button(error_screen,text='No',width=7,command=error_screen.destroy)
        no_btn.place(x=90,y=74)

#create json 
def Create_json():
    try:
        dct={'farhan':'b1390'}
        with open('users.json','w') as j:
            json.dump(dct,j)
        error_screen.destroy()
    except NameError:
        error_login_screen.destroy()
    finally:
        error_screen_delete.destroy()
def delete_screen():
    global msg_lbl_delete
    global usr_entry_delete
    global pw_entry_delete
    #delete screen
    delete_screen = Toplevel()
    delete_screen.geometry("300x150")
    delete_screen.title("Delete Account")
    
    
    #username label and entry
    Label(delete_screen,text='Username:').pack()
    usr_entry_delete=Entry(delete_screen,)
    usr_entry_delete.pack()
    
    #password label and entry
    Label(delete_screen,text='Password:').pack()
    pw_entry_delete=Entry(delete_screen,show='*')
    pw_entry_delete.pack()
    
    
    #message label and delete button
    msg_lbl_delete=Label(delete_screen,text='')
    msg_lbl_delete.pack()
    del_btn=Button(delete_screen,text="DELETE", height="1", width="5",command=delete_user)
    del_btn.pack()
#delete user
def delete_user():
    try:
        u=usr_entry_delete.get()
        p=pw_entry_delete.get()
        with open('users.json') as j:
            s=json.load(j)
        if u in s:
            if s[u]==p:
                s.pop(u)
                with open('users.json','w') as j:
                    json.dump(s,j)
                msg_lbl_delete.configure(text='Account Deleted Successfully',fg='green')
            else:
                msg_lbl_delete.configure(text='Wrong Username Or Password!',fg='red')
        else:
            msg_lbl_delete.configure(text='Wrong Username Or Password!',fg='red')
    except FileNotFoundError:
        #globalize
        global yes_btn_delete
        global error_screen_delete
        #error box
        error_screen_delete = Toplevel()
        error_screen_delete.geometry("300x105")
        error_screen_delete.title("File Not Find!")
        
        # json msg
        Label(error_screen_delete,text='Users.json Not Find! Do You Want To Create One?',fg='purple').pack()
        
        
        #yes and no buttons
        yes_btn_delete=Button(error_screen_delete,text='Yes',width=7,command=Create_json)
        yes_btn_delete.place(x=150,y=74)
        
        no_btn=Button(error_screen_delete,text='No',width=7,command=error_screen_delete.destroy)
        no_btn.place(x=90,y=74)
def delete_file_screen():
    #globalize
    global delete_file_screen
    global usr_entry_delete_file
    global pw_entry_delete_file
    global msg_lbl_delete_file
    #delete file screen
    delete_file_screen = Toplevel()
    delete_file_screen.geometry("300x150")
    delete_file_screen.title("Delete Save File")
    
    
    #username label and entry
    Label(delete_file_screen,text='Username:').pack()
    usr_entry_delete_file=Entry(delete_file_screen,)
    usr_entry_delete_file.pack()
    
    #password label and entry
    Label(delete_file_screen,text='Password:').pack()
    pw_entry_delete_file=Entry(delete_file_screen,show='*')
    pw_entry_delete_file.pack()
    
    
    #message label and delete button
    msg_lbl_delete_file=Label(delete_file_screen,text='')
    msg_lbl_delete_file.pack()
    Button(delete_file_screen,text="DELETE", height="1", width="5",command=verify_admin).pack()
def verify_admin():
    u=usr_entry_delete_file.get()
    p=pw_entry_delete_file.get()
    if u=='admin':
        if p=='admin':
            verify_delete_file()
    else:
        msg_lbl_delete_file.configure(text='You Are Not An Admin!',fg='red')
def verify_delete_file():
    #globalize
    global verify_delete_file_screen
    #screen
    verify_delete_file_screen = Toplevel()
    verify_delete_file_screen.geometry("300x105")
    verify_delete_file_screen.title("Delete File")
    
    # json msg
    Label(verify_delete_file_screen,text='With This Option All Data Will Be Lost Are You Sure ?',fg='purple').pack()
    
    
    #yes and no buttons
    verify_yes_btn=Button(verify_delete_file_screen,text='Yes',width=7,command=delete_file_yes)
    verify_yes_btn.place(x=150,y=74)
    
    verify_no_btn=Button(verify_delete_file_screen,text='No',width=7,command=destroy_screen)
    verify_no_btn.place(x=90,y=74)
    
def destroy_screen():
    verify_delete_file_screen.destroy()
    delete_file_screen.destroy()
def delete_file_yes():
    try:
        os.remove('users.json')
        txt.configure(text='json file deleted',fg='green')
        destroy_screen()
    except FileNotFoundError:
        destroy_screen()
        txt.configure(text='json file Not Exist',fg='red')

main_account_screen()