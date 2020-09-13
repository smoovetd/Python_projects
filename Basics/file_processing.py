#with open('files/vegetables.txt', 'a') as myfile:
#    myfile.write('\nGarlic\n')
#    myfile.write('Pepper')  
    
             
              
with open('files/data.txt', 'a+') as crnt_file:
    crnt_file.seek(0)
    content = crnt_file.read()
    crnt_file.write('\n' + content)
    crnt_file.write('\n' + content)
    
