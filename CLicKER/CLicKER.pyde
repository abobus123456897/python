absciss = 1
ordinat = 1
ochci = 99
b = 1
c = 1
uroven= 1
# e = 0
def setup():
    size(600,400)
    background(24,174,274)
def draw():
    global ochci , uroven
    background(24,174,274)
    push()
    fill(0,255,50)
    ellipse(100,300,1500,200)
    fill(255)
    rect(0,350,200,50)
    rect(200,350,200,50)
    rect(400,350,200,50)
    strokeWeight(5)
    fill(255)
    pop()
    textSize(30)
    fill(0)
    text(ochci,300,300)
    text("CLICK",50,395)
    text("LEVEL UP",220,395)
    text("EXIT",400,395)
    text(uroven,0,25)
    
def mouseClicked():
    global ochci , b , c, e , uroven
    if mouseX <200 and mouseX > 0 and mouseY < 400 and mouseY > 350 :
        ochci= ochci + c
    if mouseX <600 and mouseX > 400 and mouseY < 400 and mouseY >350:
        exit()
    if mouseX <400 and mouseX > 200 and mouseY < 400 and mouseY > 350:
        if ochci >= 100 and ochci < 250:
            ochci= ochci - 100 
            c = c + 1
            uroven = uroven + 1
        elif ochci >= 250 and ochci <600:
            ochci =ochci  - 250
            c = c + 2
            uroven = uroven + 1
        elif ochci >= 600 and ochci<1000:
            ochci =ochci  - 600
            c = c + 3
            uroven = uroven + 1
        elif ochci >= 1000 and ochci<2000:
            ochci=ochci  - 1000
            c = c + 4
            uroven = uroven + 1
        elif ochci >= 2000 and ochci<3600:
            ochci= ochci - 2000
            c = c + 5
            uroven = uroven + 1
        elif ochci >= 3600 and ochci<4200:
            ochci  = ochci - 3600
            c = c + 6
            uroven = uroven + 1
        elif ochci >= 4200 and ochci<5656:
            ochci = ochci- 4200
            c = c + 7
            uroven = uroven + 1
        elif ochci >= 5656 and ochci<9999:
            ochci= ochci- 5656
            c = c + 8
            uroven = uroven + 1
        elif ochci >= 9999:
            uroven = uroven + 1
            text("YOU ARE WINNER",300,200)
            exit()
       
                    
                
