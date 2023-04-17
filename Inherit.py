class Vc:
    def __init__(self,first_name,surname,company,occupation,email):
        self.first_name=first_name
        self.surname=surname
        self.company=company
        self.occupation=occupation
        self.email=email
        self._label_length=0
    @property
    def label_length(self):
      return len(self.first_name) + len(self.surname)
    
    def contact(self):
        print (f"Kontaktuję się z {self.first_name} {self.surname} {self.occupation} {self.email}")
           

class Basecontact(Vc):
    def __init__(self, priv_tel, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.priv_tel = priv_tel
    
    @property
    def label_lenght(self):
      return len(self.first_name) + len(self.surname)
    
    def contacting(self):
        print (f"Wybieram {self.priv_tel} i dzwonię do {self.first_name} {self.surname}")

    


class Businesscontact(Vc):
    def __init__(self, comp_tel, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.comp_tel = comp_tel
      
    @property
    def label_lenght(self):
      return len(self.first_name) + len(self.surname)
      

    def contact(self):
      print (f"Wybieram {self.comp_tel} i dzwonię do {self.first_name} {self.surname}")

Kajetan= Basecontact(first_name="Kajetan", surname="Sokołowski",company="Polpark",occupation="web writer", email="ksokolowski@wp.pl",priv_tel= "123")
Adam = Basecontact(first_name="Adam", surname="Karnowski",company="Flixcar", occupation="HR Manager", email="akarnowski@gmail.com",priv_tel= "123")
Ewa= Basecontact(first_name="Ewa", surname="Rawicz", company="Taxlist", occupation="Tax Advisor", email="erawicz@gmail.com",priv_tel= "123")
Anna= Basecontact(first_name="Anna", surname="Biedrzycka",company="Abakuss",occupation="Księgowa", email="a.biedrz@outlook.com",priv_tel= "123")
Piotr= Basecontact(first_name="Piotr",surname="Kowal",company="Collar",occupation="Sales Manager",email="piotrkowal@collar.eu",priv_tel= "123")

Kajetan.contact()
Adam.contact()
Ewa.contact()
Anna.contact()
Piotr.contact()

Kajetan.label_length
Adam.label_length
Ewa.label_length
Anna.label_length
Piotr.label_length

Kajetan= Businesscontact(first_name="Kajetan", surname="Sokołowski",company="Polpark",occupation="web writer", email="ksokolowski@wp.pl",comp_tel= "456")
Adam = Businesscontact(first_name="Adam", surname="Karnowski",company="Flixcar", occupation="HR Manager", email="akarnowski@gmail.com",comp_tel= "456")
Ewa= Businesscontact(first_name="Ewa", surname="Rawicz", company="Taxlist", occupation="Tax Advisor", email="erawicz@gmail.com",comp_tel= "456")
Anna= Businesscontact(first_name="Anna", surname="Biedrzycka",company="Abakuss",occupation="Księgowa", email="a.biedrz@outlook.com",comp_tel= "456")
Piotr= Businesscontact(first_name="Piotr",surname="Kowal",company="Collar",occupation="Sales Manager",email="piotrkowal@collar.eu",comp_tel= "456")

Kajetan.contact()
Adam.contact()
Ewa.contact()
Anna.contact()
Piotr.contact()

print(Kajetan.label_length)
print(Adam.label_length)
print(Ewa.label_length)
print(Anna.label_length)
print(Piotr.label_length)

