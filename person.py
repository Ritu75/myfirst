person={'name':'John', 'gender':'Male','age':45,'address':'Alpharetta','phone':4048517477}


info=input("Enter what information do you want to know about the person?").lower()
print(person.get(info,'Info not found'))

