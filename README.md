# Monkey Moves
#### Video Demo:  <URL HERE>
#### Description:

Monkey Moves is a Pygame-based game where the player controls a character using hand gestures detected by a camera. The goal is to avoid obstacles and collect items while progressing through obstacles that are progressively increasing in speed. 

## Features

- **Hand Gesture Controls**: Use one hand and the gestures detected by the camera to control the player character.
- **Dynamic Gameplay**: Obstacles and collectible items spawn dynamically, providing a unique gameplay experience each time.
- **Scoring System**: Keep track of your score as you progress through the game.
- **Start and End Screens**: Clearly defined start and end screens provide a smooth user experience.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 2.9
- Pygame
- mediapipe
- OpenCV

Extra: Make sure you have a camera accessible for CV2, either internal or external. Using WSL2 with an integrated laptop camera will not work.

### Installation

   ```sh
   git clone https://github.com/your_username/Murats-Game.git

pip install pygame mediapipe opencv-python-headless

python game.py
