
import sys 

# sys.argv: arguments at command line

# sys.argv will alway be there, 
# always be a string list, 
# with at least one item
# any argument passed in cmd line 
# check len(sys.argv) to check if any arguments has been passed

print(sys.argv)             # ['sys_argv.py']
print(sys.argv[0])          # sys_argv.py -> always at least one item: script name 
print(type(sys.argv))       # <class 'list'>










