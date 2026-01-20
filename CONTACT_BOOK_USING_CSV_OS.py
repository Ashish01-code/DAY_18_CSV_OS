#!/usr/bin/env python
# coding: utf-8

# In[12]:


import os
import csv
class ContactBook:
    def __init__(self,filename):
        self.filename=filename
        self.contact={}
        self.load_contact()
    def load_contact(self):
        if not os.path.exists(self.filename):
            print("FILE NOT FOUND")
            return
        with open(self.filename,"r",newline="") as f:
            reader=csv.reader(f)
            next(reader,None)
            for row in reader:
                if row:
                    name,phone=row
                    self.contact[name]=phone
    def save_contact(self):
        file_exists=os.path.exists(self.filename)
        file_empty=(not file_exists) or os.path.getsize(self.filename)==0
        with open(self.filename,"w",newline="") as f:
            writer=csv.writer(f)
            if file_empty:
                writer.writerow(["NAME","PHONE"])
            for name,phone in self.contact.items():
                writer.writerow([name,phone])
    def get_valid_name(self):
        while True:
            name=input("ENTER NAME").strip()
            if name=="":
                print("NAME CANNOT BE EMPTY")
            else:
                return name
    def get_valid_phone(self):
        while True:
            phone =input("ENTER THE PHONE NUMBER: ").strip()
            if not phone.isdigit():
                print("PLEASE ENTER ONLY NUMBERS")
            elif len(phone)!=10:
                print("PHONE NUMBER MUST BE 10 DIGIT")
            else:
                return phone
    def add_contact(self):
        name=self.get_valid_name()
        if name in self.contact:
            print("CONTACT ALREADY EXISTS")
            return
        phone=self.get_valid_phone()
        self.contact[name]=phone
        self.save_contact()
        print("CONTACT ADDDED")
    def view_contact(self):
        if not self.contact:
            print("NO CONTACT FOUND")
            return
        print("---CONTACT LIST---\n")
        for name,phone in self.contact.items():
            print(f"NAME : {name} | PHONE : {phone}")
    def search_contact(self):
        name=input("ENTER NAME")
        if name in self.contact:
            print(f"FOUND {name} : {self.contact[name]}")
        else:
            print("NO SUCH CONTACT EXISTS")
    def delete_contact(self):
        name=input("ENTER NAME")
        if name not in self.contact:
            print("NO SUCH CONTACT EXIST")
            return
        del self.contact[name]
        self.save_contact()
        print("CONTACT DELETED")
    def count_contact(self):
        print("THE COUNT IS : ",len(self.contact))
    def update_contact(self):
        name= self.get_valid_name()
        if name not in self.contact:
            print("NO SUCH CONTACT")
            return
        phone=self.get_valid_phone()
        self.contact[name]=phone
        self.save_contact()
        print("CONTACT UPDATED")
    def open_contact(self):
        os.startfile(self.filename)
book = ContactBook("E:\TEST\CONTACT.csv")
while True:
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Count Contacts")
    print("6. Update contact")
    print("7. Open Contacts in Excel") 
    print("8. Exit")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Enter a valid number")
        continue
    if choice == 1:
        book.add_contact()
    elif choice == 2:
        book.view_contact()
    elif choice == 3:
        book.search_contact()
    elif choice == 4:
        book.delete_contact()
    elif choice == 5:
        book.count_contact()
    elif choice==6:
        book.update_contact()
    elif choice==7:
       book.open_contact()
    elif choice == 8:
        print("Exiting...")
        break
    else:
        print("Invalid choice")


# In[ ]:




