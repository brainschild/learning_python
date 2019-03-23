#print message
message='BrainsChild'

print('Hello',message) #embodies string interpolation
print(len(message)) #prints the length of the String. HOw manay characters
print(message[7:12]) #prints the instance of the string from index 7 to index 12

print(message.lower()) #print string in lowercase
print(message.upper()) #prints String in UPPERCASE
print(message[0],message.count('b')) #takes the index character at 0 , counts how many instaces of M are n the string.
print(message[1],message.count('r'))
print(message[2],message.count('a'))
print(message[3],message.count('i'))
print(message[4],message.count('n'))
print(message[5],message.count('s'))
print(message.find('Chi')) # finds the starting index value of character in the String
print(message) 

replace_message = message.replace('Brains','Benta') #replace the word Martin then assigns the output to a variable or an instances of itself
print(replace_message)

greeting = 'Hello'
name = 'Benta'
#appends both String to form a Sentence/String... there is use of (+) and String spaces and commas. Gets complicated with more inclusions of Strings
greetme = greeting +', '+ name+'. Welcome! NOT'
#second instance uses placeholders thus instigates the consruction of normal instance of how the senstence
#would appear then implores the use of .format which is feed with the Strings
greetme2 = '{}, {}. Welcome!'.format(greeting,name)
greetme3 = f'{greeting.upper()}, {name}. Welcome! Used F Strings' 
#F strings make is easier to write the variables within the placeholders and give functionality to add commands to the variables
print(greetme)
print(greetme2)
print(greetme3)

