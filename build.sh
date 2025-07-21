#!/usr/bin/env bash
set -e

# 1) Crear entorno virtual limpio
python3 -m venv venv
source venv/bin/activate

# 2) Instalar dependencias + PyInstaller
pip install --upgrade pip
pip install -r requirements.txt pyinstaller

# 3) Empaquetar con PyInstaller
#    --onefile: un solo binario
#    --windowed: sin terminal
pyinstaller \
  --onefile \
  --windowed \
  --name test_pyqt \
  src/main.py

# 4) Preparar carpeta final
rm -rf dist_app
mkdir -p dist_app
cp dist/test_pyqt dist_app/

echo "✅ Ejecutable generado en dist_app/test_pyqt"
