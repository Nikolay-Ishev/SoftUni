from math import floor


class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if type(float_value) is float:
            return cls(floor(float_value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        mapping = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        dec = last = 0
        for i in range(0, len(value)):
            no = mapping.get(value[i])
            # subtract last 2 times cuz one for this pass and another for last pass
            dec = dec + (no - 2 * last) if no > last else dec + no
            last = no
        return cls(dec)
        pass

    @classmethod
    def from_string(cls, value):
        if type(value) is not str:
            return "wrong type"
        return cls(int(value))



