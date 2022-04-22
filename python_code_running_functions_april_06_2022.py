
# python is unstructed program
# python can be made as structured programming if it follows "class principles"
# class is a collection of objects
# object is a real world entity
# class is a kind of template or wrapper to hold things
# object is anything which takes memory
# class is mainly to give the property of inheritance or extensibility
#.......................................................................................................................................

##var = "dhoni"
##print(var)
##
##def fun():
##    print("welcome")
##
##fun()
#........................................................................................................................................

##class my_class:
##    var = "dhoni"
##
##    def fun():
##        print("welcome")
##
##print(my_class.var)
##my_class.fun()
#.........................................................................................................................................

##class my_class:
##    var = "dhoni"
##
##    def fun():
##        print("welcome")
##
##my = my_class
##print(my_class.var)
##my_class.fun()
##my is called object reference of the "my_class"
##class with out constructor
#...........................................................................................................................................

##class my_class:
##
##    def new(name):
##        print("hello")
##
##    def fun(name,age):
##        print("welcome")
##
##my = my_class
##my.fun("dhoni",33)
##my.new("dhoni")
#.............................................................................................................................................

##class my_class:
##
##    def __init__(self,name,age):
##        
##        self.name = name
##        self.age = age
##
##    def new(self):
##        print(self.name)
##
##    def fun(self):
##        print(self.name,self.age)
##
##my = my_class("dhoni",33)
### my_class is called constructor class
### my is called as object reference with single instant memory (single instant memory)
### my_class() will have one hidden object inside
### whenever you create constructor , an attribute called __init__ is created automatically
### attribute or magic method or dunder method is anything that contain double underscore on eighter side
### self is similar to my
### my is the object reference for external class
### self is the object references for internal class
##my.fun()
##my.new()
