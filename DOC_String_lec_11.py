#DOC In Python => is a special string which tells about the compilation of a function/class/method/module
#DOCSTRING is declare right after the function/class/method
def square(n,upto):
    '''THIS FUNCTION WILL FIRST CHECK IF THE IS N == 0 OR NOT , THEN IF IT IS != 0 IT WILLRETURN N**2 SQUARE OF NUMBER'''
    if n == 0:
        return 0
    return n**upto

result = square(5,2)
print(":",result)
print(help(square)) # DOCstring => call : help(fun_name)