import pytest
from unittest.mock import patch
import tkinter as tk
from app.gui import Window


@pytest.fixture  # to create a fixture for the GUI application
def app():
    gui_app = Window()
    gui_app.__main__()  # Initialize the GUI application
    yield gui_app  # yield the app instance for testing
    gui_app.window.destroy()  # clean up after tests


def test_window_title(app):
    """Test that the window title is set correctly."""

    assert app.window.title() == "Cross Sum Number"


def test_window_geometry(app):
    """Test that the window geometry is set to 600x400."""
    assert app.window.geometry().startswith("600x400")



def test_initial_vars(app):
    """Test that input_var and result_var are initialized as StringVar."""
    assert isinstance(app.input_var, tk.StringVar)
    assert isinstance(app.result_var, tk.StringVar)


def test_canvas_created(app):
    """Test that the canvas is created and has a non-negative width."""
    assert isinstance(app.canvas, tk.Canvas)
    assert app.canvas.winfo_width() >= 0


def test_window_resizable_false(app):
    """Test that the window is not resizable."""
    resizable_x, resizable_y = app.window.resizable()
    assert not resizable_x and not resizable_y


def test_button_exists(app):
    """Test that the calculate button exists and has the correct text."""
    assert app.button_calculate is not None
    assert app.button_calculate.cget("text") == "Calculate"


def test_input_field_exists(app):
    """Test that the input field exists and is an Entry widget."""
    assert hasattr(app, "input_number")
    assert isinstance(app.input_number, tk.Entry)


def test_button_command_calls_functionality(app):
    with patch("app.gui.show_message") as mock_show_message:
        app.input_var.set("456")
        app.handle_calculate()  # Simulate button click
        mock_show_message.assert_called_once()
