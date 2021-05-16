"""
Whn to use ?
When we're expecting exception like file operations, connecting to db. I/O streaming etc
Show meaning full msg instead of stack trace
"""

def checkException(x,y):
    try:
        z = (x / y)
    except(ZeroDivisionError):
        print("We tried to divide by zero")
    else:
        print("Something else went sideways")
    finally:
        print("Code cleanup")

x = 42
y = 1
checkException(x,y)

''' 
same thing is achieved by 'with' command
with open('output', wt) as stream:
    stream.write('Lorem ipsum dolar')
    
closes stream regardless of open succeeded or not     
'''

# normal try -> else -> finally
# exception try -> except -> finally
