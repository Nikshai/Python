from importfile import *
import importfile as imp

b = imp.list_imp()
print("The list before updation:",b)
c = b
c[3] = 4
c[4] = 5
print("The list after updation:",c)