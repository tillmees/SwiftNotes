import os
import sys
from PySide6.QtWidgets import QApplication

from classes.MainWindow import MainWindow


def main():
    app = QApplication(sys.argv)

    # with open(os.path.join("ui_windows", "style_dark.qss")) as style_file:
    #     style_sheet = style_file.read()
    # app.setStyleSheet(style_sheet)

    main_window = MainWindow(app)
    main_window.show()

    app.exec()

    # sys.exit(
    #     app.exec()
    # )


if __name__ == "__main__":
    main()

