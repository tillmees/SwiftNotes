@echo OFF

call conda activate py310_pyside6

call pyinstaller main.py --onefile --noconsole

pause
exit