class BookSearch:
    
    def __init__(self):
        self.books = {}

    def is_available(self):
        return self.books
        
    def add_books(self,title,copies):
        self.books[title] = copies 
        
    def search_of_books(self,title):
        for name in self.books.keys():
            if name == title:
                return title
              
        
b = BookSearch()

b.add_books("The Guide",10)

b.add_books("Wings of Fire",20)

b.add_books("Ignited Minds", 14)

b.add_books("My Life", 40)

print(b.is_available())

print(b.search_of_books("The Guide"))

print(b.search_of_books("My Life"))

print(b.search_of_books("Anandmath"))