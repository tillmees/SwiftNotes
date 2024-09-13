@echo OFF

echo create_exe.bat
echo ============================
echo.

echo activate conda environment
call conda activate swift_notes_py3_10
echo.

echo create directory ./exe 
cd ..
mkdir exe
cd exe
echo.

echo create SwiftNotes.exe 
set pyinstallerCall=pyinstaller ../src/main.py --name "SwiftNotes" --icon="../ui/icons/swift-notes.ico" --onefile --noconsole
echo calling: %pyinstallerCall%
echo.
call %pyinstallerCall%

pause
exit