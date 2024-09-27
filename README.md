# AquaBit

Aquabit is a pixel-like aquarium simulation game

## Description

you can add fishes of different colors, food pellets for each of them, seaweed-like plants that grow upwards, and even some predators that hunt the fish.

## Technologies Used

This game was made in Visual Studio Code using Python. It uses Pygame, Random, and OS Libraries.

## Installation & Running
1. **Clone Repository:** Open your terminal and run the following command to clone the repository.
```bash
git clone https://github.com/NeilM5/AquaBit
```

2. **Navigate to Project Directory:**
```bash
cd C:\Users\username\Documents\AquaBit
```

3. **Install Dependencies:** Make sure to have Python and pip installed. Then install Pygame.       
 ```bash
 pip install pygame
 ```
4. **Run The Game:**
```bash
python AquaBit.py
```

## How to Play
   - **Z** - Add Fish (limit 50)
   - **C** - Add Food Pellets (limit 20)
   - **V** - Add Plants (limit 20)
   - **X** - Add Predators (limit 5)
   - **S** - Take a Screenshot (saves to Downloads)
   - Hold **D** and Press:
     
     - **Z** - Kill All Fish
     - **C** - Remove All Food Pellets
     - **V** - Kill All Plants
     - **X** - Kill All Predators
       
## How It Works
   - Fishes (3 colors) move randomly
   - When Food Pellets are added, Fish move towards Food Pellets (hunger limit of 5 Pellets per Fish)
   - Plants (3 colors) grow upwards in random up, right, and left directions
   - Predators move randomly, and move towards Fish (hunder limit of 5 Fishes per Predator) (Predator dies at 5th Fish eaten)

## Version History
   - v1.0.0
     - Initial Release
    
## License
This game is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgements

### Inspired by:
   - John Conway's Game of Life
