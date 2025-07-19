# SOKOBAN (CLI) by Filippo Casola
### Video Demo: [![sokoban video](https://img.youtube.com/vi/2nOiFd54rn4/0.jpg)](https://www.youtube.com/watch?v=2nOiFd54rn4 "sokoban video")
## Description of the project
A command-line version of the classic Sokoban puzzle game where the player pushes boxes onto target locations to win.

Built in Python, this version is lightweight, uses simple text files for levels, and runs directly inside a terminal window.

### How to play
To play the game, the player (that’s you!) needs to push the boxes onto the target spots to complete the level.

 To move the player, you can use W A S D and R to restart the game. To quit the game, press the Q key.

<details>
<summary>Keys and Legend</summary>
    Movement key:             Legend:

    W - Move Up               # - Wall block

    A - Move Left             @ - Player

    S - Move Down             $ - Box

    D - Move Right            . - Target

    R - Restart the game.     * - Box on target

    Q - Quit the game.

</details>


## Design philosophy
### UI
The game displays four columns:
- Game board
- Legend
- Controls
- Moves counter

Every time the player moves, the terminal updates the board and the move counter accordingly.

Having all the information and board visible at the same time makes the game easy to play and understand.

### Gameplay
The game is played real time, with the CLI enviroment refreshing immediately after each move, making the gameplay seamless and responsive.

#### Game rules:
- The player can only push boxes (not pull them)
- The player cannot move into walls or targets
- Boxes can only be pushed into empty spaces or targets
- Once a box is on the target, it cannot be removed
- The player can restart or quit the game at any time during gameplay.


The game starts by explaining the objectives, then asks the player to select a difficulty level.  After the selection, the respective level is loaded.


### Code
The code is structured in a modular way, where each action that the player can perform is separated into its own function.

The level that the player interacts with is a copy of the original level file.
This ensures that if the game is quit early or crashes, the original level files remain unaffected and do not need to be reset manually

## Requirements:
To run this script you need to have python 3 and have these packages installed:
- readchar
- (sys) usually comes with Python but for listed for completeness
- (os) usually comes with Python but for listed for completeness
### To launch the game, run the following command

```python
.../python sokoban.py
```

## Project structure
```
├── Sokoban.py
├── level1.txt
├── level2.txt
├── README.md
├── test_sokoban.py
└── requirements.txt
```
## Files explanation

| File             | Use                          |
| -------------    |:-------------                |
| Sokoban.py       | main game code               |
| level1.txt       | Easy level layout            |
| level2.txt       | Hard Level layout            |
| README.md        | This file                    |
| test_sokoban.py  | Test cases file              |
| requirements.txt | List of required packages    |

## Next steps
The game is designed flexibly as it is not hardcoded to use only the two provided levels.
If you modify the level files (for example, change their width or add more objectives and boxes), the game will still work.

### Planned improvements
My next step would be to implement a "select your own level" system, where users can place a .txt file in the project folder, and the program will detect and load it as the active level.
To achieve this, the goal is to build a robust validation system that will:
- Ensure each target has at least a box
- Check that boxes are placeable (not stuck aganist a wall)
- Validate the overall structure of the level


