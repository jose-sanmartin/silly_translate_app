@echo off
echo Verificando Python...
where python >nul 2>nul || (
    echo Instalando Python...
    start /wait "" "%~dp0python-installer.exe" /quiet InstallAllUsers=1 PrependPath=1
)

echo Clonando repositorio...
git clone https://github.com/jose-sanmartin/silly_translate_app.git

cd silly_translate_app
echo Instalando requerimientos...
pip install -r requirements.txt

echo Instalación completa. Ejecutando la aplicación...
python script.py
pause
