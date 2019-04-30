# marcatrice-csv2json-daemon

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

Per generare l'eseguibile, e' necessario installare questi pacchetti:
- pyinstaller: pip install pyinstaller<br>
questo pacchetto va installato sia nell'ambiente virtuale che in quello reale;
per generare l'eseguibile bisogna dare i seguenti comandi:
1. pyinstaller main.py (usanto il pyinstaller dell'ambiente virtuale)
2. pyinstaller main.py (usanto il pyinstaller dell'ambiente di sistema)

Possibile file batch
.\venv\Scripts\pyinstaller main.py --distpath .\build\dist --workpath .\build\build
pyinstaller main.py --distpath .\build\dist --workpath .\build\build

Comandi utili

il file di risorse e' stato creato da Qt Designer (View -> Resource Browser);

la conversione da .rcc a py e' fatta da questo comando:<br>
pyside2-rcc nomefile.rcc -o nomefile.py

la conversione da .ui a py e' fatta da questo comando:<br>
pyside2-uic nomefile.ui -o nomefile.py