@echo OFF

call conda activate swift_notes_py3_10

cd ..
mkdir exe
cd exe
call pyinstaller ../src/main.py --name "SwiftNotes" --icon="../ui/icons/swift-notes.ico" --onefile --noconsole

pause
exit