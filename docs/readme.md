*Timothy Hitch*  
*May 28, 2022*  
*IT FDN 110A*  
*Assignment 7*  
# Documenting Assignment Seven
## Introduction
I created a script to demonstrate pickling and error handling. Pickling is a python native function to store data in a binary fine. Error handling manages what happens when programs experience exceptions.
## Pickling
Pickling is a python native function that converts data into a data stream. It produces smaller sized output then using text. I created a table demolist and used dumpto save it into the demopickle.bin file.
 ```
 # Open the file, Pickle.dump to write to the file and close it
objfile = open('demopickle.bin', "wb")
pickle.dump(demolist, objfile)
objfile.close()
```
I then used load to populate a blank list, readlist, with the contents of the file. Displaying both lists, before and after pickeling demonstrates that the information was passed from one list, to the other after passing thorough the file on the drive.
It is worth noting that while researching pickle, the official documentation, https://docs.python.org/3/library/pickle.html,  make a warning that pickle is not secure and unpickling unknown data can execute arbitrary code.
## Error Handling
Exceptions in python is handled in multiple ways. They can be raised, or handled as they happen. I started with forcing an error and catching it with a try/except block.
```
# Error Handling
try:
    print(5/0) # Force an error
except: # errors execute the except block
    print('There is an error')
```
This captures any exception that happens in the try block, and allows the program to continue. I added the else and finally commands to the next try block. Else provides code when there is no exception, and finally executes at the completion of the try block regardless of errors.
Raising an exception allows for custom generated errors to be produced. Using if/else I asked for an input of 0, all other input produced an error.

This is useful for catching input that is technically valid, but not what is wanted.
	The last variation of error handling was to catch specific errors. Using a try/except block you specify what specific error you are looking for. In the example earlier it was a ZeroDivisionError. The Python standard library, https://docs.python.org/3/library/exceptions.html, explains all the standard error types in python
## Summary
Pickling allows the storage of data to the drive, in a smaller and more obscured way. Error handling allows us to provide users with the tools they need to use our software.
