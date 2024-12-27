from django.test import TestCase

from libs.setting_utils import comma_separated_list, strtobool, strtofloat, strtoint


class StrToIntTest(TestCase):
    def test_strtobool_with_valid_input(self):
        # Test with valid input
        result = strtobool("yes")
        self.assertEqual(result, True)

    def test_strtobool_with_invalid_input(self):
        # Test with invalid input
        result = strtobool("invalid")
        self.assertEqual(result, False)

    def test_strtobool_with_none(self):
        # Test with None
        result = strtobool(None)
        self.assertEqual(result, False)

    def test_strtoint_with_valid_input(self):
        # Test with valid input
        result = strtoint("123")
        self.assertEqual(result, 123)

    def test_strtoint_with_invalid_input(self):
        # Test with invalid input
        result = strtoint("abc")
        self.assertIsNone(result)

    def test_strtoint_with_default_value(self):
        # Test with default value
        result = strtoint("abc", default=0)
        self.assertEqual(result, 0)

    def test_strtoint_with_none(self):
        # Test with None
        result = strtoint(None)
        self.assertIsNone(result)

    def test_strtofloat_with_valid_input(self):
        # Test with valid input
        result = strtofloat("123.45")
        self.assertEqual(result, 123.45)

    def test_strtofloat_with_invalid_input(self):
        # Test with invalid input
        result = strtofloat("abc")
        self.assertIsNone(result)

    def test_strtofloat_with_default_value(self):
        # Test with default value
        result = strtofloat("abc", default=0.0)
        self.assertEqual(result, 0.0)

    def test_strtofloat_with_none(self):
        # Test with None
        result = strtofloat(None)
        self.assertIsNone(result)

    def test_comma_separated_list_with_valid_input(self):
        # Test with valid input
        result = comma_separated_list("a,b,c")
        self.assertEqual(result, ["a", "b", "c"])

    def test_comma_separated_list_with_invalid_input(self):
        # Test with invalid input
        result = comma_separated_list("a,b,c,")
        self.assertEqual(result, ["a", "b", "c"])

    def test_comma_separated_list_with_none(self):
        # Test with None
        result = comma_separated_list(None)
        self.assertEqual(result, [])

    def test_comma_separated_list_with_empty_string(self):
        # Test with empty string
        result = comma_separated_list("")
        self.assertEqual(result, [])

    def test_comma_separated_list_with_whitespace(self):
        # Test with whitespace
        result = comma_separated_list(" ")
        self.assertEqual(result, [" "])
