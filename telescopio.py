from turtle import*
color("yellow")
pencolor("black")
def hexagonales():
    for i in range(6):
        right(60)
        forward(40)
def hexan_01():
    begin_fill()
    hexagonales()
    left(180)
    forward(40)
    left(120)
    end_fill()
for y in range(6):
    hexan_01()
def hexan_02():
    for z in range(12):
        begin_fill()
        hexagonales()
        left(180)
        forward(40)
        left(120)
        end_fill()
        if z in [1,3,5,7,9,11]:
            right(60)
            forward(40)
            left(120)
right(60)
forward(40)
right(60)
forward(40)
left(120)
color("yellow")
pencolor("black")
hexan_02()
pencolor("yellow")
goto(-40,0)
done()
