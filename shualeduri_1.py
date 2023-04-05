class Person:
    def __init__(self,age,gender,pulse):
        self.age = age
        self.gender = gender
        self.pulse = pulse
    def __str__(self):
        return f"age:{self.age} , gender:{self.gender} , pulse:{self.pulse} beats per minute"
    def life(self):
        return round(2600000000 / self.pulse / 60 / 24 / 365,2)
    def max_hb(self):
        if self.gender=="F" or "m":
            max_pulse= 226 - 0.9 * self.age
            return max_pulse
        elif self.gender=="M" or "m":
            max_pulse = 223 - 0.9 * self.age
            return max_pulse
    def workout_hb(self,factor):
        self.factor = factor
        if self.factor == "ინტენსიური":
            self.factor = 0.8
        elif self.factor == "საშუალო":
            self.factor = 0.6
        elif self.factor == "დამწყები":
            self.factor = 0.5

        workout_pulse = (self.max_hb() - self.pulse)*self.factor + self.pulse
        return workout_pulse


p1=Person(15,"f",60)
print(p1.life())
print(p1.max_hb())
print(p1.workout_hb("საშუალო"))