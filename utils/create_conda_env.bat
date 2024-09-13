@echo OFF

echo create_conda_env.bat
echo ============================
echo.

echo create conda environment
set condaCreateCall=conda env create --file environment.yml
echo calling: %condaCreateCall%
echo.
call %condaCreateCall%

pause
exit