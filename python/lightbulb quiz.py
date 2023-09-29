import random
class lightbulb:
    def __init__(self, color: str = "White",kind: str = "LED"):
        self.on = False
        self.color = color
        self.burnt = False
        self.type = kind
        print("A", kind, "lightbulb has started existing!")
    def gimme(self):
        print("I am", end = " ")
        if not self.on:
            print("not", end = " ")
        print("on,\nmy color is", self.color, "\nand", end = " ")
        if self.burnt:
            print("I have burnt out")
        else:
            print("everything is fine!")
    def burnout(self):
        if self.on and random.randint(1,20) == 1:
            print("AA-")
            self.burnt = True
    def switch(self):
        if self.on:
            self.on = False
            print("I have been turned off")
        else:
            self.on = True
            print("I have been turned on")

joe = lightbulb()
wheatley = lightbulb("Blue", "Halogen")
cinnamon = lightbulb("Orange", "LED Corn")
clocktown = lightbulb("Yellow", "Xenon")
keygen = lightbulb("Lime")
wondermaker = lightbulb("Light Blueberry", "Filament")
spider = lightbulb("Black", "Mercury Vapor")
fire = lightbulb("Bright", "Fire")
nyancat = lightbulb("Pink", "UV")
walle = lightbulb("Green", "Energy Saving")
stickman = lightbulb("Red", "Fluorescent")
steve = lightbulb("Invisible", "Infared")

joe.gimme()
wheatley.gimme()
cinnamon.gimme()
clocktown.gimme()
keygen.gimme()
wondermaker.gimme()
spider.gimme()
fire.gimme()
nyancat.gimme()
walle.gimme()
stickman.gimme()
steve.gimme()
for i in range(2):
    joe.switch()
    wheatley.switch()
    cinnamon.switch()
    clocktown.switch()
    keygen.switch()
    wondermaker.switch()
    spider.switch()
    fire.switch()
    nyancat.switch()
    walle.switch()
    stickman.switch()
    steve.switch()
    wheatley.burnout()
    cinnamon.burnout()
    clocktown.burnout()
    keygen.burnout()
    wondermaker.burnout()
    spider.burnout()
    fire.burnout()
    nyancat.burnout()
    walle.burnout()
    stickman.burnout()
    steve.burnout()
    joe.gimme()
    wheatley.gimme()
    cinnamon.gimme()
    clocktown.gimme()
    keygen.gimme()
    wondermaker.gimme()
    spider.gimme()
    fire.gimme()
    nyancat.gimme()
    walle.gimme()
    stickman.gimme()
    steve.gimme()
if (joe.burnt or wheatley.burnt  or cinnamon.burnt or clocktown.burnt or keygen.burnt or wondermaker.burnt or spider.burnt or fire.burnt or nyancat.burnt or walle.burnt or stickman.burnt or steve.burnt):
    print("It seems something has gone arry...\nJoe tries to communicate in binary to the others to see what could be wrong,\nUnfortunately, the others don't understand binary")
else:
    print("Everything seems in order so far...")