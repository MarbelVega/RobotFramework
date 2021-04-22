
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
y = 0
checkException(x,y)

# normal try -> else -> finally
# exception try -> except -> finally
