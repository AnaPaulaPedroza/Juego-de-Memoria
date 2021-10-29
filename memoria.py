from random import *
from turtle import *
from freegames import path

car = path('car.gif')

tiles = '''Kinder
Kit-kat
M&Ms
Toblerone
Twix
Snickers
Milky Way
Hershey's
Crunch
Reese's
Ferrero
CarlosV
Turin 
Whoppers
Kisses
Skittles
Duvalín
Nutella
Bubulubu
Kranky
Bocadín
Pulparindo
Tamborines
Skwinkles
Pelonetes
Lucas Muecas
Golos
Rockaleta
Panditas
Sour Patch
Ring Pop
Nerds
Winis
Checolines
Mamut
Mars
Freskas
Mazapán
Lunetas
Mui-Bon
Larín
Monedas
Trufas
Pelonazo 
Picafresa
Twizzlers
Miguelito
Crazy Dips
Pingüinos
Jelly Belly
Paleta Payaso
3 Muskeeters
Glorias
Rellerindos
Push Pop
Brinquitos
Milk Duds
Jolly Rancher
Butterfinger
Sandi Brochas
Tootsie Roll
Dots
Airheads
Baby Ruth'''

tiles = tiles.split('\n')
state = {'mark': None}
hide = [True] * 64
totalTaps = 0

def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    global totalTaps
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        
    if (hide == [False]*64):
        print("Todos los cuadros fueron destapados")
        done()
    totalTaps = totalTaps + 1
    print("You've tapped: " , totalTaps)

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 26, y+16)
        color('black')
        write(tiles[mark], font=('Arial', 9, 'normal'),align='center')

    update()
    ontimer(draw, 100)

shuffle(tiles)
setup(450, 450, 0, 0)
bgcolor('#F3E5AB')
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()