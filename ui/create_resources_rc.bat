@echo OFF

call conda activate swift_notes_py3_10

call pyside6-rcc ../ui/resources.qrc -o 		../src/resources_rc.py

pause
exit