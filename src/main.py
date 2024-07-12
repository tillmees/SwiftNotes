import sys

from PySide6.QtWidgets import QApplication

from windows.main_window.MainWindow import MainWindow

from settings.WindowSettingsHandler import WindowSettingsHandler
from settings.StyleSettingsHandler import StyleSettingsHandler


VERSION_MAJOR = 0
VERSION_MINOR = 1
VERSION_PATCH = 0


def main():

    # create singleton objects
    WindowSettingsHandler()
    StyleSettingsHandler()

    filename = sys.argv[1] if len(sys.argv) > 1 else None

    app = QApplication(sys.argv)
    version = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"
    main_window = MainWindow(app, version=version, filename=filename)
    main_window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()
