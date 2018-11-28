from math import pi
from random import uniform, randrange
randrange(0, 2)   # random integer (0 or 1)

def rect_circ(width, height):
    "Returns rectangle circumference."
    return 2 * (width + height)


def write_notification(rectangle_area):
    "Defines the size of your rectangle."

    print('Your new rectangle is:')
    if rectangle_area < area / 4:
        print('Tiny.')
    elif rectangle_area < area / 2:
        print('Very small.')
    elif rectangle_area < area:
        print('Smaller.')
    elif rectangle_area == area:
        print('Identical.')
    elif rectangle_area < 2 * area:
        print('Big.')
    else:
        print('Huge.')


def yes_or_no(random_num):
    "Schroedingers cat"
    while True:
        random_num = random_num
        if random_num == 1:
            return True
        else:
            return False


def ellipse_area(semi_major, semi_minor):
    "Calculates the area of the elipse fun(a,b)."
    return round(pi * semi_major * semi_minor, 4)


def cylinder_vol(semi_long, semi_short, height):
    "Calculates the volume of any cylinder"
    return round(ellipse_area(semi_major, semi_minor) * height, 4)


def get_input():
    while True:
        x = input('Choose any length in metres: ')
        try:
            return float(x)
        except ValueError:
            print('This is not a number! please, try again!')


x = get_input()
#  input as float in metres
#  variable = input('Choose any string: ') input as text
#  variable = int(input('Choose any number: ')) input as integer

while x <= 0:
    x = float(input('Choose any length in metres: '))
    if x == 0:
        print("""Zero!!! ...
...We can't make any calculation this time.""")
        print("Please, please try again :|.")
    else:
        print("""C'mon. The side length has to be positive,
otherwise the results make no sense.""")
        print("Please, make more effort :/.")

else:
    cf = 4*x
    area = x ** 2
    r = x / 2
    circ = 2 * pi * r
    circ_area = pi * r ** 2
    semi_major = r * uniform(0.001, 1.999)  # semi major axis
    a = 2 * semi_major
    semi_minor = r * uniform(0.001, 1.999)  # semi minor axis
    b = 2 * semi_minor
    height = x  # cylinder height
    rectangle_area = a * b
    rectangle_circumference = rect_circ(a, b)
    print("The circumference of the square with side",
          round(x, 2), "m is", round(cf, 2), "m.")
    print("The area of the same square with side", x, "is",
          round(area, 2), "m2.")
    print("The circumference of the circle within this square (radius: ",
          round(r, 2), "m) is", round(circ, 2), "m.")
    print("The area of the same circle with radius is",
          round(circ_area, 2), "m2.")
    print("\nRANDOM RECTANGLE:\nHeight: ", round(a, 2), "metres.\nWidth: ",
          round(b, 2), "metres.")
    print('The circumference of this rectangle is',
          round(rectangle_circumference, 2), 'metres.')
    print('It\'s area is', round(rectangle_area, 4), 'm2.')
    write_notification(rectangle_area)
    print('\nRANDOM ELLIPSE:\nArea of the ellipse within your new rectanle',
          ellipse_area(a / 2, b / 2), 'is m2')
    print('Volume of the cylinder with height', height, 'over ellipse is',
          cylinder_vol(a / 2, b / 2, x), 'is m3')
    print('Thank you for using the random geometric calculator.')

    print("""\nBONUS:\nThe Schrödinger's cat.\nOnce upon the time...
...there was an important quantum experiment.""")
    random_num = randrange(0, 2)
    if yes_or_no(random_num):
            print('\nDoc\'s cat made it "alive" this time.')
    else:
            print("""\nMeow...
Ups!!!
It looks like Doc's cat died before he could even start his experiment!!!""")
