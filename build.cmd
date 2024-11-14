
py -m nuitka --standalone --onefile --windows-console-mode=disable --enable-plugin=tk-inter^
 --product-name="Image overlay" --product-version=1.0.0 --file-description="Overlays an image on top of your screen frfr" --copyright="Copyright © 2024 Omena0. All rights reserved."^
 --output-dir="__build"^
 --deployment --python-flag="-OO" --python-flag="-S"^
 --output-filename="imageOverlay.exe"^
 main.py
