# <img width="48" height="48" alt="CrosswordStudio" src="https://github.com/user-attachments/assets/1d5b80d5-db82-4b24-8f1a-96c42c1f9567" style="vertical-align: middle;" /> Crossword Studio

**The privacy-focused, offline crossword generator; the greatest to ever exist.** *With Google Gemini/Gemma AI.*

## ✨ Why this tool?
Most crossword makers are either expensive subscriptions or clunky websites filled with ads. 
**Crossword Studio** is different:
* **0% Cloud Storage:** Your puzzles are saved directly to your hard drive (`/Puzzles` folder).
* **100% Portable:** It's a single `.exe` file. No installation. Run it from a USB drive.
* **Smart AI:** Bring your own free Google AI API key for unlimited smart generation.
* **Print Ready:** Export vector-perfect PDFs that never get cut off.
<img width="1905" height="933" alt="Screenshot 2026-02-04 153150" src="https://github.com/user-attachments/assets/aafb407d-6da2-45f6-8edd-b367b15ca8cd" />

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
python -m PyInstaller --noconsole --onefile --name "CrosswordStudio" --add-data "CrosswordStudio.html;." --icon "CrosswordStudio.ico" server.py
```

# 🖼️ Photo Gallery
<img width="1897" height="937" alt="Screenshot 2026-02-04 152604" src="https://github.com/user-attachments/assets/50266739-5c45-4f1f-a76c-dd62f1ee5e80" />
<img width="1909" height="932" alt="Screenshot 2026-02-04 152351" src="https://github.com/user-attachments/assets/20274148-501b-4033-ade0-b01713493253" />
<img width="1915" height="939" alt="Screenshot 2026-02-04 152146" src="https://github.com/user-attachments/assets/b2a9833e-240a-4acf-b76e-15daa234ca7f" />
<img width="2180" height="3150" alt="The 50 States of America CrosswordStudio" src="https://github.com/user-attachments/assets/ffdba6c9-3f78-4611-b9a7-42d71b6f466c" />
<img width="2180" height="3080" alt="The 50 States of America CrosswordStudio(2)" src="https://github.com/user-attachments/assets/fb50fe60-18e2-4089-8438-b45b54e363e6" />
<img width="1880" height="3380" alt="The 50 States of America CrosswordStudio(1)" src="https://github.com/user-attachments/assets/4b3ee566-cdbd-4201-a9c3-5e34356db249" />
<img width="2180" height="3080" alt="The 50 States of America CrosswordStudio Solution" src="https://github.com/user-attachments/assets/800b2244-b69c-44a9-842e-13429026b8a5" />
<img width="1916" height="932" alt="Screenshot 2026-02-04 153213" src="https://github.com/user-attachments/assets/913ee37b-23c8-4b9d-b785-a729c7a417bc" />
<img width="1905" height="933" alt="Screenshot 2026-02-04 153150" src="https://github.com/user-attachments/assets/f862e14a-6744-480f-bec9-5114964b84fc" />
<img width="1900" height="931" alt="Screenshot 2026-02-04 153047" src="https://github.com/user-attachments/assets/17ae4133-9e66-4685-9b2c-d52eb45179c8" />
<img width="1911" height="937" alt="Screenshot 2026-02-04 152955" src="https://github.com/user-attachments/assets/ad165c09-e666-46c0-a65e-a9c09998f102" />
<img width="1911" height="927" alt="Screenshot 2026-02-04 152904" src="https://github.com/user-attachments/assets/88798567-2358-4773-8837-fa7eb026d7c9" />
<img width="1868" height="898" alt="Screenshot 2026-02-04 152802" src="https://github.com/user-attachments/assets/b93451ef-e266-4ed9-a15b-93df64ce1fa5" />
<img width="1445" height="898" alt="Screenshot 2026-02-04 152734" src="https://github.com/user-attachments/assets/de057283-95fd-4296-a732-c832c2e695f5" />
<img width="1448" height="898" alt="Screenshot 2026-02-04 152711" src="https://github.com/user-attachments/assets/a95b677d-3486-41a5-8118-afccfea54db5" />
<img width="468" height="874" alt="Screenshot 2026-02-04 152647" src="https://github.com/user-attachments/assets/f4926fa0-92cd-4af9-93f9-49ff7d9059d3" />

