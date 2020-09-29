class Hash:
    def __init__(self, value):
        ascii_value = 0
        for char in value:
            ascii_value += ord(char)
        self.key = ascii_value % 100