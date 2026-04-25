# Bar1-VS-Stats

Dieses Projekt dient zur Archivierung und Anzeige von wöchentlichen Statistiken (Markdown und HTML).

## Struktur

Die Berichte werden im Ordner `reports/` abgelegt, unterteilt nach Jahren und Kalenderwochen:
`reports/YYYY/WW/`

## Nutzung

1. Erstellen Sie einen neuen Ordner unter `reports/YYYY/WW/` (z.B. `reports/2026/18/`).
2. Kopieren Sie Ihre HTML- und Markdown-Dateien in diesen Ordner.
3. Die `index.html` im Hauptverzeichnis wird automatisch durch eine GitHub Action aktualisiert, sobald Sie die Dateien pushen.

### Automatisierung
Es ist ein Python-Skript `update_index.py` und ein GitHub Workflow vorhanden, die automatisch die `index.html` basierend auf den Inhalten im `reports/` Ordner neu generieren.

### Beispiel Struktur
```
reports/
  2026/
    17/
      ranking.html
      ranking.md
```

## Veröffentlichung
Die Dateien sind über GitHub Pages (oder einen anderen Webserver) browsbar.
