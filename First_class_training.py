#
# class Dog:
#     """simulate of dog"""
#
#     def __init__(self, name, age):
#         """init type name and age"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """imitate action of sit"""
#         print(self.name.title() + " is now sitting. ")
#
#     def roll_over(self):
#         """imitate action of rolll"""
#         print(self.name.title() + " rolled over ")
#
#
# my_dog = Dog('willie', 6)
# my_dog.sit()
# my_dog.roll_over()
# print("My dog's name is " + my_dog.name.title() + ".")
# print("My dog is " + str(my_dog.age) + " years old.")

from car import ElectricCar, Car, Battery

    # def get_describe_battery(self):
    #     """打印一条描述电瓶容量的消息"""
    #     print("This car has a " + str(self.battery_size) + "-kwh battery")


# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()
#
# my_used_car = Car('subaru', 'outback', 2013)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()


