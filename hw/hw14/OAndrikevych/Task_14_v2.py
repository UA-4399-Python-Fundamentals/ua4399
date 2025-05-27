import unittest
import functions
import functions_with_errors


class CustomTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"Test {test} is Passed")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"Test {test} is Failed")

    def addError(self, test, err):
        super().addError(test, err)
        print(f"Test {test} is Failed")


class BaseTestFunctions:
    module = None

    ## Test greeting_by_name
    def test_greeting_by_name(self):
        actual = self.module.greeting_by_name("Alex")
        expected = "Hello Alex!"
        self.assertEqual(actual, expected)

    ## Test get_symbol_position
    def test_get_symbol_position_found(self):
        actual = self.module.get_symbol_position("Hello", "e")
        expected = 2
        self.assertEqual(actual, expected)

    def test_get_symbol_position_not_found(self):
        actual = self.module.get_symbol_position("Hello", "a")
        expected = "Not found"
        self.assertEqual(actual, expected)

    def test_get_symbol_position_invalid_symbol(self):
        actual = self.module.get_symbol_position("Hello", "ab")
        expected = "Error! Symbol can be string with only one letter"
        self.assertEqual(actual, expected)

    ## Test merge
    def test_merge(self):
        dict1 = {"a": 1}
        dict2 = {"b": 2}
        result = self.module.merge(dict1, dict2)
        expected = {"a": 1, "b": 2}
        self.assertEqual(result, expected)

    def test_merge_dir_unchanged(self):
        dict1 = {"a": 1}
        dict2 = {"b": 2}
        self.module.merge(dict1, dict2)
        if self.module == functions:
            self.assertEqual(dict1, {"a": 1})
        else:
            self.assertEqual(dict1, {"a": 1, "b": 2})


class TestFunctions(BaseTestFunctions, unittest.TestCase):
    module = functions


class TestFunctionsWithErrors(BaseTestFunctions, unittest.TestCase):
    module = functions_with_errors


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestFunctions))
    suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(TestFunctionsWithErrors))

    runner = unittest.TextTestRunner(resultclass=CustomTestResult)
    runner.run(suite)