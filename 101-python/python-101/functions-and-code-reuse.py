def function1():
    print("hello from function1")

function1()
function1()
print("-------------")

def function2():
    return "Hello from function2"

return_from_function2=function2()
print(return_from_function2)
print("-------------")

def function3(s):
    print("\t{}".format(s))
function3("parameter")
function3("parameter2")

def function4(s1,s2):
    print("{} {}".format(s1,s2))
function4("s1","s2")
function4("any","thing")
function4(s1="thing",s2="any")
function4(s2="any",s1="thing")

def function5(s1="default"):
    print("{}".format(s1))
function5()
function5("anything")

def function6(s1,*more):
    print("{} {}".format(s1," ".join([s for s in more])))
function6("function6")
function6("function6","a")
function6("function6","a","b","c")

def function7(**ks):
    for a in ks:
        print(a,ks[a])

function7(a="1",b="2",c="3",d="4")

def function8(s,f,i,l):
    print(type(s))
    print(type(s))
    print(type(i))
    print(type(l))

function8("string",1.0,1,['l','i','s','t'])


v=1000
print(v)

def function9():
    print(v)
function9()
print(v)

def function10():
    v=5
    v+=1
    print(v)
function10()
print(v)


v=100
print(v)

def function11():
    global v
    v+=1
    print(v)
function11()
print(v)

def function12():
    print("hello from function12")

def function13():
    print("hello from function13")

function12()
function13()

def function14():
    function12()
    function13()
function14()

def function15(x):
    print(x)
    if x>0:
        function15(x-1)
function15(5)

def function16(x):
    while x>=0:
        x-=1
function16(5)
