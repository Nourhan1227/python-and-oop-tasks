#####file to import my modules and callong fns from modules


# import module
# print(module.modes)
# content=module.readfn('d.txt','lines')
# print(content)
#############or  use  from and import
# from module import modes,readfn

# print(modes)
# content=readfn('d.txt','lines')
# print(content)
#calling modules >>>>>>>>>from pckge.module import fn or vars
# from mypckge.module  import modes,readfn
# print(modes)
# content=readfn('d.txt','lines')
# print(content)
########calling subpackage  >>>>>>>> from pckge.subpckg import module
from mypckge.subadmin.system import * 
print(modes)

#read
content=readfn('d.txt','lines')
print(content)

#write
writefn("d.txt", "hi from day5")
print(readfn("d.txt", "lines"))

#append
appendfn("d.txt", " hi again from day5")
print(readwritefn("d.txt", option="all"))


#readwrite fn
readwritefn("d.txt", content="hello from read write")