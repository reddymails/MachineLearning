'''
 Tuples are nothing mut arrays which are immutable , means you cant assign any value once initialized.
 Dictinary is just like java MAP
'''

def find_pe_pb(price, eps, book_volume) :
    pe = price /eps
    pb = price/book_volume
    # You can return both results at once.
    return pe, pb


pe_ratio, pb_ratio = find_pe_pb(100,2,4)
print(pe_ratio)
print(pb_ratio)


# Still a Tuple
contacts = [('Ram',9854666),('Raja',89765455),('Rob',8976543)]

for contact in contacts:
    #contact <=== each variable here will have name value pairs with element at zero being name and element at 1 being phone number.
    if contact[0] == 'Raja':
        print(contact[1])

# Dictionary (or MAP )
contacts_dictionary = {
    'rachel': 985683455,
    'rama': 89765455,
    'rob': 8976543
}

print('Rachel phone = '+ str(contacts_dictionary.get('rachel')))
print('Rama phone = '+ str(contacts_dictionary.get('rama')))
del contacts_dictionary['rachel']
print(contacts_dictionary)

# Dictionary within Dictionary (or MAP  of maps)
address_and_contacts_dictionary = {
    'rachel': {'phone': '9856835', 'email': 'rachel@gmaiil1.com','address':'123 fairview street, Texas '},
    'rama': {'phone': '123456', 'email': 'raml@gmaiil1.com','address':'423 long view Ave, Mass '},
    'rob': {'phone': '98765430', 'email': 'roy@gmaiil1.com','address':'1 Loop street , California '}
}
print(address_and_contacts_dictionary.get('rachel'))
#Both syntaxes work.
print(address_and_contacts_dictionary.get('rachel').get('phone'))
print(address_and_contacts_dictionary['rachel']['phone'])

print('items = '+ str(address_and_contacts_dictionary.items()))

# just will print Keys
for name in address_and_contacts_dictionary.keys():
    print(name)

# just will print Keys
for value in address_and_contacts_dictionary.values():
    print(value)

