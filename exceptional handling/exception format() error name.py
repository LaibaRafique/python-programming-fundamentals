lIst = [5, 10, 20]
try:
    print(lIst[5])
except IndexError as error:
    print('Exception is: {}'.format(type(error).__name__))