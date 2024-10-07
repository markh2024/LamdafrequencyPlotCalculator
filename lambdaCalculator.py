#!/usr/bin/env python3
# MD Harrington  London Kent  DA6 8NP 
# Witten for Course 172 Amatuer  Radio  


## Purpose  to create an easy and quick tool displaying graphs that will 
## Present you with  answers for wavelength and frequency 

## You will need to if using linux make adjustments to  your configuration 
## file in /etc/ImageMagick-6/policy.xml

"""  Note *************************************************************
	 Change line  of config file using command 
	    sudo nano /etc/ImageMagick-6/policy.xml
	    from this line towards the end of the file 
	 <policy domain="coder" rights="none  pattern="PS" />
	   
	   to 
	   
	 <policy domain="coder" rights="read|write" pattern="PS" />
	 
	 
	 Otherwise the program will hang !! 
	 ******************************************************************
""" 





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

def clear_screen():
    # Detect the OS and clear the screen accordingly
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def typewriter_text(text, color):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(0.05)  # Pause to create typewriter effect
    print()

def display_menu():
    typewriter_text("1: Frequencies covering the HF bands (3 MHz to 30 MHz)", Fore.GREEN)
    typewriter_text("2: Frequencies covering the VHF bands (30 MHz to 300 MHz)", Fore.YELLOW)
    typewriter_text("3: Frequencies covering the UHF bands (300 MHz to 3000 MHz)", Fore.BLUE)
    typewriter_text("4: Exit the program", Fore.WHITE)

def calculate_wavelength(frequencies):
    return C / frequencies

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

if __name__ == "__main__":
    main()
