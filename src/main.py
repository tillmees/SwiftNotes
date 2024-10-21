import os
import sys

from PySide6.QtWidgets import QApplication

from windows.main_window.MainWindow import MainWindow

from settings.WindowSettingsHandler import WindowSettingsHandler
from settings.StyleSettingsHandler import StyleSettingsHandler
from settings.RecentFilesSettingsHandler import RecentFilesSettingsHandler


VERSION_MAJOR = 0
VERSION_MINOR = 1
VERSION_PATCH = 2


def main():

    # change the working directory to the directory of the executable
    # this ensures that the settings files will be created in the
    # correct location
    os.chdir(os.path.dirname(os.path.abspath(sys.executable)))

    filename = None
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if not filename.endswith(".todo"):
            # dont open the app on a non .todo file
            return
    
    # create singleton objects
    WindowSettingsHandler()
    StyleSettingsHandler()
    RecentFilesSettingsHandler()

    app = QApplication(sys.argv)
    version = f"{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}"
    main_window = MainWindow(app, version=version, filename=filename)
    main_window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()
