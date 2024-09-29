# AquaBit

Aquabit is a pixel-like aquarium simulation game

## Description

you can add fishes of different colors, food pellets for each of them, seaweed-like plants that grow upwards, and even some predators that hunt the fish.

## Technologies Used

This game was made in Visual Studio Code using Python. It uses Pygame, Random, and OS Libraries.

## Installation & Running
1. **Download the Source:** Go to the "Releases" section and download the source zip folder from the latest update.

2. **Unzip Folder:** Extract the zip folder to your preffered location.

3. **Install Dependencies:** Make sure to have Python and pip installed. Then install Pygame by running:     
 ```bash
 pip install pygame
 ```
4. **Run the Game:** Either open the .py file by double clicking on it or run this in the terminal:
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
   - Predators move randomly, and move towards Fish (hunger limit of 5 Fishes per Predator) (Predator dies at 5th Fish eaten)

## Snipets

<img width="734" alt="aquabit_snipet" src="https://github.com/user-attachments/assets/dfc0735e-e4b1-45b8-944e-c9229bdd5e39">
<br></br>
<img width="734" alt="aquabit_screenshot" src="https://github.com/user-attachments/assets/7f9b51dd-33cd-429b-9bf6-64d22641a2b2">



## Version
Latest: v1.1.0
   - See [Release History](https://github.com/NeilM5/AquaBit/releases) 
    
## License
This game is licensed under the GPL-3.0 License - see the LICENSE.md file for details

## Acknowledgements

### Inspired by:
   - John Conway's Game of Life
