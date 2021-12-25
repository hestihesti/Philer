import os

print('############################################################################################ \n')
print(' \n')
print('                                                                         \n')
print(' xxxxxxxxxx     xx            xx    xx                 xxxxxx            \n')
print(' xx      xxx    xx            xx    xx                 xx  xxxx          \n')
print(' xx       xxx   xx            xx    xx                 xx    xxxx        \n')
print(' xx        xxx  xx            xx    xx                 xx      xxxx      \n')
print(' xx        xxx  xx            xx    xx                 xx        xxx     \n')
print(' xx       xxx   xx            xx    xx                 xx        xxx     \n')
print(' xx      xxx    xx            xx    xx                 xx       xxx      \n')
print(' xx     xx      xx            xx    xx                 xx      xxx       \n')
print(' xxxxxxx        xxxxxxxxxxxxxxxx    xx                 xx     xxx        \n')
print(' xx             xxxxxxxxxxxxxxxx    xx                 xx   xxx          \n')
print(' xx             xx            xx    xx                 xxxxxxx           \n')
print(' xx             xx            xx    xx                 xx   xxxx         \n')
print(' xx             xx            xx    xx                 xx      xxx       \n')
print(' xx             xx            xx    xx                 xx       xxx      \n')
print(' xx             xx            xx    xx                 xx         xxx    \n')
print(' xx             xx            xx    xx                 xx          xxx   \n')
print(' xx             xx            xx    xxxxxxxxxxxxxx     xx            xxx \n')
print(' xx             xx            xx    xxxxxxxxxxxxxxxxx  xx             xxx\n')
print('                                                                                 \n')
print('///////////////////////////////////////////////////////////////////////////////  \n')
print('//////////////////////////////////////////////////////////////////////////////   \n')
print(' \n')
print('                         Welcome to profiler! \n')
print(' \n')
print(' \n')
print('########################################################################################### \n') 


ProfileName = input("Name the person you're trying to profile: ")
dob = input('Whens the date of birth: ')
email = input('What is the email this person uses: ')
user = input('What is the username commonly used: ')
phone = input('What is a phone number he/she uses: ')
lives = input('Where does this person live: ')
school = input('What high school did they go to: ')
college = input('If they went to college, which one did they attend: ')
mother = input('What is the mothers name: ')
father = input('What is the fathers name: ')
siblings = input('Do they have siblings? If so what are their names and age (seperate with comma): ')
pets = input('What are the names of their pets: ')
IP = input('Known IP address: ')
passwords = input('What are some passwords you managed to recover with what site (ex. (John Doe)Circlecircle. . =facebook, (HappyCamper331)lowkeyyBUTT2>

with open(os.path.join('/path/to/Philer/proPhiles', ProfileName), 'w') as f:
        f.write(ProfileName + '\n'),
        f.write('dob: ' + dob + '\n'),
        f.write('email: ' + email + '\n'),
        f.write('user: ' + user + '\n'),
        f.write('phone: ' + phone + '\n'),
        f.write('City lives in: ' + lives + '\n'),
        f.write('high school: ' + school + '\n'),
        f.write('college: ' + college + '\n'),
        f.write('mothers name: ' + mother + '\n'),
        f.write('fathers name: ' + father + '\n'),
        f.write('siblings: ' + siblings + '\n'),
        f.write('pets: ' + pets + '\n'),
        f.write('IP address: ' + IP + '\n'),
        f.write('passwords: ' + passwords + '\n'),
