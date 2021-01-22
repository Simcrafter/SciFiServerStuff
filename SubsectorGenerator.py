import random as r
from PIL import Image, ImageDraw, ImageColor

im = Image.open("subsectortemplate.png")

#width, height = im.size
#print(str(width)+', '+str(height))

draw = ImageDraw.Draw(im)

rad = 50
draw.ellipse([245-rad, 225-rad, 245+rad, 225+rad], 'black') #0101
draw.ellipse([245-rad, 225+(10*260)-rad, 245+rad, 225+(10*260)+rad], 'black') #0102
draw.ellipse([470-rad, 354-rad, 470+rad, 354+rad], 'black') #0201
draw.ellipse([470-rad, 354+(1*260)-rad, 470+rad, 354+(1*260)+rad], 'black') #0202

# collum 1 start x,y: 245,97
# 0101 midpoint x,y: 245, 225
# 0111 midpoint x,y: 245, 2795

# collum 2 start x,y: 470,225
# 0201 midpoint x,y: 470, 354
# 0210 midpoint x,y: 470, 2538

#hex width = 294 half = 147
#hex height = 260 half = TODO
#distance between collum x mids: TODO


im.show()



print("Save? (y/n): ")
doSave = input()
if doSave == 'y':
    print("Name: ")
    name=input()
    im.save(name+".png", "PNG")