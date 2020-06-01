"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(value=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, value=100):
        """initialize serial generator. default set to 100 unless otherwise stated"""

        self.value = value - 1
        self.init = value
        # self.init = value

    def __repr__(self):
        
        return f'<Current Value ={self.value} Start Value={self.init}'

    def generate(self):
        """increment value by one"""

        self.value += 1
        return self.value

    def reset(self):
        """reset value to initial value"""

        self.value = self.init - 1
