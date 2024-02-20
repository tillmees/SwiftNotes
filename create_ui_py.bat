@echo OFF

call conda activate py310_pyside6

call pyside6-rcc resources.qrc -o resources_rc.py

call pyside6-uic ui_windows/add_edit_window.ui -o ui_windows/add_edit_window_ui.py

call pyside6-uic ui_windows/info_window.ui -o ui_windows/info_window_ui.py

call pyside6-uic ui_windows/main.ui -o ui_windows/main_ui.py

call pyside6-uic ui_windows/task.ui -o ui_windows/task_ui.py

call pyside6-uic ui_windows/project.ui -o ui_windows/project_ui.py

pause
exit