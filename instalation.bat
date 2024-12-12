python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip install pyinstaller
python scr\__create__databases.py
pyinstaller --onefile --icon=src/imagens/check.png --noconsole --add-data "src/imagens/check.png;src/imagens" --add-data "src/cadastros.db;src" ponto.py
pause