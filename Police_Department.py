from tkinter import *
from tkinter.ttk import Combobox
from tkcalendar import Calendar

class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry('450x450')
        self.main_menu()

    def main_menu(self):
        self.main_frame = Frame(self.root)
        self.main_frame.pack(expand=True, fill='both')
        welcome_label = Label(self.main_frame, text="Welcome officer! \n Please choose an action:", font=("Arial", 14))
        welcome_label.pack(pady=20)
        query_button = Button(self.main_frame, text="Query Records", command=self.query_page, width=20, height=2)
        query_button.pack(pady=10)
        add_button = Button(self.main_frame, text="Add Records", command=self.add_page, width=20, height=2)
        add_button.pack(pady=10)
        edit_button = Button(self.main_frame, text="Edit Records", command=self.edit_page, width=20, height=2)
        edit_button.pack(pady=10)
        officers_button = Button(self.main_frame, text="Department officers", command=self.officers_page, width=20, height=2)
        officers_button.pack(pady=10)

    def pop_up(self):
        self.top = Toplevel(root)
        self.top.geometry('450x450')
        photo = PhotoImage(file="po-badge.ico")
        self.top.iconphoto(False, photo)

    def add_page(self):
        self.pop_up()
        self.top.title('Add record')
        name_label = Label(self.top, text="Name:")
        name_label.pack()
        self.name_entry = Entry(self.top, width=50, )
        self.name_entry.pack()
        ssn_label = Label(self.top, text="SSN:")
        ssn_label.pack()
        self.ssn_entry = Entry(self.top, width=50)
        self.ssn_entry.pack()
        address_label = Label(self.top, text="Address:")
        address_label.pack()
        self.address_entry = Entry(self.top, width=50)
        self.address_entry.pack()
        dob_label = Label(self.top, text="Date of Birth:")
        dob_label.pack()
        self.dob_calendar = Calendar(self.top)
        self.dob_calendar.pack()
        role_label = Label(self.top, text="Role:")
        role_label.pack()
        self.role_var = StringVar()
        self.role_menu = Combobox(self.top, textvariable=self.role_var, values=('Officer', 'Convict','Visitor' ), state='readonly')
        self.role_menu.pack()
        submit_button = Button(self.top, text="Submit", command=self.save_record, width=20, height=2)
        submit_button.pack(pady=20)


    def edit_page(self):
        self.pop_up()
        self.top.title('Edit record')
        ssn_label = Label(self.top, text="Enter SSN:")
        ssn_label.pack()
        self.ssn_entry = Entry(self.top, width=50)
        self.ssn_entry.pack()
        address_label = Label(self.top, text="Enter new address:")
        address_label.pack()
        self.address_entry = Entry(self.top, width=50)
        self.address_entry.pack()
        search_button = Button(self.top, text="Edit", command=self.edit, width=20, height=2,font=("Arial", 12))
        search_button.pack(pady=20)
        self.edit_result = Text(self.top, height=10, width=35)
        self.edit_result.pack(pady=10)

    def query_page(self):
        self.pop_up()
        self.top.title('Find record')
        ssn_label = Label(self.top, text="SSN:")
        ssn_label.pack()
        self.ssn_entry = Entry(self.top, width=50)
        self.ssn_entry.pack()
        query_button = Button(self.top, text="Query", command=self.query_records, width=20, height=2)
        query_button.pack(pady=20)
        result_label = Label(self.top, text="Result: ")
        result_label.pack()
        self.search_result = Text(self.top, height=10, width=50)
        self.search_result.pack(pady=10)
        # self.clear_frame(self.main_frame)

    def officers_page(self):
        self.pop_up()
        self.top.title('Find record')
        officers_label = Label(self.top, text="Available officers: ", font=("Arial", 14))
        officers_label.pack()
        self.search_result = Text(self.top, height=20, width=50, font=("Arial", 14))
        self.search_result.pack(pady=10)
        lst=[]
        mifi = open('records.txt', 'r')
        readed = mifi.readlines()
        mifi.close()
        for i in readed:
            data=i.split(",")
            if data[4]=="Officer":
                lst.append(i)
        for j in lst:
            data=j.split(",")
            self.search_result.insert(END,"  "+data[0]+"\n")

    def save_record(self):
        name = self.name_entry.get()
        ssn = self.ssn_entry.get()
        address = self.address_entry.get()
        dob = self.dob_calendar.get_date()
        role = self.role_var.get()
        myf=open('records.txt', 'a')
        myf.writelines(name+","+ssn+","+address+","+dob+","+role+",end"+"\n")
        myf.close()
        self.main_menu()

    def query_records(self):
        ssn=self.ssn_entry.get()
        myfi=open('records.txt','r')
        all=myfi.readlines()
        myfi.close()
        c=0
        for i in all:
            data=i.split(",")
            if ssn == data[1]:
                c=1
                self.search_result.insert(END, "Name: " + data[0] + "\n" + "SSN: " + data[1] + "\n")
                self.search_result.insert(END,"Address: " + data[2] + "\n" + "DOB: " + data[3] + "\n" + "Role: " + data[4])
        if c==0:
            self.search_result.insert(END,"User not Found")

    def edit(self):
        mifi=open('records.txt','r')
        readed=mifi.readlines()
        mifi.close()
        myfi=open('records.txt','w')
        ssn=self.ssn_entry.get()
        address=self.address_entry.get()
        c=0
        for i in readed:
            data=i.split(",")
            if ssn == data[1]:
                c=1
                data[2]=address
            line=','.join(data)
            myfi.write(line)
            self.edit_result.insert(END, "Edited successfully \n")
        if c==0:
            self.edit_result.insert(END,"User not Found \n")
        myfi.close()

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

root = Tk()
root.title('Police Department')
photo = PhotoImage(file = "po-badge.ico")
root.iconphoto(False,photo)
app = App(root)

root.mainloop()