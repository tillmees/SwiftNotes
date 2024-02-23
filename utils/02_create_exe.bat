@echo OFF

call conda activate swift_notes_py3_10

cd ..
mkdir exe
cd exe
call pyinstaller ../src/main.py --onefile --noconsole

pause
exit