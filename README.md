# ruko

A simple computer-vision tool to interactively recognize colors in an image. Click (or double-click) on any pixel to display its closest named color and RGB values.


## Features

- **Pixel-level Color Detection:** Uses Euclidean distance in RGB space against a CSV of standard colors.  
- **Interactive CLI Session:**  
  1. Run `python color_detection.py -i <image_path>`  
  2. Double-click anywhere on the image window to see the color name and RGB.  
  3. Press `Ctrl + C` in the console to exit.  
- **Modular CSV Backend:** Easily swap in your own color database.  
- **Planned Upgrades:** ML-based classifiers for faster and more accurate color naming.


## Installation

```bash
git clone https://github.com/sharmabhay/ruko.git
cd ruko
pip install -r requirements.txt
```
