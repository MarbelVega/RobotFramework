# Add meaningful info
def logger(func):
    def wrapper():
        print('Logging execution')
        func()
        print('Done logging')
    return wrapper()

@logger
def sample():
    print('--Inside sample')

sample()

# Register route e.g https://myserver/api/products
#
# @route('api/products'):
#     #list from db
