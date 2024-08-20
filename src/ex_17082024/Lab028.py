#Escape sequence

print("Hello World")
print("Hello\nWorld")  #\n - New line
print("Hello\tWorld")  #\t - tab line
print("Hello\bWorld")  #\b - backspace

#dir = 'C:\suji\n.txt'
#dir = "C:\suji\n.txt"
dir = r"C:\suji\n.txt" #we can user "r" raw string to avoid the conversions in escape sequence
dir2 = r'C:\suji\n.txt'
# r concept will be used in Api or web automation to store the values
print(dir)
print(dir2)

#name = 'Suji'chim' -- this will give error
name = 'Suji\'chim' # -- \ will resolve error
name2 = "sujana'chim"
print(name)
print(name2)