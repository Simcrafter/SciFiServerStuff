import random as r

#generate star
#generate orbits
#put objects in orbit
#detail said objects physical charecteristics (size atmosphere etc)
#pick one to be most important (basically if there a not shit planet use that LLLLLLLLLLLLLLLLLLLL)
#generate thats other stats first :)
#generate rest other stats
#base pop of other objects off main :) (or something idk lol)

#CLASSES
class Star: #class containing data on a star
    spectralType = 5# B = 0 A = 1 F = 2 G = 3 K = 4 M = 5
    size = 5 #spectype subsizes
    brightness = 5 #is it main sequence or cool

    def __init__(self, specT, siz, bright):
        self.spectralType=specT
        self.size = siz
        self.brightness = bright

class Body:
    orbitID = 99
    isGasGiant = False
    isAsteroidBelt = False

    size = 0

    def __init__(self, orb, isGG, isAB):
        self.orbitID = orb
        self.isGasGiant = isGG
        self.isAsteroidBelt = isAB

#FUNCTIONS
def makeStar(): #discount star constructor
    specT = spectralTypeGen()
    size = r.randint(0,9)
    brightness = starBright(specT)

    return Star(specT, size, brightness)

def spectralTypeGen(): #rng spectraltype
    spectralTypeRoll = r.randint(0,1000)
    spectralType = 5

    if spectralTypeRoll < 1: #B type
        spectralType=0
    elif spectralTypeRoll < 7: #A type
        spectralType=1
    elif spectralTypeRoll < 37: #F type
        spectralType=2
    elif spectralTypeRoll < 113: #G type
        spectralType=3
    elif spectralTypeRoll < 234: #K type
        spectralType=4
    else: #M type
        spectralType=5

    return spectralType

def starBright(specT): #this is doesnt need to be a function
    if specT < 2:
        return 3
    else:
        return 5

### GENRATING STARS
binaryRoll = r.randint(0,100) #rng for binary
binaryChance = 33 #chance of binary system
stars = [] #list o stars
binary = False
binaryClass = "P"

#make stars in list
stars.append(makeStar())
if binaryRoll<binaryChance:
    stars.append(makeStar())
    binary=True

    if stars[1].spectralType<stars[0].spectralType: #sort by size if binary
        stars[1], stars[0] = stars[1], stars[0]
    elif stars[1].size <stars[0].size:
        stars[1], stars[0] = stars[1], stars[0]
    
    if stars[0].spectralType < stars[1].spectralType+1 or (stars[0].spectralType!=5 and stars[1].spectralType==5):
        binaryClass="S" #update binary class with size diff between stars

for i in range(len(stars)):
    specTstring="M"
    if stars[i].spectralType == 0:
        specTstring = "B"
    elif stars[i].spectralType == 1:
        specTstring = "A"
    elif stars[i].spectralType == 2:
        specTstring = "F"
    elif stars[i].spectralType == 3:
        specTstring = "G"
    elif stars[i].spectralType == 4:
        specTstring = "K"
    else:
        specTstring = "M"
    print("Star "+str(i+1)+": "+specTstring+str(stars[i].size)+str(stars[i].brightness))

if binary: 
    print("Binary Class: "+binaryClass)

#GENERATE OBJECTS
orbitHeats = []
for i in range(13):
    orbitHeats.append(0)

#heat class
#0=cold 1=hab 2=hot 3=no
mStar = stars[0]

#hardcoding orbit tempature bands... agony
if mStar.spectralType == 5 and stars[0].size == 0: #M0
    orbitHeats[0] = 1
elif mStar.spectralType == 4 and mStar.size > 4: #K5
    orbitHeats[0] = 1
elif mStar.spectralType == 4 and mStar.size < 5: #K0
    for i in range(1):
        orbitHeats[i] = 2
    orbitHeats[2] = 1
elif mStar.spectralType == 3 and mStar.size > 4: #G5
    for i in range(1):
        orbitHeats[i] = 2
    orbitHeats[2] = 1
elif mStar.spectralType == 3 and mStar.size < 5: #G0
    for i in range(2):
        orbitHeats[i] = 2
    orbitHeats[3] = 1
elif mStar.spectralType == 2 and mStar.size > 4: #F5
    for i in range(3):
        orbitHeats[i] = 2
    orbitHeats[4] = 1
elif mStar.spectralType == 2 and mStar.size < 5: #F0
    for i in range(4):
        orbitHeats[i] = 2
    orbitHeats[5] = 1
elif mStar.spectralType == 1 and mStar.size > 4: #A5
    for i in range(5):
        orbitHeats[i] = 2
    orbitHeats[6] = 1
elif mStar.spectralType == 1 and mStar.size < 5: #A0
    for i in range(6):
        orbitHeats[i] = 2
    orbitHeats[7] = 1
elif mStar.spectralType == 0 and mStar.size > 4: #B5
    for i in range(2):
        orbitHeats[i] = 3
    for i in range(3,8):
        orbitHeats[i] = 2
    orbitHeats[9] = 1
elif mStar.spectralType == 0 and mStar.size < 5: #B0
    for i in range(5):
        orbitHeats[i] = 3
    for i in range(6,11):
        orbitHeats[i] = 2
    orbitHeats[12] = 1

bodies = []
#Chances
chanceBody = 50 #chance of a thing
chanceGG = 60 #chance of it being a gas giant
chanceAB = 10 #chance of it being a belt

for i in range(len(orbitHeats)):
    rollBody = r.randint(0,100)
    if rollBody < chanceBody and orbitHeats[i] != 3: #if rng good and orbit availiabe
        if orbitHeats[i] == 0 and i>2: #if cold and away
            rollGG = r.randint(0,100)
            if rollGG < chanceGG: #see if gas giant
                bodies.append(Body(i, True, False))
                continue

        rollAB = r.randint(0,100)
        if rollAB < chanceAB: #check to see if asteroid belt
            bodies.append(Body(i, False, True))
            continue

        bodies.append(Body(i, False, False)) #if not make rocky planet

#Sizes
for b in bodies: #TODO AAAAAAAAAAAAAAHHHHHHHH HOW DO THIS
    if b.isAsteroidBelt:
        b.size = 0
    elif b.isGasGiant:
        b.size = 99
    else: #0.1 EarthRadii to 2 Er, Median 0.9, majority within 0.4 to 1.4
        sizeRoll=r.randint(0,6) + r.randint(1,6) + r.randint(1,3)
        #size in 100s km
        siz = 64.0 * (float(sizeRoll) / 10.0)
        siz *= 100.0
        b.size = int(siz) #radius in km
    print(b.size)


        


