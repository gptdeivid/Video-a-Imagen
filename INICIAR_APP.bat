@echo off
title Extractor de Frames - Inicializador
color 0A

echo ========================================
echo    EXTRACTOR DE FRAMES DE VIDEO
echo ========================================
echo.

REM Verificar si Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python no esta instalado en tu sistema.
    echo Por favor, descarga e instala Python desde:
    echo https://www.python.org/downloads/
    echo.
    echo Asegurate de marcar "Add Python to PATH" durante la instalacion.
    pause
    exit /b 1
)

echo [OK] Python detectado
echo.

REM Verificar si pip esta disponible
pip --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] pip no esta disponible
    pause
    exit /b 1
)

echo [OK] pip detectado
echo.

REM Verificar si Flask esta instalado
python -c "import flask" >nul 2>&1
if errorlevel 1 (
    echo [INSTALANDO] Instalando dependencias...
    echo Esto puede tomar unos minutos la primera vez...
    echo.
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] Hubo un problema al instalar las dependencias
        pause
        exit /b 1
    )
    echo.
    echo [OK] Dependencias instaladas correctamente
) else (
    echo [OK] Dependencias ya instaladas
)

echo.
echo ========================================
echo   INICIANDO SERVIDOR WEB...
echo ========================================
echo.
echo La aplicacion se abrira automaticamente en tu navegador
echo En la direccion: http://localhost:5000
echo.
echo IMPORTANTE: NO CIERRES ESTA VENTANA mientras uses la aplicacion
echo Para detener el servidor, presiona Ctrl+C
echo.
echo ========================================
echo.

REM Esperar 2 segundos y abrir el navegador
timeout /t 2 /nobreak >nul
start http://localhost:5000

REM Iniciar el servidor Flask
python app.py

pause
