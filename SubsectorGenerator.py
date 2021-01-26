import random as r
from PIL import Image, ImageDraw, ImageColor

im = Image.open("subsectortemplate.png")

#width, height = im.size
#print(str(width)+', '+str(height))

draw = ImageDraw.Draw(im)

rad = 50
density  = 40 #percentage decity as an integer

for i in range(0,8):
    if i % 2 == 0:
        for j in range(0,11):
            if r.randint(0,100) < density:
                draw.ellipse([245-rad+(225*i), 225-rad+(j*260), 245+rad+(225*i), 225+rad+(j*260)], 'black')
    elif i % 2 == 1:
        for j in range(0,10):
            if r.randint(0,100) < density:
                draw.ellipse([245-rad+(225*i), 354-rad+(j*260), 245+rad+(225*i), 354+rad+(j*260)], 'black')

# collum 1 start x,y: 245,97
# 0101 midpoint x,y: 245, 225
# 0111 midpoint x,y: 245, 2795

# collum 2 start x,y: 470,225
# 0201 midpoint x,y: 470, 354
# 0210 midpoint x,y: 470, 2538

#hex width = 294 half = 147
#hex height = 260 half = TODO
#distance between collum x mids: 225

im.show()

print("Save? (y/n): ")
doSave = input()
if doSave == 'y':
    print("Name: ")
    name=input()
    im.save("maps/"+name+".png", "PNG")