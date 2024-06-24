import sys

from PySide6.QtWidgets import QApplication

from windows.main_window.MainWindow import MainWindow

from settings.WindowSettingsHandler import WindowSettingsHandler
from settings.StyleSettingsHandler import StyleSettingsHandler


VERSION_MAJOR = 0
VERSION_MINOR = 1
VERSION_PATCH = 0
WINDOW_SETTINGS_FILENAME = "swiftnotes_window.json"
STYLE_SETTINGS_FILENAME = "swiftnotes_style.json"


def main():

    # create singleton objects
    WindowSettingsHandler(WINDOW_SETTINGS_FILENAME)
    StyleSettingsHandler(STYLE_SETTINGS_FILENAME)

    app = QApplication(sys.argv)
    version = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"
    main_window = MainWindow(app, version=version)
    main_window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()
