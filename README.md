# Progetto *marcatrice-csv2json-daemon*

Daemon che converte un file di punti .csv in .json (il file csv e' esportato utilizzando il software OpenAPC BeamConstruct)
Rispetto al file csv, il file json introduce:
- Numero di punti
- Punto massimo
- Punto minimo
- Coordinate di punti ordinate

Nota: si consiglia di utilizzare un ambiente di python virtuale (venv per esempio)
per utilizzare il progetto, e' necessario installare nell'ambiente virtuale:
- watchdog: pip install watchdog
- pyside: pip install PySide2

In data 02/04/2021, i pacchetti installati nell'ambiente virtuale sono i seguenti:

```
.\pip.exe list

Package                   Version
------------------------- --------
altgraph                  0.16.1
argh                      0.26.2
future                    0.17.1
importlib-metadata        3.10.0
macholib                  1.11
pathtools                 0.1.2
pefile                    2018.8.8
pip                       10.0.1
pyinstaller               4.2
pyinstaller-hooks-contrib 2021.1
PySide2                   5.12.2
pywin32-ctypes            0.2.0
PyYAML                    5.1
setuptools                39.1.0
shiboken2                 5.12.2
tailer                    0.4.1
typing-extensions         3.7.4.3
watchdog                  0.9.0
zipp                      3.4.1
```

Per la generazione dell'eseguibile, e' stato importante aggiornare *pyinstaller* all'ultima versione.

Per generare l'eseguibile, viene utilizzato il pacchetto *pyinstaller*:
```
pip install pyinstaller
```
Per generare l'eseguibile bisogna dare il comando:
```
.\venv\Scripts\pyinstaller.exe main.pyw --distpath .\build2\dist --workpath .\build2\build -n csv2json-0.5.0
```

L'opzione `-n` specifica il nome del file.

<!--
1. pyinstaller main.py (usanto il pyinstaller dell'ambiente virtuale)
2. pyinstaller main.py (usanto il pyinstaller dell'ambiente di sistema)

Possibile file batch
.\venv\Scripts\pyinstaller main.py --distpath .\build\dist --workpath .\build\build
pyinstaller main.py --distpath .\build\dist --workpath .\build\build

-->

## Comandi utili

il file di risorse e' stato creato da Qt Designer (View -> Resource Browser);

la conversione da .rcc a py e' fatta da questo comando:<br>
```
pyside2-rcc nomefile.rcc -o nomefile.py
```

la conversione da .ui a py e' fatta da questo comando:<br>
```
pyside2-uic nomefile.ui -o nomefile.py
```

Avvio in modalita' grafica (senza console)
rinominare il file `main.py` in `main.pyw`