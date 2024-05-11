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

#### Files

game.py: This is the main Python script that contains the game logic, including the player controls, obstacle spawning, scoring system, and game state management.

images/: This directory contains the images used in the game, such as the player character, obstacles, background, and start/end screens.

README.md: This file contains the project documentation, including a description of the game, installation instructions, and file descriptions.

#### Design 

Python 2.9
Python 2.9 was chosen as the language for this project due to compatibility reasons with existing libraries and dependencies. While Python 3.x is the recommended version, some libraries may not yet fully support it, and compatibility issues could arise.

Pygame
Pygame was chosen as the game development framework due to its simplicity and ease of use. It provides a high-level interface for handling graphics, sound, and user input, allowing for rapid game development without the need for low-level programming.

mediapipe and OpenCV
mediapipe and OpenCV were chosen for hand gesture recognition and camera input processing, respectively. These libraries provide robust and efficient solutions for computer vision tasks, making it possible to implement hand gesture controls and camera-based gameplay mechanics.

Conclusion
Monkey Moves is a fun and engaging game that combines hand gesture controls with dynamic gameplay mechanics. By leveraging the power of Python and popular libraries like Pygame, mediapipe, and OpenCV, it provides a unique gaming experience that is both challenging and enjoyable.