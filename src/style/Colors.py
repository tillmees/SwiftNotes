from PySide6.QtGui import QColor


class Colors:
    def __init__(self):
        self.Color1 = f"#799558"
        self.Color2 = f"#b0bf84"
        self.Color3 = f"#e17e44"
        self.Color4 = f"#f69d59"
        self.Color5 = f"#e8b449"
        self.Color6 = f"#d2838f"
        self.Color7 = f"#ae445a"
        self.Color8 = f"#732e54"
        self.Color9 = f"#216869"
        self.Color10 = f"#75a09b"

        self.color_mapping = {
            1: self.Color1,
            2: self.Color2,
            3: self.Color3,
            4: self.Color4,
            5: self.Color5,
            6: self.Color6,
            7: self.Color7,
            8: self.Color8,
            9: self.Color9,
            10: self.Color10,
        }

    def get_color_id_by_string(self, string):
        for key, val in self.color_mapping.items():
            if val == string:
                return key
        return None

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