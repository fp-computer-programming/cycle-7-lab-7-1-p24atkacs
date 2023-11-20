"""
Create a Python file named lab_7-1.py

*** You must write a comment for every chunk of code you write from now on along with your author tag***

Create a function called greeting()
Add a docstring to the function that explains how the function can only print "Hello World" on one line
Add a statement in the function to print "Hello World!"
Add a statement that returns the docstring for the greeting function
Add another statement to call the function
"""

#Author: Andrew Tkacs

def greeting():
    """
    This function prints 'Hello World' on one line.
    """
    print("Hello World!")

    # Return the docstring for the greeting function
    return greeting.__doc__ #I used __doc__ functions bc it provides documentation for my docstring

# Call the greeting function
greeting()

