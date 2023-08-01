    # 1
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def __eq__(self, other):
        return self.radius == other.radius
    def __lt__(self, other):
        return self.radius < other.radius
    def __le__(self, other):
        return self.radius <= other.radius
    def __gt__(self, other):
        return self.radius > other.radius
    def __ge__(self, other):
        return self.radius >= other.radius
    def __add__(self, other):
        return Circle(self.radius + other.radius)
    def __iadd__(self, other):
        self.radius += other.radius
        return self
    def __sub__(self, other):
        return Circle(self.radius - other.radius)
    def __isub__(self, other):
        self.radius -= other.radius
        return self

circle = Circle(5)
circle2 = Circle(4)
print(circle == circle2)
print(circle < circle2)
print(circle <= circle2)
print(circle > circle2)
print(circle >= circle2)
print(circle + circle2)
print(circle - circle2)




    # 2
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.imag * other.real + self.real * other.imag)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        return Complex((self.real * other.real + self.imag * other.imag) / denominator, (self.imag * other.real - self.real * other.imag) / denominator)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

a = Complex(3, 4)
b = Complex(2, -1)

print(a + b)
print(a - b)
print(a * b)
print(a / b)

    # 3
class Airplane:
    def __init__(self, model, max_pass, passengers):
        self.model = model
        self.max_pass = max_pass
        self.passengers = passengers
    def __eq__(self, other):
        return self.model == other.model
    def __add__(self, other):
        new_passengers = self.passengers + other
        if new_passengers <= self.max_pass:
            self.passengers = new_passengers
        else:
            print("Слишком много пассажиров")
        return self
    def __sub__(self, other):
        new_passengers = self.passengers - other
        if new_passengers >= 0:
            self.passengers = new_passengers
        else:
            print("Отрицательное кол-во пассажиров недопустимо.")
        return self
    def __eq__(self, other):
        return self.max_pass == other.max_pass
    def __lt__(self, other):
        return self.max_pass < other.max_pass
    def __le__(self, other):
        return self.max_pass <= other.max_pass
    def __gt__(self, other):
        return self.max_pass > other.max_pass
    def __ge__(self, other):
        return self.max_pass >= other.max_pass
    def __iadd__(self, other):
        return self.__add__(other)
    def __isub__(self, other):
        return self.__sub__(other)

airplane1 = Airplane("A9-B1", 300, 150)
airplane2 = Airplane("A8-B6", 300, 250)
print(airplane1.model == airplane2.model)
print(airplane1.passengers + airplane2.passengers)
print(airplane1.passengers - airplane2.passengers)
print(airplane1.max_pass > airplane2.max_pass)
print(airplane1.max_pass < airplane2.max_pass)
print(airplane1.max_pass <= airplane2.max_pass)
print(airplane1.max_pass >= airplane2.max_pass)

    # 4
class Flat:
    def __init__(self, price, square):
        self.price = price
        self.square = square
    def __eq__(self, other):
        return self.square == other.square
    def __ne__(self, other):
        return self.square != other.square
    def __lt__(self, other):
        return self.price < other.price
    def __le__(self, other):
        return self.price <= other.price
    def __gt__(self, other):
        return self.price > other.price
    def __ge__(self, other):
        return self.price >= other.price

flat1 = Flat(1500000, 60)
flat2 = Flat(1650000, 63)
print(flat1.square == flat2.square)
print(flat1.square != flat2.square)
print(flat1.price < flat2.price)
print(flat1.price <= flat2.price)
print(flat1.price > flat2.price)
print(flat1.price >= flat2.price)