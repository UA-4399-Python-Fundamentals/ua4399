import unittest
import functions
import functions_with_errors

class FunctionsTest(unittest.TestCase):

    def setUp(self):
        self.modules = [functions, functions_with_errors]

    def test_greeting_by_name(self):
        test_cases = [
            ("Alice", "Hello Alice!"),
            ("", "Hello !")
        ]
        for module in self.modules:
            for name, expected in test_cases:
                with self.subTest(module=module.__name__, name=name):
                    self.assertEqual(module.greeting_by_name(name), expected)

    def test_get_symbol_position(self):
        test_cases = [
            ("hello world", "o", 5),
            ("apple", "a", 1),
            ("hello", "z", "Not found"),
            ("hello", "he", "Error! Symbol can be string with only one letter"),
            ("", "a", "Not found"),
            ("abc", "", 1)
        ]
        for module in self.modules:
            for text, symbol, expected in test_cases:
                with self.subTest(module=module.__name__, text=text, symbol=symbol):
                    self.assertEqual(module.get_symbol_position(text, symbol), expected)

    def test_merge(self):
        test_cases = [
            ({"a": 1, "b": 2}, {"c": 3, "d": 4}, {"a": 1, "b": 2, "c": 3, "d": 4}),
            ({"a": 1, "b": 2}, {"b": 3, "c": 4}, {"a": 1, "b": 3, "c": 4}),
            ({}, {"a": 1}, {"a": 1}),
            ({"a": 1}, {}, {"a": 1}),
            ({}, {}, {}),
            ({"name": "Alice", "age": 30}, {"city": "New York", "age": 31}, {"name": "Alice", "age": 31, "city": "New York"})
        ]
        for module in self.modules:
            for dict1, dict2, expected in test_cases:
                with self.subTest(module=module.__name__, dict1=dict1, dict2=dict2):
                    result = module.merge(dict1.copy(), dict2.copy())
                    self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
