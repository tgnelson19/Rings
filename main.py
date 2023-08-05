from classes.entity import entity
from classes.globalVar import globalVar

ourVars = globalVar()

while not ourVars.done:

    ourVars.updateKeys()
    ourVars.updateChar()
    ourVars.updateScreen()

ourVars.exit()