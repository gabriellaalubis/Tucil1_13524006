# Queens Game Solver

Qeens Game Solver is a graphical puzzle solver built with Python using the Tkinter library. The program solves a modified Queens problem with constraints: exactly one queen per row, column, and color region, with no two queens in adjacent rows are placed in adjacent columns.

The board is loaded from a .txt file where each cell contains a letter representing its color region.

When a solution is found, the program will:
- Displays the board visually
- Shows execution time and number of cases tried
- Allows saving the solution as .txt or .png file

If no solution exists, a notification message is shown.

## Requirements and Installation

### Requirements:
- **Python 3.x** 
- **Operating System**: Windows or Linux with display support

### Required Python Packages:
- `tkinter` (usually comes with Python installation)
- `Pillow` 
- `random` (built-in standard library)

### Installation:

1. Ensure Python 3.x is installed on your system

   Check installation:

   **Windows:**
   ```bash
   python --version
   ```

   **Linux/macOS:**
   ```bash
   python3 --version
   ```

2. Install required packages:

   ```bash
   pip install Pillow
   ```

   or

   ```bash
   pip3 install Pillow
   ```
3. Clone or download this repository:
   ```bash
   git clone https://github.com/gabriellaalubis/Tucil1_13524006.git
   cd Tucil1_13524006
   ```

For Linux Users, if `tkinter` is not installed by default, install it using:

```bash
sudo apt install python3-tk
```
or
```bash
sudo dnf install python3-tkinter
```

## Compilation

This project does not require compilation. Python files are interpreted at runtime.

## How to Run 

1. Navigate to the project directory:
   ```bash
   cd Tucil1_13524006
   ```

2. Run the main program:
   ```bash
   python src/core.py
   ```

## How To Use

1. The application window will open showing the "QUEENS GAME SOLVER" interface
2. Click the file selection button to choose a game board file (.txt format). The board file should contain:
   - A square grid of alphabetic characters representing regions
   - Each line represents a row
   - Characters are space-separated or continuous
   - Must have exactly n distinct characters for an n×n board
   Example:
     ```
     A A C C
     A A C D
     B B C D
     B C C D
     ```
     or
     ```
     AACC
     AACD
     BBCD
     BCCD
     ```

4. Click 'Solve', the program will:
   - Validate the board format 
   - Find the solution to the Queens problem
   - Display the live process visually 
   - Show the queens' positions on the board


## Author

Gabriella Botimada Lubis

13524006

---