import random as r

#functions
def d6():
    return r.randint(1,6)

#generator

#TODO Names
#this is hard lol no wonder i skipped it

#size
Size = (d6() + d6()) - 2
print("Size: " + str(Size))

#atmosphere
Atmosphere = (d6() + d6()) - 7 + Size
Atmosphere = max(0, min(Atmosphere, 15))
print("Atmosphere " + str(Atmosphere))

#hydrographics
if Size < 2:
    Hydrographic = 0
elif Atmosphere < 2 or (Atmosphere <= 12 and Atmosphere >= 10):
    Hydrographic = (d6() + d6()) - 7 + Atmosphere - 4
else:
    Hydrographic = (d6() + d6()) - 7 + Atmosphere
Hydrographic = max(0, min(Hydrographic, 10))
print("Hydrographics: " + str(Hydrographic))

#tempurature
tempNum = d6() + d6()
Tempurature = 6
if(Atmosphere<2):
    tempNum = 6
elif(Atmosphere<4):
    tempNum -= 2
elif(Atmosphere<6 or Atmosphere==14):
    tempNum -=1
elif(Atmosphere<8):
    tempNum = tempNum
elif(Atmosphere<10):
    tempNum += 1
elif(Atmosphere==10 or Atmosphere == 13 or Atmosphere == 15):
    tempNum += 2
elif(Atmosphere == 11 or Atmosphere == 12):
    tempNum += 3

zoneEdge = d6() + d6()
if (zoneEdge==1):
    tempNum -= 4
elif (zoneEdge==12):
    tempNum += 4

if tempNum < 3:
    Tempurature = 1
elif tempNum < 5:
    Tempurature = 2
elif tempNum < 10:
    Tempurature = 3
elif tempNum < 12:
    Tempurature = 4
else:
    Tempurature = 5

print("Tempurature: " + str(Tempurature))

#population
Population = (d6() + d6()) - 2
print("Population: 10^" + str(Population))

#government
Government = (d6() + d6()) - 7 + Population
Government = max(0, min(Government, 15))
print("Government: " + str(Government))

#TODO factions

#law
Law = (d6() + d6()) - 7 + Government
Law = max(0, min(Law, 100))
print("Law Level: " + str(Law))

#starport
starnum = d6() + d6()
if Population>9:
    starnum += 2
elif Population>7:
    starnum += 1
elif Population<5:
    starnum -= 1
elif Population<3:
    starnum -=2

#Number to Type
# A = 5
# B = 4
# C = 3
# D = 2
# E = 1
# x = 0
Starport = 0
if starnum>10:
    Starport = 5
elif starnum>8:
    Starport = 4
elif starnum>6:
    Starport = 3
elif starnum>4:
    Starport = 2
elif starnum>2:
    Starport = 1
else:
    Starport = 0
print("Starport: " + str(Starport))

# Bases
navalNum = d6()+d6()
scoutNum = d6()+d6()
researchNum = d6()+d6()
Naval = False
Scout = False
Research = False

if Starport == 5:
    if navalNum>= 8:
        Naval=True
    if scoutNum>=10:
        Scout=True
    if researchNum>=8:
        Research=True
elif Starport==4:
    if navalNum>= 8:
        Naval=True
    if scoutNum>=8:
        Scout=True
    if researchNum>=10:
        Research=True
elif Starport==3:
    if scoutNum>=8:
        Scout=True
    if researchNum>=10:
        Research=True
elif Starport==2:
    if scoutNum>=7:
        Scout=True

if Naval:
    print("Has Naval Base")
if Scout:
    print("Has Scout Base")
if Research:
    print("Has Research Base")

#Tech Level
Tech = d6()

#starport modifiers
if Starport == 5:
    Tech += 6
elif Starport == 4:
    Tech += 4
elif Starport == 3:
    Tech += 2
elif Starport == 0:
    Tech -= 4

#size modifiers
if Size < 2:
    Tech += 2
elif Size < 5:
    Tech += 1

#atmosphere modifiers
if Atmosphere < 4:
    Tech += 1
elif Atmosphere > 9:
    Tech += 1

#hydro modifiers
if Hydrographic==0 or Hydrographic == 9:
    Tech += 1
elif Hydrographic == 10:
    Tech += 2

#population modifiers
if Population>0 and Population<6:
    Tech += 1
elif Population == 8:
    Tech += 1
elif Population == 9:
    Tech += 2
elif Population == 10:
    Tech += 4

#government modifiers
if Government== 0 or Government == 5:
    Tech += 1
elif Government == 7:
    Tech += 2
elif Government == 13 or Government == 14:
    Tech -= 2

# minimum tech levels
if Atmosphere < 2 and Tech<8:
    Tech = 8
elif Atmosphere < 4 and Tech<5:
    Tech = 5
elif (Atmosphere == 4 or Atmosphere == 7 or Atmosphere == 9)and Tech<3:
    Tech = 3
elif Atmosphere == 10 and Tech<8:
    Tech = 8
elif Atmosphere == 11 and Tech<9:
    Tech = 9
elif Atmosphere == 12 and Tech<10:
    Tech = 10
elif Atmosphere == 15 and Tech<5:
    Tech = 5
elif (Atmosphere == 13 or Atmosphere == 14) and Tech < 8:
    Tech = 8

print("Tech Level: " + str(Tech))

#Trade Codes
Agricultural = False
Asteroid = False
Barren = False
Desert = False
FluidOceans = False
Garden = False
HiPop = False
HiTech = False
IceCapped = False
Industrial = False
LoPop = False
LoTech = False
NonAgricultural = False
NonIndustrial = False
Poor = False
Rich = False
Vacuum = False
WaterWorld = False

if 3 < Atmosphere < 10 and 3 < Hydrographic < 9 and 4 < Population < 8:
    Agricultural=True
if Size==0 and Atmosphere==0 and Hydrographic==0:
    Asteroid=True
if Population==0 and Government==0 and Law==0:
    Barren=True
if Size>1 and Hydrographic==0:
    Desert=True
if Atmosphere>9 and Hydrographic>0:
    FluidOceans=True
if 5<Size<9 and 4<Hydrographic<8 and (Atmosphere == 5 or Atmosphere == 6 or Atmosphere == 8):
    Garden=True
if Population>8:
    HiPop=True
if Tech>11:
    HiTech=True
if Atmosphere<2 and Hydrographic > 0:
    IceCapped=True
if Population>8 and (Atmosphere<3 or Atmosphere==4 or Atmosphere==7 or Atmosphere==9):
    Industrial=True
if Population<4:
    LoPop=True
if Tech<6:
    LoTech=True
if Atmosphere<4 and Hydrographic<4 and Population>5:
    NonAgricultural=True
if Population<7:
    NonIndustrial=True
if 1<Atmosphere<6 and Hydrographic<3:
    Poor=True
if (Atmosphere == 6 or Atmosphere ==8) and 5<Population<9 and 3<Government<10:
    Rich=True
if Atmosphere==0:
    Vacuum=True
if Hydrographic>9:
    WaterWorld=True

if Agricultural:
    print("Agricultural")
if Asteroid:
    print("Asteroid")
if Barren:
    print("Barren")
if Desert:
    print("Desert")
if FluidOceans:
    print("Fluid Oceans")
if Garden:
    print("Garden")
if HiPop:
    print("High Population")
if HiTech:
    print("High Tech")
if IceCapped:
    print("Ice-Capped")
if Industrial:
    print("Industrial")
if LoPop:
    print("Low Population")
if LoTech:
    print("Low Tech")
if NonAgricultural:
    print("Non-Agricultural")
if NonIndustrial:
    print("Non-Industrial")
if Poor:
    print("Poor")
if Rich:
    print("Rich")
if Vacuum:
    print("Vacuum")
if WaterWorld:
    print("Water World")


#TODO make number into descriptors
