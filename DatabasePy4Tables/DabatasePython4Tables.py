class Table:
    def __init__(self):
        self.table = {}

    def insertData(self, data):
        self.table[data.id] = data

    def getRegById(self, id):
        return self.table.get(id)
    
class People:
    def __init__(self, id, name, idCity, idContact, idCountry):
        self.id = id
        self.name = name
        # self.gender = gender
        self.idCity = idCity
        self.idContact = idContact
        self.idCountry = idCountry

class Cities: 
    def __init__(self, id, cityName):
        self.id = id
        self.cityName = cityName

class Contacts:
    def __init__(self, id, phone, email):
        self.id = id
        self.phone = phone
        self.email = email

class Country:
    def __init__(self, id, countryName):
        self.id = id
        self.countryName = countryName


def main():
    peopleTable = Table()
    citiesTable = Table()
    contactsTable = Table()
    countryTable = Table()

    for i in range(1, 11):
        country = Country(i, f"Country {i}")
        countryTable.insertData(country)

    for i in range(1,11):
        cities = Cities(i, f"Cities {i}")
        citiesTable.insertData(cities)

    for i in range(1,11):
        contact = Contacts(i, f"0000-000{i}", f"email{i}@email.com")
        contactsTable.insertData(contact)

    for i in range(1,11):
        people = People(i, f"Nome {i}", i, i, i) 
        # Repetindo indice pois estou usando um "factory" para gerar cadastros
        peopleTable.insertData(people)

    print("-"*50 + "\tPessoas\t\t" + "-"*50)
    for i in range(1, 11):
        peoplef = peopleTable.getRegById(i)
        cityf = citiesTable.getRegById(i)
        contactf = contactsTable.getRegById(i)
        countryf = countryTable.getRegById(i)

        if peoplef is not None:
            print(f"{peoplef.id}\t|\t"
                    f"{peoplef.name}\t|\t" 
                    f"{contactf.phone}\t|\t" 
                    f"{contactf.email}\t|\t"
                    f"{cityf.cityName}\t|\t"
                    f"{countryf.countryName}")
                    
                    

if __name__ == '__main__':
    main()




























