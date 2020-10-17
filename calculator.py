class Calculator:


    def sum(self, a=0, b=0, precision=2):
        return round(a + b, precision)


    def subtract(self, a=0, b=0, precision=2):
        return round(a - b, precision)
    

    def multiply(self, a=0, b=0, precision=2):
        return round(a * b, precision)


    def divide(self, a=0, b=1, precision=2):
        return round(a / b, precision)