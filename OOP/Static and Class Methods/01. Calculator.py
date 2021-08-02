class Calculator:
    @staticmethod
    def add(*args):
        return sum(args)

    @staticmethod
    def multiply(*args):
        current_result = 1
        for arg in args:
            current_result *= arg
        return current_result

    @staticmethod
    def divide(*args):
        current_result = None
        for arg in args:
            if not current_result:
                current_result = arg
                continue
            current_result /= arg
        return current_result

    @staticmethod
    def subtract(*args):
        current_result = None
        for arg in args:
            if not current_result:
                current_result = arg
                continue
            current_result -= arg
        return current_result


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
