class Book:

    def __init__(self,title, author):
        self.title = title
        self. author = author
        self.is_borrowed = False


    def borrow(self):
        self.is_borrowed = True
        print(self.title,"has been borrowed.")


    def return_book(self):

        self.is_borrowed = False
        print(self.title,"has been returned...")



Book1 = Book("Harry Porter" , "J.K. Rowling")
Book2 = Book("Tratina" , "M.D. Jafar Ikbal")
Book3 = Book("Dakhghor" , "Robindronath Thakur")

Book1.borrow()
Book1.return_book()

Book2.borrow()
Book2.return_book()

Book3.borrow()
Book3.return_book()