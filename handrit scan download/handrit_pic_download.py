# kleines Skript, um Einzel-Scans von Handschriften auf handrit.is herunter zu laden
# Die Bilder werden dorthin gespeichert, wo auch dieses Skript ausgeführt wird
# In der variable urlstring wird die url eines der Einzel-Scans abgelegt – die Zahl zwischen der Ms.-Sigle und 'SECONDARY_DISPLAY' wird durch den Platzhalter '{i} ersetzt
# Z. B.: myndir.handrit.is/file/Handrit.is/AM%20334%20fol./[→] 7 [←]/SECONDARY_DISPLAY
# In der übernächsten Zeile muss in 'range(x,y)' angegeben werden, welche Bilder man haben will (aus der Url entnehmen: x ist die Ziffer aus der Url des ersten Bilds; y = die ziffer aus der URL des letzten Bilds PLUS 1!)
import requests
for i in range(7,42): # ← hier Bereich definieren 
    # ↓ hier url einsetzen
    urlstr = f'https://myndir.handrit.is/file/Handrit.is/AM%20334%20fol./{i}/SECONDARY_DISPLAY'
    file = requests.get(urlstr)
    filename = file.headers['Content-Disposition'].split('=')
    filename = filename[1].strip('"')
    bild = requests.get(urlstr).content
    with open (filename,"wb") as t:
      t.write(bild)


