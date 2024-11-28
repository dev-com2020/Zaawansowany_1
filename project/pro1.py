class Temp:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError('Temperature below -273.15 is not possible')
        self._celsius = value

temp = Temp(10)
print(temp.celsius)
temp.celsius = -400