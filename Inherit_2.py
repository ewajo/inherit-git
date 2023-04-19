from faker import Faker

class BaseContact:
    def __init__(self , name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    @property
    def label_length(self):
      return len(self.name)

    def contact(self): 
       print(f'Wybieram numer {self.phone} i dzwonię do {self.name}') 
    
class BusinessContact(BaseContact):
    def __init__(self, name, phone, email, company_position, company_name, company_number):
       super().__init__(name, phone, email)
       self.company_position = company_position
       self.company_name = company_name
       self.company_number = company_number
       
    def contact(self): 
       print(f'Wybieram numer służbowy {self.company_number} i dzwonię do {self.name}')  


def create_contacts(is_business, amount):
    fake = Faker()
    name = fake.name()
    phone = fake.msisdn()
    email = fake.email()
    company_position = fake.job()
    company_name = fake.company()
    company_number = fake.msisdn()
    

    list_of_contacts = []
    for i in range(amount):
        if is_business:
          card = BusinessContact(name, phone, email, company_position, company_name,company_number)
        else:
          card = BaseContact(name, phone, email)
        list_of_contacts.append(card)

    return list_of_contacts

create_contacts(1,1)
created_contacts = create_contacts(1,1)
for card in created_contacts:
    card.contact()

create_contacts(0,1)
created_contacts = create_contacts(0,1)
for card in created_contacts:
    card.contact()
