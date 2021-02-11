class DivisionZero:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_zero(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль невозможно")


div = DivisionZero(1, 20)
print(DivisionZero.divide_zero(10, 0))
print(DivisionZero.divide_zero(20, 0.1))
print(div.divide_zero(1, 0))