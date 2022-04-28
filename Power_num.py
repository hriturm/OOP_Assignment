class Power:
    def __init__(self,x ,n):
        self.x = x
        self.n = n

    def pow(self):
        return self.x**self.n

pow_obj = Power(10, 2)
print(pow_obj.pow())