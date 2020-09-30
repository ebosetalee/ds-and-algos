class HashTable:
    def __init__(self):
        """
        Initialize the Hash Table here
        """
        self.dict = None

    def hash(self, value):
        """
        Calculate the value using ascii value to get the key

        :param value: the value to be calculated
        """
        pass

    def get(self, value):
        """"
        Requests the key of the value

        :param value: The value of the key requested for
        :returns: The key or None if not in the dict
        """
        pass

    def set(self, value):
        """
        Adds the value and key to the dict

        :param value: the value to be added
        """
        pass

    def get_keys(self):
        """"
        Prints out all the items in the dict

        :returns: The keys and values in the dict
        """
        return self.dict

    def has(self, key):
        """
        Searches the dict for the key

        :param key: the key searched for
        :return: True if the key is in the dict, or False if it isn't in the dict
        """
        pass

    def delete(self, value):
        """
        Finds the vales and deletes it with its key

        :param value: the value to be deleted
        :return: True if the value was deleted, or False if the value isn't in the dict
        """
        pass
