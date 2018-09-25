#there is a bool data type (which inherits from int and has only two values: True and False ).
# But also Python has the boolean-able concept for every object, which is used when function bool([x]) is called.

#When we sum two integer objects using the + operator, like 2 + 5, we get a new object: 7.
# In the same way, when we compare two integers using the < operator, like 2 < 5, we get a new object: True

print(2<5)

print(2>5)

#The True and False objects have a special type called bool.
# As every type name can be used to cast objects into that type, let's see what this cast gives for numbers:

print(bool(-10))
print(bool(0))
print(bool(30))
print(bool())
print(bool("qwerty"))
print(bool(""))

#Any object can be tested for truth value, for use in an if or while condition or as
# operand of the Boolean operations below. The following values are considered false:
#1.None
#2.False
#3.zero of any numeric type, for example, 0, 0L, 0.0, 0j.
#4.any empty sequence, for example, '', (), [].
#5.any empty mapping, for example, {}.
#6.instances of user-defined classes,
# if the class defines a __nonzero__() or __len__() method, when that method returns the integer zero or bool value False. [1]