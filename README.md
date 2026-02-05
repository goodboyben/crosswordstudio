# Crossword Studio

**The privacy-focused, offline crossword generator; the greatest to ever exist.** *With Google Gemini/Gemma AI.*

## ✨ Why this tool?
Most crossword makers are either expensive subscriptions or clunky websites filled with ads. 
**Crossword Studio** is different:
* **0% Cloud Storage:** Your puzzles are saved directly to your hard drive (`/Puzzles` folder).
* **100% Portable:** It's a single `.exe` file. No installation. Run it from a USB drive.
* **Smart AI:** Bring your own free Google AI API key for unlimited smart generation.
* **Print Ready:** Export vector-perfect PDFs that never get cut off.

## 🚀 Quick Start
1.  Download the latest **`CrosswordStudio.exe`** from the Releases tab.
2.  Double-click to run. (A browser window will open automatically).
3.  Start building!

> Tip: You can also access a hosted version of the application at https://goodboyben.github.io/crosswordstudio. Note that when using the hosted page, the local auto-save to your `./Puzzles` folder will not be available — this mode is intended for convenient access on mobile devices.

## 🛠️ Features
* **AI Construction:** Type *"Ocean life"* and get a full puzzle in seconds.
* **Brute Force Optimizer:** Algorithms ensure maximum word interlock.
* **Local Auto-Save:** Never lose work. Versions saved as `Puzzle (1).json`, `Puzzle (2).json`.
* **Glassmorphism UI:** A beautiful, modern interface with Dark Mode support (quadruple-click the background anywhere for dark mode).
* **Play:** Fill in the crossword puzzle digitally within the application.
* **Export:** Save as PNG image or Print-ready PDF.

## 🔒 Privacy Note
This application runs a local Python server on your machine. 
* **Your Data:** Stored locally in `./Puzzles`.
* **Your API Key:** Stored locally in your browser's `localStorage`.
* **No Telemetry:** No data is sent to the developer.

## 📦 For Developers (Building from Source)
If you prefer to run the raw Python script or build the EXE yourself:

```bash
# 1. Install PyInstaller
pip install pyinstaller

# 2. Build the silent executable
python -m PyInstaller --noconsole --onefile --name "CrosswordStudio" --add-data "CrosswordStudio.html;." --add-data "CrosswordStudio.ico;." server.py
```
