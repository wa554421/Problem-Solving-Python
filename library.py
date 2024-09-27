# Library Function
class Library:
    def __init__(self,listofbooks):
        self.books=listofbooks
        
    def diplayavailablebooks(self):
        print("Books present in this library are:  ")
        for book in self.books:
            print(" * "+ book)
    
    def borrowbooks(self,bookname):
        
        if bookname in self.books:
            print(f"You have been issued {bookname}. Please Keep it safe and handle it properly and Return within 30 days.")
            self.books.remove(bookname)
        else:
            print("Sorry , This book is either not available in the library or hope so it has already issued by someone.PLease wait until it available then you borrow this.")
    
    def returnbooks(self,bookname):
        self.books.append(bookname)
        print("You Returned Book SuccesFully.")
            

class Student:
    def requestbook(self):
        self.book=input("Enter the name of the Book you want to boorow: ")
        return self.book
    
    def returnbook(self):
        self.book=input("Enter the name of the book you want to return or add: ")
        return self.book

centrallibrary=Library(["Algorithms","Hackers","Python",'Coding'])
student=Student()
while(True):
    welcomemsg='''\n ==== Welcome to Central Library ====
    Plaese Choose Option which you want:
    1. Listing all the Books
    2. Request the Books
    3. Return a Book
    4. Exit the library'''
    print(welcomemsg)
    a=int(input("Enter a Choice: "))
    if a==1:
        centrallibrary.diplayavailablebooks()
        
    elif a==2:
        centrallibrary.borrowbooks(student.requestbook())
        
    elif a==3:
        centrallibrary.returnbooks(student.returnbook())
        
    elif a==4:
        print("Thanks for choosing Central Library.Have a great day ahead!")
        exit()
    else:
        print("You Choose Wrong Option!")
    
    
