##print("hello")
##print("welcome to python")
##
##def MY_fun(): #function defining without argument or signature or parameters
##
##    print("hello")
##    print("hello program")
##
##MY_fun() #function calling

##def MY_fun(name): #function defining with argument or signature or parameters
##
##    print("hello", name)
##    print("hello program")
##
##MY_fun("kohili") #function calling
##MY_fun("dhoni")


##def MY_fun(name): #function defining with argument or signature or parameters
##
##    if isinstance(name,str):
##        print("hello", name)
##        print("hello program")
##
##MY_fun("kohili") #function calling
##MY_fun(4)


##def MY_fun(name,country): #function defining with argument or signature or parameters
##
##    if isinstance(name,str) and isinstance(country,str):
##        print("hello", name, "from", country)
##        print("hello program")
##
##MY_fun("kohili","india") #function calling
##MY_fun("dhoni",4)


##def MY_fun(name,country): #function defining with argument or signature or parameters
##
##    if isinstance(name,str):
##        if isinstance(country,str):
##            print("hello", name, "from", country)
##            print("hello program")
##
##MY_fun("kohili","india") #function calling
##MY_fun("dhoni",4)


##def MY_fun(name,country = "india"): #function defining with argument or signature or parameters
##
##    if isinstance(name,str):
##        if isinstance(country,str):
##            print("hello", name, "from", country)
##            print("how are you!")
##
##MY_fun(country = "india",name = "kohili") #function calling
##MY_fun("dhoni","chennai")


##def MY_fun(name,country = None): #function defining with argument or signature or parameters
##
##
##        print("hello", name, "from", country)
##        print("how are you!")
##
##MY_fun("kohili") #function calling
##MY_fun("dhoni","chennai")


##def MY_fun(name="sachin",country): #function defining with argument or signature or parameters
##
##
##        print("hello", name, "from", country)
##        print("how are you!")
##
##MY_fun("kohili") #function calling
##MY_fun("dhoni","chennai")


##def student_passed(*names):
##
##    print(names)
##
##student_passed("dhoni")
##student_passed("kohili", "sachine")

#*args means it can take any number of arguments
#output will be in the form of tuples


##def student_passed(**names):
##
##    print(names)
##
##student_passed(name = "dhoni")
##student_passed(name = "kohili",age = "sachine")

#**args means it can take any number of arguments
#output will be in the form of dictionary


##def student_mark(eng,math,student_name):
##
##    total = eng + math
##    return
##
##print(student_mark(40,50,"dhoni"))


##def student_mark(eng,math,student_name):
##
##    total = eng + math
##    return
##
##output = student_mark(40,50,"dhoni")
##print(output)


##def student_mark(eng,math,student_name):
##
##    total = eng + math
##    return total, student_name
##    print(welcome)
##
##output = student_mark(40,50,"dhoni")
##print(output)


##scoping.......................................................

##var = 100 #outside variable(global)
##def fun():
##    var = 10 #local
##    print(var)
##
##print(var)
##fun()
##print(var)


##var = 100 #outside variable(global)
##def fun():
##    global var
##    var = 10 #local
##    print(var)
##
##print(var)
##fun()
##print(var)

##counter = 0
##def fun():
##    global counter
##
##    print("hello", counter)
##    counter = counter + 1
##    fun()
##
##fun()


##counter = 0
##def fun():
##    global counter
##
##    print("hello", counter)
##    counter = counter + 1
##    if counter == 101:
##        return
##    fun()


##counter = 0
##def fun():
##    global counter
##
##    print("hello", counter)
##    counter = counter + 1
##    while counter < 101:
##        fun()
##fun()


##counter = 0
##def fun():
##    global counter
##
##    print("hello", counter)
##    counter = counter + 1
##    if counter < 101:
##        return
##    fun()
##fun()




























