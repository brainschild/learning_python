#print message
message='BrainsChild'

print('Hello',message) #embodies string interpolation
print(len(message)) #prints the length of the String. HOw manay characters
print(message[7:12]) #prints the instance of the string from index 7 to index 12

print(message.lower()) #print string in lowercase
print(message.upper()) #prints String in UPPERCASE
print(message[0],message.count('b')) #takes the index character at [0] , counts how many instaces of M are n the string.
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
greetme = greeting +', '+ name+'. Welcome! using plus signs to add combine the Strings'
#second instance uses placeholders thus instigates the consruction of normal instance of how the senstence
#would appear then implores the use of .format which is feed with the Strings
greetme2 = '{}, {}. Welcome!'.format(greeting,name)
greetme3 = f'{greeting.upper()}, {name}. Welcome! Used F Strings' 
#F strings make is easier to write the variables within the placeholders and give functionality to add commands to the variables
print(greetme)
print(greetme2)
print(greetme3)

print(dir(name ))

#### RESULT OF print(dir(name )) ####
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', 
#'__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
#'__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__',
#'__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', 
#'__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', 
#'__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 
#'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
#'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
# 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join',
# 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 
#'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 
#'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# so the print(dir(name )) give a user all available commands that can work with the String "name"

# but does not explain what the function does to get what the commands associated with String or any element we use
#check the file in python folder for help commands

