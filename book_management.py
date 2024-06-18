class Book:
    def __init__(self):
        self.books = {}

    def add_new_book(self,title,author,ISBN,genre,quality):
        self.books["Name"] = title
        self.books["Author"] = author
        self.books["ISBN"] = ISBN
        self.books["Genre"] = genre
        self.books["quality"] = quality
        
    def update_book_info(self,genre):
        self.books["Genre"] = genre
        
    def remove_book_info(self,title,author,ISBN,genre,quality):
        del self.books["Name"]
        del self.books["Author"]
        del self.books["ISBN"]
        del self.books["Genre"]
        del self.books["quality"]

b = Book()

b.add_new_book("Wings of fire", "APJ Abdul Kalam","9788173711466","Autobiograpy",
"It gives us an understanding on his journey of success")

print(b.books)

b.add_new_book("Anandmath","Bakim Chandra Chatterjee","8188672130","Nationalist",
"It represents socio-cultural contexts and patronages")

print(b.books)

b.update_book_info("Inspirational Fiction")

print(b.books)

b.remove_book_info("Anandmath","Bakim Chandra Chatterjee","8188672130","Nationalist",
"It represents socio-cultural contexts and patronages")

print(b.books)
