# Lamda frequency  and Plot Calculator
# Wavelength and Frequency Plotter

**Author:** MD Harrington  
**Location:** London, Kent, DA6 8NP  
**Purpose:** Written for Course 172 Amateur Radio

This Python script calculates and plots the relationship between wavelength and frequency across three radio bands: HF, VHF, and UHF. It provides a graphical representation using the formula:

\[
\lambda = \frac{v}{f}
\]

Where:
- \( \lambda \) is the wavelength (in meters),
- \( v \) is the speed of light (\( 3 \times 10^8 \) meters per second),
- \( f \) is the frequency (in Hz).

The program allows users to choose between three frequency ranges (HF, VHF, UHF) and plots a wavelength vs frequency graph for each choice.

## Linux Configuration
> If you are using Linux, make sure to adjust your ImageMagick configuration file to avoid the program hanging. 

Follow these steps:
1. Open the configuration file using the command:
    ```bash
    sudo nano /etc/ImageMagick-6/policy.xml
    ```
2. Find the line towards the end of the file:
    ```xml
    <policy domain="coder" rights="none" pattern="PS" />
    ```
3. Change it to:
    ```xml
    <policy domain="coder" rights="read|write" pattern="PS" />
    ```

Without this change, the program will not run properly due to ImageMagick policy restrictions.

---

## Dependencies

The program uses the following Python libraries:
- `matplotlib`: For plotting graphs.
- `numpy`: For handling arrays and calculations.
- `colorama`: For colored terminal output.
- `mplcursors`: For adding hover functionality to the graphs.
- `os`, `platform`: For system-level operations like clearing the screen.
- `sys`, `time`: For creating a typewriter effect in the terminal.

Make sure to install these dependencies using pip:
```bash
pip install matplotlib numpy colorama mplcursors


## Code Breakdown

### Imports and Constants

```python
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
from colorama import Fore, Style, init
import mplcursors  # Importing mplcursors for interactive tooltips
import os 
import platform 

# Initialize colorama
init()

# Constants
C = 3 * 10**8  # Speed of light in meters per second

### Explanation of Imports

- **matplotlib**: Used for plotting graphs. It provides functions to create static, animated, and interactive visualizations in Python.
- **numpy**: A library for efficient array handling and numerical computation. It is used here for generating frequency values and handling array-based calculations.
- **colorama**: This module provides functionality for coloring text in the terminal. It allows easy use of different colors when printing text to the console.
- **mplcursors**: This library allows interactive tooltips on the graph. It lets the user hover over points on the plot to see the corresponding frequency and wavelength values.
- **os and platform**: These modules are used to detect the operating system and clear the terminal screen accordingly (`cls` for Windows, `clear` for Linux/macOS).
- **C**: A constant representing the speed of light, defined as \( 3 \times 10^8 \) meters per second. It is used to calculate the wavelength (`λ`) from the frequency (`f`).

### `clear_screen()` Function

```python
def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

### Purpose

This function clears the terminal screen. It detects the operating system and executes the appropriate command:

- On **Windows**, it runs `cls` to clear the console.
- On **Linux/macOS**, it runs `clear` to perform the same task.

### `plot_graph()` Function

```python
def plot_graph(frequencies, wavelengths, title):
    frequencies_mhz = frequencies / 1e6  # Convert frequencies from Hz to MHz
    
    # Set the figure size to 800x600 pixels (8x6 inches at 100 DPI)
    fig, ax = plt.subplots(figsize=(8, 6))
    
    scatter = ax.scatter(frequencies_mhz, wavelengths, s=1)  # Smallest visible points
    plt.title(title)
    plt.xlabel('Frequency (MHz)')
    plt.ylabel('Wavelength (m)')
    
    # Add header
    plt.figtext(0.5, 0.01, 'Created by MD Harrington London UK DA6 8NP', ha='center')
    plt.grid(True)
    
    # Adding hover functionality using mplcursors, formatted for MHz and meters
    cursor = mplcursors.cursor(scatter, hover=True)
    cursor.connect("add", lambda sel: sel.annotation.set_text(
        f'f={frequencies_mhz[sel.index]:.2f} MHz\nλ={wavelengths[sel.index]:.2f} m'))
    
    plt.show()

### Purpose

This function generates a scatter plot of frequencies vs. wavelengths. Key details include:

- **Frequencies in MHz**: The frequencies are converted from Hz to MHz for better readability on the graph.
- **Figure size**: The graph is displayed in an 800x600 pixel window (8x6 inches at 100 DPI).
- **Scatter plot**: Points are plotted with the smallest visible size (`s=1`), showing the relationship between frequency and wavelength.
- **Title and Labels**: A title and labels for the X and Y axes are provided to describe the graph.
- **Header**: A footer is added at the bottom of the figure with custom text.
- **Grid**: A grid is shown to improve readability.
- **Interactive Tooltips**: Using `mplcursors`, the function enables hover functionality. When hovering over a point, it displays the corresponding frequency (in MHz) and wavelength (in meters).

### `typewriter_text()` Function

```python
def typewriter_text(text, color):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.05)  # Pause to create typewriter effect
    print()

```python
def typewriter_text(text, color):

### Function Definition

This line defines a function named `typewriter_text` that takes two parameters:

- `text`: The string of text to be displayed.
- `color`: The color code (typically a string) to format the text output.

### Function Definition

```python
def main():
    while True:
        clear_screen()  # Clear the screen before displaying the menu
        
        print("\n" + "-"*40)
        display_menu()
        print("\n" + "-"*40)
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            frequencies = np.linspace(3e6, 30e6, 100)  # HF: 3 MHz to 30 MHz
        elif choice == '2':
            frequencies = np.linspace(30e6, 300e6, 100)  # VHF: 30 MHz to 300 MHz
        elif choice == '3':
            frequencies = np.linspace(300e6, 3000e6, 100)  # UHF: 300 MHz to 3000 MHz
        elif choice == '4':
            print("Exiting program...")
            break
        else:
            print("Invalid choice, please try again.")
            continue
        
        # Calculate wavelengths
        wavelengths = calculate_wavelength(frequencies)
        
        # Plot the graph with hover functionality
        plot_graph(frequencies, wavelengths, "Wavelength vs Frequency")
### Code Explanation

```python
def main():

    Function Definition: This line defines the main function that contains the primary logic for the program.



    while True:

    Infinite Loop: This creates an infinite loop, allowing the program to continuously display the menu until the user decides to exit.



        clear_screen()  # Clear the screen before displaying the menu

    Clear Screen: This function call clears the console screen, providing a clean display for the menu each time it is shown.



        print("\n" + "-"*40)

    Print Separator: This line prints a newline followed by a line of 40 dashes, creating a visual separator before displaying the menu.



        display_menu()

    Display Menu: This function call displays the menu options for the user to choose from.



        print("\n" + "-"*40)

    Print Separator: Another visual separator is printed after the menu to enhance readability.


        choice = input("Enter your choice: ")

    User Input: This line prompts the user to enter their choice from the menu and stores it in the variable choice.


        if choice == '1':
            frequencies = np.linspace(3e6, 30e6, 100)  # HF: 3 MHz to 30 MHz

    HF Option: If the user selects option '1', this line generates an array of 100 evenly spaced frequencies between 3 MHz and 30 MHz using NumPy's linspace function.



        elif choice == '2':
            frequencies = np.linspace(30e6, 300e6, 100)  # VHF: 30 MHz to 300 MHz

    VHF Option: If the user selects option '2', this generates frequencies between 30 MHz and 300 MHz.



        elif choice == '3':
            frequencies = np.linspace(300e6, 3000e6, 100)  # UHF: 300 MHz to 3000 MHz

    UHF Option: If the user selects option '3', this generates frequencies between 300 MHz and 3000 MHz.



        elif choice == '4':
            print("Exiting program...")
            break

    Exit Option: If the user selects option '4', a message is printed, and the loop is exited, terminating the program.



        else:
            print("Invalid choice, please try again.")
            continue

    Invalid Input Handling: If the input does not match any valid option, an error message is displayed, and the loop continues, prompting the user for input again.



        # Calculate wavelengths
        wavelengths = calculate_wavelength(frequencies)

    Calculate Wavelengths: After a valid choice is made, this line calls the calculate_wavelength function, passing the selected frequencies to calculate their corresponding wavelengths.



        # Plot the graph with hover functionality
        plot_graph(frequencies, wavelengths, "Wavelength vs Frequency")

    Plot Graph: This line calls the plot_graph function to visualize the relationship between the frequencies and their wavelengths, with a title of "Wavelength vs Frequency."
