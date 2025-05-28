import unittest
from unittest.mock import (
    MagicMock,
)  # MagicMock is used to create mock objects for testing
from app.cross_sum import validate_input, show_message, calculate_cross_sum
from tkinter import Entry, messagebox


class TestCrossSum(unittest.TestCase):
    def setUp(self):
        self.mock_entry = MagicMock(
            spec=Entry
        )  # Mocking the Entry widget with specification of Entry class

    def test_validate_input_valid_number(self):
        """Test that validate_input returns True for a valid number input."""

        self.assertTrue(validate_input("12345"))

    def test_validate_input_invalid_empty(self):
        """Test that validate_input returns False for an empty input."""

        self.assertFalse(validate_input(""))

    def test_validate_input_invalid_non_digit(self):
        """Test that validate_input returns False for a non-digit input."""
        self.assertFalse(validate_input("12a34"))

    def test_calculate_cross_sum_basic(self):
        """Test that calculate_cross_sum returns the correct sum of digits."""
        self.assertEqual(calculate_cross_sum("12345"), 15)

    def test_calculate_cross_sum_with_zeros(self):
        """Test that calculate_cross_sum correctly handles zeros."""
        self.assertEqual(calculate_cross_sum("0000"), 0)

    def test_calculate_cross_sum_with_non_digits(self):
        """Test that calculate_cross_sum ignores non-digit characters."""
        self.assertEqual(calculate_cross_sum("12a3b4"), 10)

    def test_show_message_valid(self):
        """Test that show_message calls showinfo with the correct parameters for valid input."""
        messagebox.showinfo = MagicMock()
        show_message(messagebox, "123")
        messagebox.showinfo.assert_called_with("Result", "6")

    def test_show_message_invalid_empty(self):
        """Test that show_message calls showerror for empty input."""
        messagebox.showerror = MagicMock()
        show_message(messagebox, "")
        messagebox.showerror.assert_called_with("Error", "Please enter a valid number.")

    def test_show_message_invalid_nondigit(self):
        """Test that show_message calls showerror for non-digit input."""
        messagebox.showerror = MagicMock()
        show_message(messagebox, "12a")
        messagebox.showerror.assert_called_with("Error", "Please enter a valid number.")
