class Vehicle:
    def __init__(self,seat_cap):
        self.seat_cap=seat_cap
        self.a=23
    def ch(self,seat_cap):
        self.a=34
        return self.a
o=Vehicle(29)
print(o.ch(24))