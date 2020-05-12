class Caesar():
    '''
    Attributes:
    - input
    - key
    - output

    Methods:
    - encode
    - decode
    '''
    def __init__(self, input, key, output):
        self.input = input
        self.key = key
        self.output = output

    @property
    def encode(self):
        output = []
        input = self.input.lower()

        for x in input:
            number = self.key + (ord(character) - 96)
            output.append(number)

        return output

    @property
    def decode(self):
        output = []
        return output
