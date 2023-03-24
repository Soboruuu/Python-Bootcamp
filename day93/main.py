import pyautogui
from PIL import ImageOps, ImageGrab
import time
from numpy import array

# X and Y coordinates differs with the environment.
# Macbook air 13(2560 x 1600) | left half Chorme browser, right half Interpreter(Pycharm)

dino = (78, 432)
obstacles = (89, 451)
# Set hypothetical box infront of the Dino so that it can detect if there is an obstacle.
lookbox=(130,422,182,456)

def jump():
  pyautogui.press('up')
  
def detect():
  # Capture image of lookbox with Pillow's ImageGrab.grab
  image = ImageGrab.grab(lookbox)
  # Change captured image's color values from RGB to Grayscale with Pillow's Image Ops
  grayimage = ImageOps.grayscale(image)
  # Calculate sum of the image's color values with NumPy array
  cactus = array(grayimage.getcolors()).sum()
  print(cactus)
  return cactus

while True:
  # Even if there is no obstacles in the look box, cactus may differs if the background is black or white
  if 2023 != detect():
    jump()
    
# When editing the code, comment out the above 2 lines in while statement and use below 2 lines to detect x,y coordinates
# Below 2 lines detect x and y coordinates of the mouse cursor
#     print(pyautogui.position())
#     time.sleep(.5)
