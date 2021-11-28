# Homework: OOP

from fraction import Fraction


my_fraction_one = Fraction(4, 2)
my_fraction_two = Fraction(3, 2)
print("my first fraction: ", my_fraction_one)
print("my second fraction: ", my_fraction_two)

sum_of_fractions = my_fraction_one + my_fraction_two
print("sum of fractions: ", my_fraction_one, "+", my_fraction_two, "=", sum_of_fractions)

sub_of_fractions = my_fraction_one - my_fraction_two
print("subtraction of fractions: ", my_fraction_one, "-", my_fraction_two, "=", sub_of_fractions)
my_fraction_one.reverse()
print("my first fraction reversed: ", my_fraction_one)
