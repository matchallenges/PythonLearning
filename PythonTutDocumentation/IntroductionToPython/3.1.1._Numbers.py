# this code was created while reading the 3.1.1. Numbers documentation on the tutorial page

from decimal import *
from fractions import *
import math

#Numbers

print (2 + 2) # add
print (50 - 5 * 6) # subtract and multiply
print (17 // 6) # floor division
print (4 ** 2) # exponent

# in python the equals sign is used to assign a value to a variable, no result is displayed

x = 5

f = 3
g = 5

print (f + g)

# we can also mix floating point values and integer values

print (4 * 4.33 // 2) # converts the integer operand to a floating point

# in interactive mode the last printed expression is saved to the variable _

price = 143.74
tax = 1.13
shipping = 10.0
_ = (price * tax)
print (_ + shipping) #interactive mode _ would be assigned to this displayed float

# additionally Python also support Decimal and Fraction objects (more accurate then a floating point because it will round to our level of accuracy)

print (repr(Decimal(5.5) + Decimal(8.7))) #returns another decimal object

getcontext().prec=3

print (repr(Decimal(5.5) + Decimal(8.7))) # look at how the object changes if we modify the precision value

# more advanced precision would be to maybe use the 'with' statement to make changes within that operation

with localcontext() as ctx:
     #localcontext being a temp change
     ctx.prec = 100
     print (repr(Decimal(5.5) + Decimal(8.7)))

print (repr(Decimal(5.5) + Decimal(8.7))) # the global value should not change and the precision value stayed within the 'with' statement

# or we can quantize a variable that has already been created 

q = Decimal(5.5555555555)
print (q.quantize(Decimal('0.00'))) # and then afterwards we can round the number more dynamically

# afterwards we can also typecast it

cast_to_float = float(q.quantize(Decimal('0.00')))
print (type(cast_to_float))

# we can also set parameters to round up or round down when we quantize

print (q.quantize(Decimal('0.00'), rounding = ROUND_DOWN))

# If value is a tuple, it should have three components, a sign (0 for positive or 1 for negative), a tuple of digits, and an integer exponent. For example, Decimal((0, (1, 4, 1, 4), -3)) returns Decimal('1.414').
# Documentation above about an interesting way of contructing decimals from tuples

decimal_tuples = (1, 2, 4, 2)
print (Decimal((0, (decimal_tuples), -3))) # the negative three at the end indicates the amount of spaces the decimal moves by from the end of the tuple

# fractions return numerator and denominator *syntax [sign] numerator ['/' denominator]

print (Fraction(0.5))
print (Fraction(100, 5))
print (Fraction('2/3'))

# we can also combine fraction and decimal objects

print (Fraction(Decimal((0, (decimal_tuples), -4)))) # can automatically convert decimal objects into fractions

print (Fraction.as_integer_ratio(Fraction(0.5))) #integer_ratio returns a tuple with two numbers whose ratio is equal to the fraction (simplified basically) with a positive denominator

# fractions module used to have a function called (greatest common divisor) / gdc but the math module added easier functionality

print (math.gcd(2, 34)) # biggest number we can divde both integers is by 2

#WIP

