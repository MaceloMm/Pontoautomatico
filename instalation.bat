python.exe -m pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller
pyinstaller --onefile --icon=src/imagens/check.png --noconsole --add-data "src/imagens/check.png;src/imagens" ponto.py
pause