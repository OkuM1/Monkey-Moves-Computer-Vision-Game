# 🐵 Monkey Moves  
![Python](https://img.shields.io/badge/python-3.9+-blue.svg) ![Pygame](https://img.shields.io/badge/pygame-2.x-orange) ![Open Source Love](https://img.shields.io/badge/PRs-welcome-brightgreen.svg) ![License: MIT](https://img.shields.io/badge/license-MIT-lightgrey.svg)

> **Hand-gesture-controlled endless-runner built with Pygame, MediaPipe & OpenCV.**  
> Dodge obstacles, collect bananas, and let your webcam be the gamepad!

[🎞 Video Demo](https://www.youtube.com/watch?v=0VEA0qOUKeI)

---

## 📑 Table of Contents
1. [Features](#-features)  
2. [Gameplay & Controls](#-gameplay--controls)  
3. [Quick Start](#-quick-start)  
4. [Project Layout](#-project-layout)  
5. [Design Highlights](#-design-highlights)  
6. [Contributing](#-contributing)  
7. [Roadmap](#-roadmap)  
8. [License & Credits](#-license--credits)

---

## 🚀 Features
- **Natural hand-gesture input** via **MediaPipe Hands** (one-hand control).
- **Procedural obstacle & item spawner** — every run is unique.
- **Smooth difficulty scaling:** game speed and spawn rate increase over time.
- **Score & high-score tracking** with on-screen HUD.
- **Polished UX:** animated start, pause, and game-over screens with sound FX.
- **Cross-platform:** tested on Windows, macOS, Linux with Python 3.9+.

---

## 🎮 Gameplay & Controls
| Gesture | Action                |
|---------|-----------------------|
| ✊ Fist  | **Jump** (avoid ground obstacles) |
| 🖐️ Palm | **Glide / Slow fall** (longer airtime) |
| 🤚 Swipe Left / Right* | **Lane change** (sidestep obstacles) |

\* Swipe detection is derived from horizontal palm-center velocity.

 Credits

   Developed locally in VS Code

   Assisted by ChatGPT for logic validation & troubleshooting

   Resources:

   Pygame Documentation

   MediaPipe Hands

   OpenCV Docs
---

## ⚡ Quick Start

### 1. Prerequisites
| Package | Tested Version |
|---------|---------------|
| Python  | **3.9 – 3.12** |
| Pygame  | 2.5 |
| MediaPipe | 0.10 |
| OpenCV-Python-Headless | 4.10 |

A USB or integrated camera must be accessible to OpenCV.  
*(WSL2 cannot access host webcams — run natively on Windows/Linux/macOS).*

### 2. Installation
```bash
  git clone https://github.com/OkuM1/Monkey-Moves-Computer-Vision-Game.git
  cd Monkey-Moves-Computer-Vision-Game
  
  # Create a virtual env (recommended)
  python -m venv .venv
  source .venv/bin/activate      # Windows: .venv\Scripts\activate
  
  # Install runtime dependencies
  pip install -r requirements.txt
  
  python game.py           # Starts the game with default settings

