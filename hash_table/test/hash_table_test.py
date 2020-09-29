import unittest
from hash_table.hash_table import HashTable
from hash.hash import Hash


class MyTestCase(unittest.TestCase):
    def test_empty_hash_table(self):
        hash_table = HashTable()
        self.assertIsNone(hash_table.dict)

    def test_hash_key(self):
        key = "Jasmine Smith"
        hash_function = Hash(key)
        self.assertEqual(hash_function.key, 60)

    def test_add(self):
        hash_table = HashTable()
        value = "Jasmine Smith"
        hash_table.add(value)
        self.assertEqual(hash_table.dict, {60: "Jasmine Smith"})

    def test_walk(self):
        hash_table = HashTable()
        hash_table.add("Jasmine Smith")
        self.assertEqual(hash_table.walk(), {60: "Jasmine Smith"})

    def test_find(self):
        pass

    def test_remove(self):
        pass


if __name__ == '__main__':
    unittest.main()
