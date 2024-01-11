import math

class Fraction:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.den = denominator

    def add(self, fraction_2):
        result_num = self.num * fraction_2.den + fraction_2.num * self.den
        result_den = self.den * fraction_2.den
        result_fraction = Fraction(result_num, result_den)
        result_fraction.simplify()  
        return result_fraction

    def subtract(self, fraction_2):
        result_num = self.num * fraction_2.den - fraction_2.num * self.den
        result_den = self.den * fraction_2.den
        result_fraction = Fraction(result_num, result_den)
        result_fraction.simplify()  
        return result_fraction

    def multiply(self, fraction_2):
        result_num = self.num * fraction_2.num
        result_den = self.den * fraction_2.den
        result_fraction = Fraction(result_num, result_den)
        result_fraction.simplify()  
        return result_fraction  

    def divide(self, fraction_2):
        result_num = self.num * fraction_2.den
        result_den = self.den * fraction_2.num
        result_fraction = Fraction(result_num, result_den)
        result_fraction.simplify()  
        return result_fraction
        
    def simplify(self):
        common_divisor = math.gcd(self.num, self.den)
        self.num //= common_divisor
        self.den //= common_divisor


fraction1 = Fraction(2, 6)
fraction2 = Fraction(4, 8)

result_sum = fraction1.add(fraction2)
result_subtract = fraction1.subtract(fraction2)
result_multiply = fraction1.multiply(fraction2)
result_divide = fraction1.divide(fraction2)

print(f"SUM: {result_sum.num}/{result_sum.den}")
print(f"SUB: {result_subtract.num}/{result_subtract.den}")
print(f"MULT: {result_multiply.num}/{result_multiply.den}")
print(f"DIV: {result_divide.num}/{result_divide.den}")
