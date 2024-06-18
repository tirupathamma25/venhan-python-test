from datetime import datetime, timedelta
class Book:
    def __init__(self,title, author,membership_id):
        self.title = title
        self.author = author
        self.membership_id = membership_id
        
    def borrow_book(self):
        if len(self.membership_id) == 4 and self.membership_id.isdigit():
            
            due_date = datetime.now() + timedelta(days=14)
            print(f"{self.title} has been borrowed and is due back on {due_date.strftime('%Y-%m-%d')}")
        else:
            raise ValueError(f"{self.title} is not available for borrowing.")
            
    def return_book(self):
        if len(self.membership_id) == 4 and self.membership_id.isdigit():
            
            print(f"Thank you for returning {self.title}.")
        else:
            raise ValueError(f"{self.title} is not currently borrowed.")

        
    
b = Book("aaaa","Ram","1234")
b.borrow_book()
b.return_book()