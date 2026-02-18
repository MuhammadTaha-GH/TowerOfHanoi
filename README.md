# Tower of Hanoi Visualizer

A graphical simulation of the classic **Tower of Hanoi** puzzle built using Python and Pygame. This application visually demonstrates the steps required to solve the puzzle and allows users to interactively select the number of disks.

---

## Project Overview

The **Tower of Hanoi Visualizer** solves the Tower of Hanoi puzzle for a user-defined number of disks (1-7) and animates each disk move in real time. Users can see how the recursive algorithm works and gain a better understanding of this classic problem.

Key highlights:

- Interactive input for number of disks
- Animated disk movements
- Color-coded disks for easy differentiation
- Educational tool for understanding recursion and problem-solving

---

## Features

- Input the number of disks (1-7) interactively
- Animated moves showing the recursive Tower of Hanoi solution
- Color-coded disks for easy differentiation
- Smooth visualization using Pygame graphics

---

## Tech Stack

| Component       | Technology            |
|-----------------|---------------------|
| Programming Language | Python 3.x       |
| Graphics Library     | Pygame           |
| Timing & Animation   | time module      |

---

## Getting Started

Install Pygame if not already installed:

```bash
pip install pygame
```

Run the Python script:

```bash
python tower_of_hanoi.py
```

1. Enter the number of disks (1-7) when prompted.
2. Watch the animation as disks move from the source peg to the destination peg according to the Tower of Hanoi algorithm.

---

## How It Works

The program uses a recursive algorithm to solve the Tower of Hanoi puzzle:

1. Move n-1 disks from source peg to auxiliary peg.
2. Move the nth disk from source peg to destination peg.
3. Move n-1 disks from auxiliary peg to destination peg.

Each move is animated in the Pygame window.

---

## Folder Structure

```
/
├── tower_of_hanoi.py  # Main Python script
├── README.md          # Project documentation
```

---

## Roadmap / Future Improvements

- Add adjustable animation speed
- Allow custom colors for disks
- Include a step-by-step mode for manual control
- Add sound effects for moves
- Expand to support more than 7 disks with scalable visualization

---

## Contributing

Contributions are welcome! To contribute:

1. Fork this repository  
2. Create a feature branch  
3. Commit your changes  
4. Push to the branch  
5. Open a Pull Request

---

## License

This project is open source — feel free to adapt and extend.  
*(Add your chosen license here, e.g., MIT)*

---

## Contact

Developed by **Muhammad Taha**  
GitHub: https://github.com/MuhammadTaha-GH  

If this project helped you, please give it a **star!**
