import unittest
from hash_table.hash_table import HashTable


class MyTestCase(unittest.TestCase):
    def test_empty_hash_table(self):
        hash_table = HashTable()
        self.assertIsNone(hash_table.get_keys())

    def test_hash(self):
        hash_table = HashTable()
        value = "Jasmine Smith"
        self.assertEqual(hash_table.hash(value), 260)

    def test_get_not_in_hash_table(self):
        pass

    def test_set(self):
        hash_table = HashTable()
        value = "Jasmine Smith"
        hash_table.set(value)
        self.assertEqual(hash_table.get("Jasmine Smith"), 260)

    def get_in_hash_table(self):
        pass

    def test_set_empty_hash_table(self):
        pass

    def test_set_not_empty_hash_table(self):
        pass

    def test_set_collision(self):
        pass

    def test_get_keys(self):
        hash_table = HashTable()
        hash_table.set("Jasmine Smith")
        self.assertEqual(hash_table.get_keys(), {260: "Jasmine Smith"})

    def test_get_keys_empty_hash_table(self):
        hash_table = HashTable()
        self.assertIsNone(hash_table.get_keys())

    def test_has_in_hash_table(self):
        pass

    def test_has_not_in_hash_table(self):
        pass

    def test_has_collision(self):
        pass

    def test_delete_not_in_hash_table(self):
        pass

    def test_delete_in_hash_table(self):
        pass

    def test_delete_collision_keys(self):
        pass


if __name__ == '__main__':
    unittest.main()
