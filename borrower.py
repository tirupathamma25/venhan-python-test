class Borrower:
    def __init__(self):
        self.persons = {}
      
    def add_new_borrower(self,name,contact_details,membership_id):
        self.persons["Name"] = name
        self.persons["Contact Details"] = contact_details
        self.persons["Membership ID"] = membership_id
        
    def update_borrower_info(self,name,contact_details,membership_id):
        self.persons["Name"] = name
        self.persons["Contact Details"] = contact_details
        self.persons["Membership ID"] = membership_id
        
    def remove_borrower(self,name,contact_details,membership_id):
        del self.persons["Name"]
        del self.persons["Contact Details"] 
        del self.persons["Membership ID"]
       
        
        
b = Borrower()

b.add_new_borrower("Ram","8787289837","avd123")
print(b.persons)

b.add_new_borrower("Nandhana","8765442243","kjw231")
print(b.persons)

b.add_new_borrower("Vijay","8765125432","juw230")
print(b.persons)

b.update_borrower_info("Nandhana","9182565231","opi098")
print(b.persons)

b.remove_borrower("Vijay","8765125432","juw230")
print(b.persons)
               
