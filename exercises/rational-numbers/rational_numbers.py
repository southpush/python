from __future__ import division


class Rational(object):
    def __init__(self, numer, denom):
        if denom == 0:
            raise ValueError('denom should not be 0')
        i = 2
        while i <= abs(numer):
            if numer % i == 0 and denom % i == 0:
                numer = numer // i
                denom = denom // i
            else:
                i += 1
        if numer * denom < 0:
            self.numer = -abs(numer)
            self.denom = abs(denom)
        else:
            self.numer = abs(numer)
            self.denom = abs(denom)

    def __eq__(self, other):
        if self.numer == 0 and other.numer == 0:
            return True
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer * self.denom, self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        if self.denom * other.numer != 0:
            return Rational(self.numer * other.denom, self.denom * other.numer)
        else:
            raise ValueError()

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        return Rational(self.numer ** power, self.denom ** power) if power > 0 else Rational(self.denom ** -power, self.numer ** -power)

    def __rpow__(self, base):
        return base ** (self.numer / self.denom)
