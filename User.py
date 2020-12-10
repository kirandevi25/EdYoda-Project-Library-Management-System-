# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:31:10 2020

@author: Kiran Devi
"""

# -*- coding: utf-8 -*-

class User:
    def __init__(self, name, location, age, aadhar_id):
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        

class Member(User):
    def __init__(self,name, location, age, aadhar_id,student_id):
        super().__init__(name, location, age, aadhar_id)
        self.student_id = student_id
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.student_id
    
    #assume name is unique
    def issueBook(self, catalog, name, days=10):
        book = catalog.searchByName(name)
        if book == None:
            print("Book doesn't exist in library.")
        elif book.total_count == 0:
            print("Book not available. All books are issued.")
        else:
            isbn_num = book.book_item[1].isbn            
            catalog.removeBookItem(name, isbn_num)

    
    #assume name is unique
    def returnBook(self, catalog, name, isbn, rack='extra'):
        book = catalog.searchByName(name)
        if book == None:
            print("Book is different.")
        else:
            catalog.addBookItem(book,isbn,rack)

        
        
class Librarian(User):
    def __init__(self,name, location, age, aadhar_id,emp_id):
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id
        
    def __repr__(self):
        return self.name + ' ' + self.location + ' ' + self.emp_id
    
    def addBook(self,catalog,name,author,publish_date,pages):
        b = catalog.addBook(name,author,publish_date,pages)
        return b
    
    def removeBook(self,catalog,name):
        catalog.removeBook(name)
    
    def addBookItemInCatalog(self,catalog,book,isbn, rack = 'extra'):
        catalog.addBookItem(book,isbn,rack)

    
    def removeBookItemFromCatalog(self,catalog,name,isbn):
        catalog.removeBookItem(name,isbn)
    