**Aktueller Ordnersturkturplan:**
rpg_game/
│-- assets/                   # Enthält Grafiken, Sounds, evtl. Fonts
│   ├── images/               # Sprites für Spieler, NPCs, Gegner, Objekte
│   ├── sounds/               # Soundeffekte & Musik
│-- data/                     # Speicherdaten (z. B. SQLite-DB)
│-- scripts/                  # Enthält Python-Module für verschiedene Spielkomponenten
│   ├── __init__.py           # Damit "scripts" als Paket erkannt wird
│   ├── main.py               # Startpunkt des Spiels
│   ├── settings.py           # Globale Spielkonfiguration (z. B. Bildschirmgröße)
│   ├── game.py               # Zentrale Spielsteuerung
│   ├── player.py             # Spieler-Logik (Bewegung, Inventar)
│   ├── npc.py                # NPC-Logik (Händler, Dorfbewohner)
│   ├── enemy.py              # Gegner-KI und Kampfmechanik
│   ├── map.py                # Weltkarte & Umgebungslogik
│   ├── ui.py                 # Benutzeroberfläche (Inventar, Menü, Dialoge)
│   ├── quest.py              # Quest-System
│   ├── save_system.py        # Speichersystem mit SQLite
│-- tests/                    # Tests für verschiedene Module
│-- README.md                 # Projektbeschreibung
│-- requirements.txt          # Liste von Python-Abhängigkeiten




**Projekt: 2D-Rollenspiel mit Pygame**

### **Allgemeine Projektinformationen**
- **Ersteller**: Benedikt
- **Interessen & Kenntnisse**: Benedikt interessiert sich für Python, Pygame, Data Science (z. B. SQL) und Künstliche Intelligenz, darunter neuronale Netzwerke und genetische KI.
- **Programmiersprachen & Tools**: 
  - Python als Hauptprogrammiersprache
  - Pygame für die grafische Darstellung
  - SQL für Speicherung von Spielständen
  - Visual Studio Code mit GitHub Copilot zur Entwicklung
- **Projektziel**: Entwicklung eines 2D-Rollenspiels mit einer lebendigen Spielwelt, Gegnern, Handelssystem und KI-Elementen

### **Spielidee & Konzept**
- **Genre**: 2D-Rollenspiel mit einer offenen Welt
- **Setting**: Eine mittelalterlich-märchenhafte Welt, die Magie und mechanische Apparaturen enthält
- **Ziel des Spiels**: Der Spieler soll durch verschiedene Aufgaben und Handel genug Geld verdienen, um eine Schatzkarte zu erwerben
- **Spielmechanik**:
  - Erkunden einer Welt mit verschiedenen Orten
  - Sammeln von Ressourcen (Holz, Kräuter, Erze, etc.)
  - Kämpfen gegen Gegner
  - Handel treiben
  - Reisen nur über Lagerfeuer möglich (dienen als Portale)
  - Fortschritt speichern nur an Lagerfeuern

### **Spielwelt & Orte**
- **Startpunkt**: Spieler beginnt in einer **Holzhütte** außerhalb des Dorfes
- **Reisemöglichkeiten nur durch Lagerfeuer**
- **Orte & ihre Funktionen**:
  - **Hütte** → Startpunkt, von hier kann man ins Dorf reisen
  - **Dorf** → Handel, Quests, NPCs, Ausgangspunkt für Reisen
  - **Wiese** → Sammeln von Kräutern
  - **Wald** → Sammeln von Holz, Begegnung mit Gegnern
  - **Dunkler Wald** → Stärkere Gegner, Zugang zur Höhle
  - **Höhle** → Miniboss-Kampf
  - **Berg** → Sammeln von Stein
  - **Mine** → Abbau von Erzen
  - **Tiefe Mine** → Stärkere Gegner, seltene Erze

### **Spielmechaniken**
#### 1. Charaktersteuerung
- **Bewegung**: Pfeiltasten
- **Kampf**: Nahkampf mit Schwert (spätere Erweiterung möglich)
- **Attribute des Charakters**:
  - Leben
  - Schaden
  - Geschwindigkeit
  - Coins (Währung)
  - Inventar (Waffen, Rüstungen, Tränke)

#### 2. Gegner
- **Gegnerische Wesen in der Welt**:
  - Goblins
  - Orks
  - Zwerge
  - Wölfe
  - Böse Bäume
  - Stärkere Monster in der Tiefenmiene und im Dunklen Wald
  - **Miniboss in der Höhle**

#### 3. Ressourcenabbau & Handel
- **Ressourcen sammeln**:
  - **Wiese** → Kräuter
  - **Wald** → Holz + Gegner
  - **Berg** → Stein
  - **Mine/Tiefe Mine** → Erze + stärkere Gegner
- **Handelssystem**:
  - Anfangs feste Preise für Waren
  - Später dynamisches Wirtschaftssystem (Händler-KI passt Preise an)

#### 4. Künstliche Intelligenz (KI)
- Unterschiedliche KIs:
  - **Monster-KI**: Feinde greifen den Spieler an
  - **NPC-KI**: Händler verkaufen Waren und interagieren mit dem Spieler
- Späteres Ziel: 
  - Entwicklung einer KI, die das Spiel eigenständig durchspielt und daraus lernt
  - Möglicherweise Einsatz genetischer Algorithmen

#### 5. Speichersystem
- Spielstand kann nur an **Lagerfeuern** gespeichert werden
- Nutzung von **SQL** für die Speicherung von Fortschritt & Inventar

#### 6. Quests & Fortschritt
- Der Spieler erhält Quests, z. B.:
  - **Sammelaufgaben** (Kraeuter für Händler)
  - **Handelsaufträge** (Bringe Holz ins Dorf)
  - **Monsterbesiegequests**
- **Kein Level-System**, sondern Fortschritt über bessere Ausrüstung

### **Grafik & Darstellung**
- **Externe, frei verfügbare Assets** werden genutzt
- **Top-Down-Perspektive** für einfachere Umsetzung
- Spieler kann sich frei in der 2D-Welt bewegen

---

### **Nächste Schritte**
1. **Projektstruktur aufsetzen** (Ordnerstruktur, erste Python-Dateien anlegen)
2. **Grundlegendes Spielfenster mit Pygame erstellen**
3. **Bewegung des Charakters implementieren**
4. **Einfache Umgebung mit ersten Objekten & Kollisionen erstellen**
5. **Gegner & Kampfmechanik hinzufügen**
6. **Interaktion mit NPCs & Handelssystem umsetzen**
7. **Speicherung & Quest-System integrieren**

Falls noch Ergänzungen oder Änderungen gewünscht sind, einfach Bescheid geben!
