#!/usr/bin/env python
# HW04_ex07_04

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:
    
#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes the
# resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

################################################################################
# Imports
import math

# Body

def eval_loop():
 
 while(True):
  print "Enter the expression or enter 'done' to exit"
  x=raw_input()
  if(x=='done'):
   print 'Bye!'
   break
  else:
   try:
    print(eval(x))
    break
   except:
    print "Not an expression. Try again."
    continue



################################################################################
def main():

     eval_loop()
    

if __name__ == '__main__':
    main()