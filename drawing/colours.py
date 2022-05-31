colourNames = ["Red", "Cyan", "Blue", "DarkBlue", "LightBlue",
               "Purple", "Yellow", "Lime", "Magenta", "Silver",
               "Gray", "Black", "Orange", "Brown", "Maroon",
               "Green", "Olive"]
colourIndex = 0


def getNextColour():
    global colourIndex
    toReturn = colourNames[colourIndex]
    colourIndex = 0 if colourIndex == len(colourNames) - 1 else colourIndex + 1
    return toReturn