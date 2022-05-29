# ------------------------------------------------- #
# Title: Assignment07
# Description: Pickling and Error Handling
# ChangeLog: (Who, When, What)
# THitch,05.28.22,Created Script
# ------------------------------------------------- #
# need to import the pickle functions
import pickle

# define some data to be pickled
demolist = ('Information','to be pickled',2)
readlist = ()
print('Before pickling')
print('Demolist(input) = ', demolist)
print('Readlist(output) = ', readlist)

# Open the file, Pickle.dump to write to the file and close it
objfile = open('demopickle.bin', "wb")
pickle.dump(demolist, objfile)
objfile.close()

# Open the file, Pickle.load to read the file to readlist and close it
objfile = open('demopickle.bin', "rb")
readlist = pickle.load(objfile)
objfile.close()

# verify the contents of readlist
print('After pickling')
print('Demolist(input) = ', demolist)
print('Readlist(output) = ', readlist)
input('End of pickling')

# Error Handling
try:
    print(5/0) # Force an error
except: # errors execute the except block
    print('There is an error')

try:
    print(5/5)
except:
    print('There is an error')
else: # when there is no error else executes
    print('It worked')
finally: # executes regardless of error state
    print('the try block has concluded')

sampleinput = input('When not in a try block, you can raise exceptions when desired\nIf you enter anything other then 0 you will see an error message\n')
if sampleinput == '0':
    print('You entered 0')
else:
    raise Exception('That was not a zero')
try:
    print('Catching specific errors')
    print(5/0)
except Exception as a:
    print(a)
    print(type(a))
    print(a.__doc__)
    print(a.__str__())

try:
    print('catching a division by zero')
    print(5/0)
except ZeroDivisionError as a:
    print('ZeroDivisionError caught')

input()