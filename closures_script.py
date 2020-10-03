"""A closure is a nested function which has access to a free variable"""
def make_printer(msg):

    msg = "hi there"

    def printer():
        print(msg)

    return printer


myprinter = make_printer("Hello there")
myprinter()
myprinter()
myprinter()