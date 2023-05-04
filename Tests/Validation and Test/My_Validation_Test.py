import My_Validation
import unittest

class TestMyValidation(unittest.TestCase):
    def test_is_valid_length(self):
        # Test a valid length
        result = My_Validation.is_valid_length("1234567890", 10)
        self.assertTrue(result)

        # Test an invalid length
        result = My_Validation.is_valid_length("1234567890", 5)
        self.assertFalse(result)

    def test_is_valid_integer(self):
        # Test a valid integer
        result = My_Validation.is_valid_integer("1234567890")
        self.assertTrue(result)

        # Test an invalid integer
        result = My_Validation.is_valid_integer("1234567890a")
        self.assertFalse(result)

    def test_is_valid_float(self):
        # Test a valid float
        result = My_Validation.is_valid_float("1234567890.0")
        self.assertTrue(result)

        # Test an invalid float
        result = My_Validation.is_valid_float("1234567890")
        self.assertFalse(result)

    def test_is_valid_string(self):
        # Test a valid string
        result = My_Validation.is_valid_string("1234567890")
        self.assertTrue(result)

        # Test an invalid string
        result = My_Validation.is_valid_string("1234567890a")
        self.assertFalse(result)

    def test_is_valid_date(self):
        # Test a valid date
        result = My_Validation.is_valid_date("01-01-20")
        self.assertTrue(result)

        # Test an invalid date
        result = My_Validation.is_valid_date("01-01-2020a")
        self.assertFalse(result)

    def test_is_valid_email(self):
        # Test a valid email
        result = My_Validation.is_valid_email("mrrawley@gmail.com")
        self.assertTrue(result)

        # Test an invalid email
        result = My_Validation.is_valid_email("mrrawley@gmail")
        self.assertFalse(result)

    def test_is_valid_range(self):
        # Test a valid range
        result = My_Validation.is_valid_range("1234567890", 5, 10)
        self.assertTrue(result)

        # Test an invalid range
        result = My_Validation.is_valid_range("1234567890", 15, 20)
        self.assertFalse(result)
