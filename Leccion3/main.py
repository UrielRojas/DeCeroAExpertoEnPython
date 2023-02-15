# ------------Basic Data types----------------
# String
Var = "Hello"
print(type(Var))

##Int
Var = 1
print(type(Var))

# Float
Var = 1.1
print(type(Var))

# Boolean
Var = False
print(type(Var))

# ----------------Strings management--------------
MyFavoriteGroup = "Aerosmith" + " " + "The best rockband"
comment = "Ever"
# First way to concat

print("My Favorite group is: " + MyFavoriteGroup + " " + comment)

# Second way to concat
print("My Favorite group is:", MyFavoriteGroup, comment)


#third way to concat
NewConcat = MyFavoriteGroup + comment
print("My Favorite group is: " +NewConcat)

#String to int

number1 = '2'
number2 = '2'

print("concat: ", number1 + number1)
print("Sum: ", int(number1) + int(number2))

##----------Tipos de bool---------------
BoolenVar = False
print(BoolenVar)

BoolenVar = 22>3
print(BoolenVar)