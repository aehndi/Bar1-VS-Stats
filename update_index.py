import os
import re

def generate_index():
    reports_dir = 'reports'
    if not os.path.exists(reports_dir):
        print("Kein 'reports' Ordner gefunden.")
        return

    reports = []
    # Durchsuche reports/YYYY/WW
    for year in sorted(os.listdir(reports_dir), reverse=True):
        year_path = os.path.join(reports_dir, year)
        if os.path.isdir(year_path):
            for week in sorted(os.listdir(year_path), reverse=True, key=lambda x: int(x) if x.isdigit() else 0):
                week_path = os.path.join(year_path, week)
                if os.path.isdir(week_path):
                    html_file = None
                    md_file = None
                    for file in os.listdir(week_path):
                        if file.endswith('.html'):
                            html_file = os.path.join(week_path, file).replace('\\', '/')
                        elif file.endswith('.md'):
                            md_file = os.path.join(week_path, file).replace('\\', '/')
                    
                    if html_file or md_file:
                        reports.append({
                            'label': f"{year} KW{week}",
                            'html': html_file,
                            'md': md_file
                        })

    # HTML generieren
    list_items = ""
    for r in reports:
        html_link = f'<a href="{r["html"]}">HTML-Bericht</a>' if r['html'] else ""
        md_link = f'<a href="{r["md"]}">Markdown-Quelle</a>' if r['md'] else ""
        list_items += f"""
            <li>
                <span class="date">{r['label']}</span>
                <div class="links">
                    {html_link}
                    {md_link}
                </div>
            </li>"""

    template = f"""<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bar1-VS-Stats - Wöchentliche Berichte</title>
    <style>
        body {{ font-family: sans-serif; line-height: 1.6; max-width: 800px; margin: 0 auto; padding: 20px; }}
        h1 {{ border-bottom: 2px solid #eee; }}
        ul {{ list-style-type: none; padding: 0; }}
        li {{ margin-bottom: 10px; padding: 10px; border: 1px solid #ddd; border-radius: 4px; }}
        .date {{ font-weight: bold; }}
        .links a {{ margin-right: 15px; text-decoration: none; color: #0066cc; }}
        .links a:hover {{ text-decoration: underline; }}
    </style>
</head>
<body>
    <h1>Bar1-VS-Stats - Archiv</h1>
    <p>Hier finden Sie die wöchentlichen Statistiken.</p>
    
    <div id="report-list">
        <ul>{list_items}
        </ul>
    </div>
</body>
</html>"""

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(template)
    print("index.html wurde aktualisiert.")

if __name__ == "__main__":
    generate_index()
