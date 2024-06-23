import sys

from PySide6.QtWidgets import QApplication

from main_window.MainWindow import MainWindow
from settings.WindowSettingsHandler import WindowSettingsHandler
from settings.StyleSettingsHandler import StyleSettingsHandler


VERSION_MAJOR = 0
VERSION_MINOR = 1
VERSION_PATCH = 0
WINDOW_SETTINGS_FILENAME = "swiftnotes_window.json"
STYLE_SETTINGS_FILENAME = "swiftnotes_style.json"


def main():
    app = QApplication(sys.argv)

    version = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"
    window_settings = WindowSettingsHandler(WINDOW_SETTINGS_FILENAME)
    style_settings = StyleSettingsHandler(STYLE_SETTINGS_FILENAME)

    main_window = MainWindow(app, version=version, settings=window_settings, style_settings=style_settings)
    main_window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()
