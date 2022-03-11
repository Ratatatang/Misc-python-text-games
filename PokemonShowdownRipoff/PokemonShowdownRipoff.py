from GlobalClasses import *
from Lists import *
from cmu_graphics import *   
    
class teamPokemon():
    
    pokemonType = ''
    move1 = ''
    move2 = ''
    move3 = ''
    move4 = ''
    heldItem = ''
    ability = ''
    
    def __init__(self):
    
    
    
startButton = Group(
    Rect(120, 150, 175, 80, fill = 'lime'),
    Label('START', 207, 190, size = 50, bold = True)
)

## app variables
app.Player1Active = 0
app.Player2Active = 0
app.Player1Pokemon = []
app.Player2Pokemon = []
app.ycenterX = 62
app.ycenterY = 178
app.tcenterX = 297
app.tcenterY = 98


## Functions that start on run
def onMousePress(mouseX, mouseY):
    if(startButton.hits(mouseX, mouseY)):
        startButton.clear()



cmu_graphics.run()
