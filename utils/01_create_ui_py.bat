@echo OFF

call conda activate swift_notes_py3_10

call pyside6-rcc ../ui/resources.qrc -o 		../src/resources_rc.py
call pyside6-uic ../ui/add_edit_window.ui -o 	../src/ui_windows/add_edit_window_ui.py
call pyside6-uic ../ui/info_window.ui -o 		../src/ui_windows/info_window_ui.py
call pyside6-uic ../ui/main.ui -o 				../src/ui_windows/main_ui.py
call pyside6-uic ../ui/task.ui -o 				../src/ui_windows/task_ui.py

pause
exit