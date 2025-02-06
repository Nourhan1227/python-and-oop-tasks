#module  of systemadmin inside subpcge named subadmin inside pcke name mypckge
# define only  contain only def of fn
modes=('r','w','r+','a')
def writefn(path, content):
    with open(path, 'w') as x:
        x.write(content)


def readfn(path, option):
    with open(path, 'r') as x:
        if option == "all":
            return x.read()
        elif option == "line":
            return x.readline()
        elif option == "lines":
            return x.readlines()
        else:
            print("Invalid option")
            return None


def appendfn(path, content):
    with open(path, 'a') as x:
        x.write(content)


def readwritefn(path, content=None, option=None):
    with open(path, 'r+') as x:
        if content is not None:
            x.write(content)
        elif option is not None:
            if option == "all":
                return x.read()
            elif option == "line":
                return x.readline()
            elif option == "lines":
                return x.readlines()
            else:
                print("Invalid option")
                return None