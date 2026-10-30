# 🏛️ Talos — Desktop GUI OCR Automator

> **Talos** (derived from the mythic bronze automaton of Crete)

---

## ⚡ Overview

**Talos** (`AutomatonV2`) automates targeted cross-platform messaging and payload delivery in desktop environments (e.g., Telegram Desktop, WhatsApp Desktop). 

Unlike standard window-coordinate automations that break when window positions shift, Talos dynamically parses client interface regions using **Tesseract Optical Character Recognition (OCR)**, image manipulation pipelines, and visual template matching to identify interactive controls and target contacts on the fly.

---

## ✨ Key Features

- **Dynamic OCR Target Matching**: Uses `pytesseract` to extract and parse account text inside application sidebars in real time.
- **Advanced Image Preprocessing**: Enhances raw screenshots through 4x Lanczos upscaling, grayscale conversion, color inversion, and binary thresholding for maximum OCR text extraction accuracy.
- **Spatial Memory & Deduplication**: Maintains a global coordinate registry (`clicked_positions`) with tolerance thresholds to avoid repeated clicks on processed UI elements.
- **Automatic Fallback Scrolling**: Detects missing sidebar targets and executes programmatic scroll passes with attempt limits to find off-screen accounts.
- **Template-Based UI Recognition**: Employs `pyautogui.locateOnScreen` for dynamic visual control identification (e.g., identifying target chat interfaces).
- **Interactive Execution Guard**: Utilizes global keyboard hooks (`keyboard` module) enabling real-time human-in-the-loop control (`Enter` to log success, `Esc` to skip/abort).

---

## 🛠️ Tech Stack

* **Core Runtime**: Python 3.8+
* **GUI & Window Control**: `PyGetWindow`, `pyautogui`, `pyperclip`
* **Computer Vision & Image Processing**: `pytesseract`, `Pillow (PIL)`
* **Event Hooks & Diagnostics**: `keyboard`, `tkinter`

---

## 🚀 Getting Started

### 1. Prerequisites
- **Tesseract OCR Engine**: Download and install [Tesseract OCR for Windows](https://github.com/UB-Mannheim/tesseract/wiki).
- Update the path to your `tesseract.exe` inside `AutomatonV2.py`:
  ```python
  pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
