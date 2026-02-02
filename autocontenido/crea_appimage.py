#!/usr/bin/env python3
import os
import shutil
import subprocess
import sys

# ---------------- CONFIG ----------------
APPNAME = "AlgorandWallet"
APPDIR = "MyWallet.AppDir"
BIN_NAME = "AlgorandWallet"
ENTRYPOINT = "main.py"
ICON_FILE = "bitcoin.png"
#descargala del github.
# https://github.com/AppImage/appimagetool/releases/download/1.9.1/appimagetool-x86_64.AppImage
# y copiala den el dir. sup.
APPIMAGETOOL = "../appimagetool-x86_64.AppImage"
# ---------------------------------------


def run(cmd):
    print(">", " ".join(cmd))
    subprocess.run(cmd, check=True)


# ---------- PASO 0: limpiar ----------
if os.path.exists(APPDIR):
    shutil.rmtree(APPDIR)

os.makedirs(f"{APPDIR}/usr/bin", exist_ok=True)

# ---------- PASO 1: PyInstaller ----------
print("🔧 Compilando binario con PyInstaller...")
run([
    "pyinstaller",
    "--onefile",
    "--windowed",
    "--name", BIN_NAME,
    ENTRYPOINT
])

# ---------- PASO 2: copiar binario ----------
dist_bin = f"dist/{BIN_NAME}"
if not os.path.exists(dist_bin):
    raise RuntimeError("❌ PyInstaller no generó el binario")

shutil.copy(dist_bin, f"{APPDIR}/usr/bin/{BIN_NAME}")
print("✅ Binario copiado")

# ---------- PASO 3: icono ----------
icon_dst = f"{APPDIR}/bitcoin.png"
shutil.copy(ICON_FILE, icon_dst)
print("✅ Icono copiado")

# ---------- PASO 4: AppRun ----------
with open(f"{APPDIR}/AppRun", "w") as f:
    f.write(f"""#!/bin/bash
HERE="$(dirname "$(readlink -f "$0")")"
exec "$HERE/usr/bin/{BIN_NAME}" "$@"
""")
os.chmod(f"{APPDIR}/AppRun", 0o755)
print("✅ AppRun creado")

# ---------- PASO 5: .desktop ----------
with open(f"{APPDIR}/{APPNAME}.desktop", "w") as f:
    f.write(f"""[Desktop Entry]
Type=Application
Name={APPNAME}
Exec=AppRun
Icon=bitcoin
Categories=Finance;
""")
print("✅ .desktop creado")

# ---------- PASO 6: AppImage ----------
print("📦 Creando AppImage...")
run([APPIMAGETOOL, APPDIR])

print("🎉 AppImage listo")

