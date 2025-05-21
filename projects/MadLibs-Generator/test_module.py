import unittest
import generator
from classes.Generator import Generator
from unittest.mock import patch


class TestGenerator(unittest.TestCase):
    def setUp(self):
        """
        Set up the test case with a sample Generator object.
        """
        self.generator = Generator("Paris", "beautiful", "cat", "run", "happy")

    @patch("builtins.open")
    @patch(
        "classes.Generator.random.choice",
        return_value="In the {place}, a {adjective} {noun} decided to {verb}, feeling very {emotion}.",
    )
    def test_generate_fixed_template(self, mock_random, mock_open):
        """
        Test the generate method with a fixed story template.
        """
        # Mock file read to return multiple templates
        mock_open.return_value.__enter__.return_value.read.return_value = (
            "In the {place}, a {adjective} {noun} decided to {verb}, feeling very {emotion}.\n"
            "Once upon a time, a {adjective} {noun} was found in the {place}, trying to {verb} because it was {emotion}.\n"
            "Deep in the {place}, a {noun} felt {emotion} and chose to {verb} in a {adjective} way.\n"
            "The {adjective} {noun} went to the {place} to {verb}, overwhelmed by {emotion}.\n"
            "At the {place}, a {emotion} {noun} attempted to {verb} with a {adjective} spirit."
        )

        result = self.generator.generate()
        expected = "In the Paris, a beautiful cat decided to run, feeling very happy."
        self.assertEqual(result, expected)

    @patch("builtins.open")
    def test_generate_random_template_structure(self, mock_open):
        """
        Test the generate method with real randomness,
        checking that placeholders are replaced properly.
        """
        mock_open.return_value.__enter__.return_value.read.return_value = (
            "In the {place}, a {adjective} {noun} decided to {verb}, feeling very {emotion}.\n"
            "Once upon a time, a {adjective} {noun} was found in the {place}, trying to {verb} because it was {emotion}.\n"
            "Deep in the {place}, a {noun} felt {emotion} and chose to {verb} in a {adjective} way.\n"
            "The {adjective} {noun} went to the {place} to {verb}, overwhelmed by {emotion}.\n"
            "At the {place}, a {emotion} {noun} attempted to {verb} with a {adjective} spirit."
        )

        result = self.generator.generate()

        # Check that there are no placeholders left
        self.assertNotRegex(result, r"{\w+}")

        # Check that all inputs appear in result
        for word in ["Paris", "beautiful", "cat", "run", "happy"]:
            self.assertIn(word, result)

    @patch(
        "classes.Generator.random.choice",
        return_value="Once upon a time in {place}, there was a {adjective} {noun} who loved to {verb} and felt very {emotion}.",
    )
    @patch("builtins.input", side_effect=["Paris", "beautiful", "cat", "run", "happy"])
    @patch("builtins.open")
    def test_start_generator(self, mock_open, mock_input, mock_random):
        """
        Test the start_generator function with fixed input and template.
        """
        mock_open.return_value.__enter__.return_value.read.return_value = (
            "Once upon a time in {place}, there was a {adjective} {noun} who loved to {verb} and felt very {emotion}.\n"
            "In the {place}, a {adjective} {noun} decided to {verb}, feeling very {emotion}.\n"
            "Deep in the {place}, a {noun} felt {emotion} and chose to {verb} in a {adjective} way.\n"
            "The {adjective} {noun} went to the {place} to {verb}, overwhelmed by {emotion}.\n"
            "At the {place}, a {emotion} {noun} attempted to {verb} with a {adjective} spirit."
        )

        with patch("builtins.print") as mock_print:
            generator.start_generator()
            mock_print.assert_any_call("Welcome to the Mad Libs game!")
            mock_print.assert_any_call("Please provide the following words:")
            mock_print.assert_any_call("Here is your story:")
            mock_print.assert_any_call(
                "Once upon a time in Paris, there was a beautiful cat who loved to run and felt very happy."
            )


if __name__ == "__main__":
    unittest.main()
