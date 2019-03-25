# marcatrice-csv2json-daemon

Daemon che converte un file di punti .csv in .json (il file csv e' esportato utilizzando il software OpenAPC BeamConstruct)
Rispetto al file csv, il file json introduce:
- Numero di punti
- Punto massimo
- Punto minimo
- Coordinate di punti ordinate

Nota: si consiglia di utilizzare un ambiente di python virtuale (venv per esempio)
per utilizzare il progetto, e' necessario installare:
- watchdog: pip install watchdog
- pyside: pip install PySide2
