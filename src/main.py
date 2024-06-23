import sys

from PySide6.QtWidgets import QApplication

from main_window.MainWindow import MainWindow
from settings.SettingsHandler import SettingsHandler


VERSION_MAJOR = 0
VERSION_MINOR = 1
VERSION_PATCH = 0
SETTINGS_FILENAME = "swiftnotes_settings.json"


def main():
    app = QApplication(sys.argv)

    version = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"
    settings = SettingsHandler(SETTINGS_FILENAME)

    main_window = MainWindow(app, version=version, settings=settings)
    main_window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()
