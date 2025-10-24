@echo off
color 0A
cls

echo.
echo   ╔════════════════════════════════════════════════════════╗
echo   ║                                                        ║
echo   ║         🎬  EXTRACTOR DE FRAMES DE VIDEO  🎬          ║
echo   ║                                                        ║
echo   ╚════════════════════════════════════════════════════════╝
echo.
echo.
echo   👋 ¡Bienvenido!
echo.
echo   Esta aplicacion te permite extraer todos los frames
echo   de tus videos y guardarlos como imagenes PNG.
echo.
echo.
echo   📋 Antes de continuar, asegurate de:
echo.
echo      ✓ Tener Python instalado
echo      ✓ Tener tus videos en esta carpeta
echo.
echo.
echo   ════════════════════════════════════════════════════════
echo.

choice /C SN /M "  ¿Deseas iniciar la aplicacion ahora"

if errorlevel 2 (
    echo.
    echo   👋 ¡Hasta luego!
    timeout /t 2 /nobreak >nul
    exit
)

echo.
echo   🚀 Iniciando...
echo.

call INICIAR_APP.bat
