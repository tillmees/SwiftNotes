import hashlib
from PySide6.QtCore import QDateTime
from PySide6.QtGui import QColor


def get_current_time_string():
    current_datetime = QDateTime.currentDateTime()
    current_time_string = current_datetime.toString("yyyy-MM-dd hh:mm:ss")
    return current_time_string

def get_hash_from_time(time_string):
    return hashlib.sha256(time_string.encode()).hexdigest()

def adjust_color(hex_color, factor=0.0, operation=None, transparency=1.0):
    """
    Adjusts the brightness of a given hex color by adding or subtracting a factor from each RGB component.
    """
    color = QColor(hex_color)
    r, g, b = color.red(), color.green(), color.blue()
    
    if operation == 'lighten':
        r = min(int(r + 255 * factor), 255)
        g = min(int(g + 255 * factor), 255)
        b = min(int(b + 255 * factor), 255)
    elif operation == 'darken':
        r = max(r - int(255 * factor), 0)
        g = max(g - int(255 * factor), 0)
        b = max(b - int(255 * factor), 0)
    else:
        pass
   
    a = transparency
    
    return f"rgba({r}, {g}, {b}, {a})"


def lighten_color(hex_color, factor=0.05):
    """
    Lightens a given hex color by adding a factor to each RGB component.
    """
    return adjust_color(hex_color, factor, 'lighten')


def darken_color(hex_color, factor=0.05):
    """
    Darkens a given hex color by subtracting a factor from each RGB component.
    """
    return adjust_color(hex_color, factor, 'darken')

def transparent_color(hex_color):
    return adjust_color(hex_color, transparency=0.5)