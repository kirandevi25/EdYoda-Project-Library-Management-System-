# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 21:30:54 2020

@author: Kiran Devi
"""

# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian

b1 = Book('Shoe Dog','Phil Knight', '2015',312)
b1.addBookItem('123hg','H1B2')
b1.addBookItem('124hg','H1B3')

b1.printBook()

catalog = Catalog()

b = catalog.addBook('Shoe Dog','Phil Knight', '2015',312)
catalog.addBookItem(b, '123hg','H1B2')
catalog.addBookItem(b, '123hg','H1B4')
catalog.addBookItem(b, '123hg','H1B5')

b = catalog.addBook('Moonwalking with Einstien','J Foer', '2017',318)
catalog.addBookItem(b, '463hg','K1B2')

#catalog.displayAllBooks()

m1 = Member("Vish","Bangalore",23,'asljlkj22','std1233')

librarian = Librarian("Awantik","Bangalore",34,'asljlkj22','zeke101') 
print (m1)
print (librarian)

b = catalog.searchByName('Shoe Dog')
print (b)

b = catalog.searchByAuthor('J Foer')
print (b)

m1.issueBook(catalog,'Shoe Dog')

#catalog.displayAllBooks()


m1.returnBook(catalog, 'Shoe Dog', '123hg' )

m1.returnBook(catalog, 'Shoe Dog', '52463' )

m1.returnBook(catalog, 'Shoe Dog', '15973' )


#catalog.displayAllBooks()

b = librarian.addBook(catalog,'English', 'J.P.Gupta' ,'2016','402')


librarian.addBookItemInCatalog(catalog, b, '1365fg', '45978')

#catalog.displayAllBooks()

librarian.removeBook(catalog,'Moonwalking with Einstien')

librarian.removeBookItemFromCatalog(catalog, 'Shoe Dog' ,'15973')

#catalog.displayAllBooks()

