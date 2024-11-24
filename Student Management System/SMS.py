from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
from re import *

def save():
    con = None
    try:
        con = connect("arp.db")
        cursor = con.cursor()
        sql = "insert into student values(?, ?, ?, ?, ?)"
        
        # rno checking
        if aw_ent_rno.get() == "":
            showerror("rno issue", "u did not enter rno")
            aw_ent_rno.focus()
            return
        try:
            rno = int(aw_ent_rno.get())
        except ValueError:
            showerror("rno issue", "rno should be integers only")
            aw_ent_rno.delete(0, END)
            aw_ent_rno.focus()
            return

        if rno < 1:
            showerror("rno issue", "rno should be min 1")
            aw_ent_rno.delete(0, END)
            aw_ent_rno.focus()
            return
        
        name = aw_ent_name.get().strip()
        # name checking
        if name == "":
            showerror("rno issue", "u did not enter name")
            aw_ent_name.delete(0, END)
            aw_ent_name.focus()
            return

        name_pattern = compile("^[A-Za-z]+$")
        if not name_pattern.match(name):
            showerror("rno issue", "name shud be alphabets only")
            aw_ent_name.delete(0, END)
            aw_ent_name.focus()
            return

        try:
            sub1 = int(aw_ent_sub1.get())
            sub2 = int(aw_ent_sub2.get())
            sub3 = int(aw_ent_sub3.get())
        except ValueError:
            showerror("sub issue", "sub should be integers only")
            aw_ent_sub.delete(0, END)
            aw_ent_sub.focus()
            return
        if any(mark < 0 or mark > 100 for mark in [sub1,sub2,sub3]):
           showerror("marks issue","marks should be between 0 and 100")
           return
	
		
	

        cursor.execute(sql, (rno, name, sub1, sub2, sub3))
        con.commit()
        showinfo("success", "record created")
        aw_ent_rno.delete(0, END)
        aw_ent_name.delete(0, END)
        aw_ent_sub1.delete(0, END)
        aw_ent_sub2.delete(0, END)
        aw_ent_sub3.delete(0, END)
        aw_ent_rno.focus()
    except Exception as e:
        con.rollback()
        showerror("issue", e)
    finally:
        if con is not None:
            con.close()

def update():
    con = None
    try:
        con = connect("arp.db")
        cursor = con.cursor()
        sql = "update student set sub1 = ?, sub2 = ?, sub3 = ? where rno = ?"
        
        # rno checking
        if uw_ent_rno.get() == "":
            showerror("rno issue", "u did not enter rno")
            uw_ent_rno.focus()
            return
        try:
            rno = int(uw_ent_rno.get())
        except ValueError:
            showerror("rno issue", "rno should be integers only")
            uw_ent_rno.delete(0, END)
            uw_ent_rno.focus()
            return

        if rno < 1:
            showerror("rno issue", "rno should be min 1")
            uw_ent_rno.delete(0, END)
            uw_ent_rno.focus()
            return
        try:
            sub1 = int(uw_ent_sub1.get())
            sub2 = int(uw_ent_sub2.get())
            sub3 = int(uw_ent_sub3.get())
        except ValueError:
            showerror("Input issue", "All subject marks should be integers only")
            return
        
        
        cursor.execute(sql, (sub1, sub2, sub3, rno))
        if cursor.rowcount == 0:
            showerror("Update issue", "Rno does not exist")
        else:
            con.commit()

            showinfo("success", "record updated")
            uw_ent_rno.delete(0, END)
            uw_ent_sub1.delete(0, END)
            uw_ent_sub2.delete(0, END)
            uw_ent_sub3.delete(0, END)
            uw_ent_rno.focus()
    except Exception as e:
            con.rollback()
            showerror("issue", e)
    finally:
        if con is not None:
            con.close()

def delete():
    con = None
    try:
        con = connect("arp.db")
        cursor = con.cursor()
        sql = "delete from student where rno = ?"
        
        # rno checking
        if dw_ent_rno.get() == "":
            showerror("rno issue", "u did not enter rno")
            dw_ent_rno.focus()
            return
        try:
            rno = int(dw_ent_rno.get())
        except ValueError:
            showerror("rno issue", "rno should be integers only")
            dw_ent_rno.delete(0, END)
            dw_ent_rno.focus()
            return

        if rno < 1:
            showerror("rno issue", "rno should be min 1")
            dw_ent_rno.delete(0, END)
            dw_ent_rno.focus()
            return

        cursor.execute(sql, (rno,))
        if cursor.rowcount == 0:
            showerror("Delete issue", "Rno does not exist")
        else:
            con.commit()
            showinfo("success", "record deleted")
            dw_ent_rno.delete(0, END)
            dw_ent_rno.focus()
    except Exception as e:
        con.rollback()
        showerror("issue", e)
    finally:
        if con is not None:
            con.close()

def get():
    con = None
    try:
        con = connect("arp.db")
        cursor = con.cursor()
        sql = "select * from student"
        cursor.execute(sql)
        data = cursor.fetchall()
        info = ""
        for d in data:
            info += f"rno = {d[0]}, name = {d[1]}, sub1 = {d[2]}, sub2 = {d[3]}, sub3 = {d[4]}\n"
        return info
    except Exception as e:
        showerror("issue", e)
    finally:
        if con is not None:
            con.close()

def f1():
    aw.deiconify()
    mw.withdraw()

def f2():
    mw.deiconify()
    aw.withdraw()

def f3():
    vw.deiconify()
    mw.withdraw()
    info = get()
    vw_st_data.delete(1.0, END)
    vw_st_data.insert(INSERT, info)

def f4():
    mw.deiconify()
    vw.withdraw()

def f5():
    uw.deiconify()
    mw.withdraw()

def f6():
    mw.deiconify()
    uw.withdraw()

def f7():
    dw.deiconify()
    mw.withdraw()

def f8():
    mw.deiconify()
    dw.withdraw()

mw = Tk()
mw.title("S.M.S")
mw.geometry("800x600+200+50")
mw.configure(bg="#c99789")
f = ("Calibri", 30, "bold")

mw_btn_add = Button(mw, text="Add Student", font=f, width=14, command=f1, activebackground="#ffa472", fg="white", bg="#f7c297")
mw_btn_view = Button(mw, text="View Students", font=f, width=14, command=f3, activebackground="#ffa472", fg="white", bg="#f7c297")
mw_btn_update = Button(mw, text="Update Student", font=f, width=14, command=f5, activebackground="#ffa472", fg="white", bg="#f7c297")
mw_btn_delete = Button(mw, text="Delete Student", font=f, width=14, command=f7, activebackground="#ffa472", fg="white", bg="#f7c297")
mw_btn_add.pack(pady=5)
mw_btn_view.pack(pady=5)
mw_btn_update.pack(pady=5)
mw_btn_delete.pack(pady=5)

# Add Student Window
aw = Toplevel(mw)
aw.title("Add Student")
aw.geometry("800x600+200+50")
aw.configure(bg="#978d83")
aw_lab_rno = Label(aw, text="Enter Rno", font=f, bg="#978d83", fg="white")
aw_ent_rno = Entry(aw, font=f)
aw_lab_name = Label(aw, text="Enter Name", font=f, bg="#978d83", fg="white")
aw_ent_name = Entry(aw, font=f)
aw_lab_sub1 = Label(aw, text="Enter Sub1 Marks", font=f, bg="#978d83", fg="white")
aw_ent_sub1 = Entry(aw, font=f)
aw_lab_sub2 = Label(aw, text="Enter Sub2 Marks", font=f, bg="#978d83", fg="white")
aw_ent_sub2 = Entry(aw, font=f)
aw_lab_sub3 = Label(aw, text="Enter Sub3 Marks", font=f, bg="#978d83", fg="white")
aw_ent_sub3 = Entry(aw, font=f)
aw_btn_save = Button(aw, text="Save Student", font=f, command=save, activebackground="light green")
aw_btn_back = Button(aw, text="Back to Main", font=f, command=f2, activebackground="#eb6841")

# Grid layout
aw_lab_rno.grid(row=0, column=0, padx=10, pady=5, sticky="e")
aw_ent_rno.grid(row=0, column=1, padx=10, pady=5, sticky="w")
aw_lab_name.grid(row=1, column=0, padx=10, pady=5, sticky="e")
aw_ent_name.grid(row=1, column=1, padx=10, pady=5, sticky="w")
aw_lab_sub1.grid(row=2, column=0, padx=10, pady=5, sticky="e")
aw_ent_sub1.grid(row=2, column=1, padx=10, pady=5, sticky="w")
aw_lab_sub2.grid(row=3, column=0, padx=10, pady=5, sticky="e")
aw_ent_sub2.grid(row=3, column=1, padx=10, pady=5, sticky="w")
aw_lab_sub3.grid(row=4, column=0, padx=10, pady=5, sticky="e")
aw_ent_sub3.grid(row=4, column=1, padx=10, pady=5, sticky="w")
aw_btn_save.grid(row=5, column=0, padx=10, pady=5, sticky="e")
aw_btn_back.grid(row=5, column=1, padx=10, pady=5, sticky="w")
aw.withdraw()

# View Students Window
vw = Toplevel(mw)
vw.title("View Students")
vw.geometry("1200x600+200+50")
vw.configure(bg="#e8d174")
vw_st_data = ScrolledText(vw, font=f, width=90, height=10)
vw_btn_back = Button(vw, text="Back to Main", font=f, command=f4, activebackground="#eb6841")
vw_st_data.pack(pady=5)
vw_btn_back.pack(pady=5)
vw.withdraw()

# Update Student Window
uw = Toplevel(mw)
uw.title("Update Student")
uw.geometry("800x600+200+50")
uw.configure(bg="#006D5B")
uw_lab_rno = Label(uw, text="Enter Rno", font=f, bg="#006D5B", fg="white")
uw_ent_rno = Entry(uw, font=f)
uw_lab_sub1  = Label(uw, text="Enter Sub1 Marks", font=f,bg="#006D5B", fg="white")
uw_ent_sub1  = Entry(uw, font=f)
uw_lab_sub2  = Label(uw, text="Enter Sub2 Marks", font=f,bg="#006D5B", fg="white")
uw_ent_sub2  = Entry(uw, font=f)
uw_lab_sub3  = Label(uw, text="Enter Sub3 Marks", font=f,bg="#006D5B", fg="white")
uw_ent_sub3  = Entry(uw, font=f)

uw_btn_update = Button(uw, text="Update Student", font=f, command=update, activebackground="light green")
uw_btn_back = Button(uw, text="Back to Main", font=f, command=f6, activebackground="#eb6841")

uw_lab_rno.pack(pady=5)
uw_ent_rno.pack(pady=5)
uw_lab_sub1.pack(pady=5)
uw_ent_sub1.pack(pady=5)
uw_lab_sub2.pack(pady=5)
uw_ent_sub2.pack(pady=5)
uw_lab_sub3.pack(pady=5)
uw_ent_sub3.pack(pady=5)
uw_btn_update.pack(pady=5)
uw_btn_back.pack(pady=5)
uw.withdraw()

# Delete Student Window
dw = Toplevel(mw)
dw.title("Delete Student")
dw.geometry("800x600+200+50")
dw.configure(bg="#ffa472")
dw_lab_rno = Label(dw, text="Enter Rno", font=f, bg="#ffa472")
dw_ent_rno = Entry(dw, font=f)
dw_btn_delete = Button(dw, text="Delete Student", font=f, command=delete, activebackground="light green")
dw_btn_back = Button(dw, text="Back to Main", font=f, command=f8, activebackground="#eb6841")

dw_lab_rno.pack(pady=5)
dw_ent_rno.pack(pady=5)
dw_btn_delete.pack(pady=5)
dw_btn_back.pack(pady=5)
dw.withdraw()

mw.mainloop()
