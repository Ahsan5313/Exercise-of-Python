class triangle:
    def __init__(self, height, base):
        self.height = height
        self.base = base

    def calculate_area(self):
        area = 0.5 * self.height * self.base

        print("Area : " ,area)

t1 = triangle(20, 10)
t1.calculate_area()
t2= triangle(30, 15)
t2.calculate_area()
