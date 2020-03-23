month=('January','February','March','April','May','June','July','August','September','October','November','December')

birth_date=input('Enter your date of birth in dd-mm-yyyy format:')

print('Your birth month is:',month[int(birth_date[3:5])-1])
