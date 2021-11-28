def gcd(m, n):
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        sum_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        sum_denominator = self.denominator * other.denominator
        common = gcd(sum_numerator, sum_denominator)
        return Fraction(sum_numerator // common, sum_denominator // common)

    def __sub__(self, other):
        sub_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        sub_denominator = self.denominator * other.denominator
        common = gcd(sub_numerator, sub_denominator)
        return Fraction(sub_numerator // common, sub_denominator // common)

    def reverse(self):
        aux = self.numerator
        self.numerator = self.denominator
        self.denominator = aux
