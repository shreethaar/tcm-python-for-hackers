string1="I am a string"
print(string1)

string2='I am a string too'
print(string2)

string3 = """ I am a long 
long 
string!"""

print(string3)

string4="I\"m a string"
print(string4)

string5='I\'m a string'
print(string5)

string6="I'm a string"
string7='I"m a string'

print(string6)
print(string7)

string8="I\"m a string\nI on a newline !"
print(string8)

string9="\\"
string10="\\ \x41\x42\x43"
print(string10)

string11="aaaaaaaaaa"
print(string11)

string12="a"*10
print(string12)

print(len(string12))

print("string" in string3)
print("neut" in string3)

print(string4.startswith("I"))
print(string4.startswith("n"))

print(string4.index("string"))
print(string4.upper())
print(string4.lower())

messy_string="      Messy string!   "
print(messy_string)
print(messy_string.strip())
print(messy_string.replace("!","?"))
print(messy_string.replace("!","?").strip())
print(messy_string.replace("string","example"))
print(messy_string.split())
print(messy_string.split(","))


string13="I am a string!"
print(string13)
print(string13.encode())
print(string13.encode("utf-8"))

print(string13.rjust(25))
print(string13.rjust(25,"X"))

print(string13.ljust(25))
print(string13.ljust(25,"X"))


print("I am " + " a string")
print("String 4 is " + str(len(string4)) + "characters long") 

print(1+1)
print("1"+"1")
print(type("1"+"1"))

print("string4 is {} characters long!".format(len(string4)))
print("{} {} {}".format(len(string4),5.0,0x12))
print("{0} {2} {1}".format(len(string4),5.0,0x12))
print("{length}".format(length=len(string4)))

length=len(string4)
print(f"string4 is {length} characters long")


print("string4 is {length:.2f} characters long".format(length=len(string4)))

print("string4 is {length:.3f} characters long".format(length=len(string4)))
print("string4 is {length:.4f} characters long".format(length=len(string4)))
print("string4 is {length:x} characters long".format(length=len(string4)))
print("string4 is {length:b} characters long".format(length=len(string4)))
print("string4 is {length:o} characters long".format(length=len(string4)))
print("string4 is {length:.3f} characters long".format(length=len(string4)))

print("string4 is %d characters long!" % len(string4))

print("string4 is %f characters long!" % len(string4))
print("string4 is %x characters long!" % len(string4))
