python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pyinstaller
cd src
python3 __create__databases.py
cd ..
pyinstaller --onefile --icon=src/imagens/check.png --noconsole --add-data "src/imagens/check.png;src/imagens" --add-data "src/cadastros.db;src" ponto.py
pause