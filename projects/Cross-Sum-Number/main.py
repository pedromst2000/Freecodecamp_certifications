import sys
from app.gui import Window
import subprocess  # to run the GUI application


def run_app():
    """
    Run the GUI application for the Cross Sum Number project.
    When the windows is closed, will execute the automatic tests.
    """

    app = Window()
    app.__main__()  # Initialize the GUI application
    app.run()  # Start the main loop of the application


def run_tests():
    """
    Run the tests for the Cross Sum Number project.
    This function is called when the application is closed.
    """

    print("\n[Info] Running tests with unittest...")
    """
    The subprocess.call() function is used to run the unittest module as a script.
    sys.executable is the path to the Python interpreter,
    "-m unittest discover" is the command to discover and run tests,
    "-s tests" specifies the starting directory for test discovery,
    "-p test_*.py" specifies the pattern to match test files.
    """
    unittest_result = subprocess.call(
        [sys.executable, "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"]
    )
    print("\n[Info] Running tests with pytest...")

    """
    The subprocess.call() function is used to run pytest as a script.
    "pytest" is the command to run pytest,
    "tests/" specifies the directory containing the tests,
    "-v" enables verbose output.
    """

    pytest_result = subprocess.call([sys.executable, "-m", "pytest", "tests/test_gui.py", "-v"])

    if unittest_result == 0 and pytest_result == 0:
        print("\n[Info] ✅ All tests passed successfully!")
    else:
        print("\n[Error] ❌ Some tests failed. Please check the output above for details.")
        sys.exit(1)

if __name__ == "__main__":
    try:
        run_app()
    except Exception as e:
        print(f"\n[Error] An error occurred while running the application: {e}")
        sys.exit(1)
    finally:
        run_tests()  # Run tests after the application is closed