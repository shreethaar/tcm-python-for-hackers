def gen_demo():
    n=1
    yield n

    n+=1
    yield n

    n+=1
    yield n

test=gen_demo()
print(test)

print(next(test))
print(next(test))
print(next(test))
#print(next(test)) # stop iteration error 

test2=gen_demo()
for a in test2:
    print(a)

def xor_static_key(a):
    key=0x5
    for i in a:
        yield chr(ord(i)^key)

for i in xor_static_key("test"):
    print(i)

xor_static_key2=(chr(ord(i) ^ 0x5) for i in "test")

print(xor_static_key2)
print(next(xor_static_key2))
print(next(xor_static_key2))


for i in xor_static_key2:
    print(i)

