f = open('top-100.txt')
print(f)

f = open('top-100.txt','rt')
print(f)
print(f.read()) # comment out as it reaches end of file
print("--------")
print(f.readlines())
f.seek(0)
print(f.readlines())
f.seek(0)
for line in f:
    print(line.strip())

f.close()


f = open("test.txt","w")
f.write("test line!")
f.close()

f=open("test.txt","a")
f.write("test line two!")
f.close()

print(f.name)
print(f.closed)
print(f.mode)

with open('rockyou.txt',encoding='latin-1') as f:
    for line in f:
        pass
