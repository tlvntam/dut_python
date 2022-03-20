# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     return sum
#
#
# print(add(1, 2, 6))

# def calculate(n, **kwargs):
#     # for key in kwargs:
#     #     print(key)
#     #     print(value)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
# calculate(2, add= 3, multiply= 5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")


my_car = Car(make="Ford")
print(my_car.model)

