def greet_person(person_name):
    titled_name = person_name.title()
    print(titled_name)
    print(type(titled_name))
    return 'Hi %s' % titled_name

user_name = input('Enter username:')    
print(greet_person(user_name))