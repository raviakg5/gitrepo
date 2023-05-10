# Python program to explain os.path.exists() method

# importing os module
import os

# Specify path
path = 'D:\Python\gitrepo'

# Check whether the specified
# path exists or not
isExist = os.path.exists(path)
print(isExist)

# Specify path
path = 'D:\Python\gitrepo\emp.log'

# Check whether the specified
# path exists or not
isExist = os.path.exists(path)
print(isExist)