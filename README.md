# RPG Map Optimizer for FoundryVTT

## Overview

This Python program is designed to optimize and prepare maps for use in the Foundry Virtual Tabletop (VTT), specifically catering to Dungeons & Dragons (D&D) RPG sessions. The utility's primary function is to resize images, optimizing them to a standard of 70 pixels per square. This standardization ensures that maps are perfectly scaled for use in FoundryVTT, enhancing the gaming experience by providing clear and consistent visuals.

## Features

- **Image Resizing:** Converts any given image to a resolution of 70 pixels per square, based on the input dimensions (width x height) provided by the user.
- **Image Optimization:** Performs optimization on the images to ensure they are suitable for web use, specifically focusing on the FoundryVTT platform.
- **Format Conversion:** Converts images to the WEBP format, which offers high-quality visuals at smaller file sizes, ideal for web-based tabletop platforms like FoundryVTT.
- **User-Friendly Interface:** Includes a graphical user interface for selecting images and inputting desired dimensions, making it accessible to users with no command line experience.

## Setup and Build Instructions

The project includes a Makefile for easy setup and building. Here's how to use it:

### Prerequisites

Ensure you have Python and pip installed on your system. This program has been tested with Python 3.8 and above. Additionally, you will need `make` installed to utilize the Makefile commands.

### Setup

The setup process installs the necessary Python dependencies, including Pillow for image manipulation and PyInstaller for creating an executable.

To install dependencies, navigate to the project directory in your terminal and run:

```bash
make setup
```

### Build
To build an executable from the Python script, ensuring it can be run on systems without requiring a Python environment, use the build command:

```bash
make build
```

This command uses PyInstaller to generate a standalone executable. After the build process completes, find the executable in the dist directory.


### Usage

After building the project, run the executable. 

A file dialog will open, allowing you to select the image you wish to optimize for FoundryVTT. After selecting an image, you will be prompted to enter the desired dimensions in the format widthxheight (e.g., 25x30).

The program will then process the image, resizing, optimizing, and converting it to WEBP format, saving it with a -ok suffix before the .webp extension in the same directory as the original image.

This utility streamlines the preparation of D&D maps for FoundryVTT, ensuring they are visually consistent and optimized for online play.