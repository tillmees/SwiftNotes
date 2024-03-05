import sys
from PySide6.QtWidgets import QApplication

from classes.MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)

    main_window = MainWindow(app, version="0.1.0")
    main_window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()

