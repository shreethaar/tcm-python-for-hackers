print(1) 
print(2)

try:
    f=open("adasadfadf")
except:
    print("the file does not exist")

try:
    f=open("adafasdf")
except Exception as e:
    print(e)


try:
    f=open("aadfdadf")
except FileNotFoundError:
    print("the file does not exist!")
except Exception as e:
    print(e)
finally:
    print("this message!")

n=100
if n==0:
    raise Exception("n cant be 0!")
if type(n) is not int:
    raise Exception("n must be an int")
print(1/n)


n = 1
assert(n!=0)
print(1/n)

n = 0 
assert(n!=0)
print(1/n)
