import pygame as pg
import random as rnd
import os

pg.init()

display = pg.display.set_mode((990, 500))
pg.display.set_caption("AquaBit")

display_color = (162, 217, 206)
fish_colors = [(229, 152, 102), (200, 189, 89), (89, 150, 200)]
predator_color = (200, 89, 89)
plant_colors = [(128, 209, 118), (110, 179, 101), (91, 149, 84)]
food_color = (172, 114, 77)

font = pg.font.SysFont("comic sans ms", 16)

class Fish():
    def __init__(self, grid, dw, dh, color):
        super().__init__()

        self.grid = grid
        self.dw = dw
        self.dh = dh

        self.x = rnd.randint(0, ((dw // grid) - 1) * grid)
        self.y = rnd.randint(0, ((dh // grid) - 1) * grid)

        self.dir = [(0, -grid * 2), (0, grid * 2), (-grid * 5, 0), (grid * 5, 0)]

        self.color = color
        self.hunger = 0

    def move(self):
        dx, dy = rnd.choice(self.dir)

        self.x += dx
        self.y += dy 

        self.x = max(0, min(self.x, self.dw - self.grid))
        self.y = max(0, min(self.y, self.dh - self.grid))

    def movetofood(self, food):
        if self.hunger < 5:
            if self.x < food.x:
                self.x += self.grid * 2
            elif self.x > food.x:
                self.x -= self.grid * 2

            if self.y < food.y:
                self.y += self.grid * 2
            elif self.y > food.y:
                self.y -= self.grid * 2

        if self.hunger > 5:
            if self.x < food.x:
                self.x -= self.grid * 2
            elif self.x > food.x:
                self.x += self.grid * 2

            if self.y < food.y:
                self.y -= self.grid * 2
            elif self.y > food.y:
                self.y += self.grid * 2

    def draw(self, display):
        pg.draw.rect(display, self.color, (self.x, self.y, self.grid, self.grid))

    def getrect(self):
        return pg.Rect(self.x, self.y, self.grid, self.grid)
    
    def gethunger(self, hunger):
        self.hunger += hunger
        return self.hunger

class Predator():
    def __init__(self, grid, dw, dh):
        super().__init__()

        self.grid = grid
        self.dw = dw
        self.dh = dh

        self.x = rnd.randint(0, (dw // grid - 1) * grid)
        self.y = rnd.randint(0, (dh // grid - 1) * grid)

        self.dir = [(0, -grid), (0, grid), (-grid, 0), (grid, 0)]

        self.hunger = 0

    def move(self):
        dx, dy = rnd.choice(self.dir)

        self.x += dx
        self.y += dy

        self.x = max(0, min(self.x, self.dw - self.grid))
        self.y = max(0, min(self.y, self.dh - self.grid))

    def movetofish(self, fish):
        if self.hunger < 5:
            if self.x < fish.x:
                self.x += self.grid * 3
            elif self.x > fish.x:
                self.x -= self.grid * 3

            if self.y < fish.y:
                self.y += self.grid * 3
            elif self.y > fish.y:
                self.y -= self.grid * 3

    def draw(self, display):
        pg.draw.rect(display, predator_color, (self.x, self.y, self.grid, self.grid))

    def getrect(self):
        return pg.Rect(self.x, self.y, self.grid, self.grid)
    
    def gethunger(self, hunger):
        self.hunger += hunger
        return self.hunger
    
    def gethungerafter(self):
        return self.hunger

class Food():
    def __init__(self, grid, dw, dh):
        super().__init__()

        self.grid = grid
        self.dw = dw
        self.dh = dh

        self.x = rnd.randint(0, (dw // grid - 1) * grid)
        self.y = rnd.randint(0, 50)

        self.dir = [(0, grid), (-grid, 0), (grid, 0)]

    def move(self):
        dx, dy = rnd.choice(self.dir)

        self.x += dx
        self.y += dy

        self.x = max(0, min(self.x, self.dw - self.grid))
        self.y = max(0, min(self.y, self.dh - self.grid))

    def draw(self, display):
        pg.draw.rect(display, food_color, (self.x, self.y, self.grid, self.grid)) 

    def getrect(self):
        return pg.Rect(self.x, self.y, self.grid, self.grid)

class Plant():
    def __init__(self, grid, dw, dh, color):
        self.grid = grid
        self.dw = dw
        self.dh = dh

        self.x = rnd.randint(0, ((dw // grid) - 1) * grid)
        self.y = 500

        self.dir = [(0, -grid * 2), (-grid, 0), (grid, 0)]

        self.segment = []

        self.color = color

    def grow(self):
        dx, dy = rnd.choice(self.dir)

        self.x += dx
        self.y += dy

        if dy != 0:
            self.segment.append((self.x, self.y, self.grid, self.grid * 2))

        if dx != 0:
            self.segment.append((self.x, self.y, self.grid * 1.5, self.grid))


        self.x = max(16, min(self.x, self.dw - self.grid * 3))
        self.y = max(50, min(self.y, self.dh))

        if self.y == 50:
            self.y = dy
            self.x = dx
        
    def draw(self, display):
        for seg in self.segment:
            pg.draw.rect(display, self.color, seg)
    
fishes = []
fishcount = 0

foods = []
foodcount = 0

plants = []

predators = []

rect = pg.Rect(0, 0, 800, 500)
sub = display.subsurface(rect)
downloads = os.path.join(os.path.expanduser("~"), "Downloads")
name = "aquabit_screenshot"
ext = "png"
filename = name + "." + ext
count = 1
    
tick = pg.time.Clock()

def collider():
    for fish in fishes:
        for food in foods:
            if fish.getrect().colliderect(food.getrect()):
                fish.gethunger(1)
                foods.remove(food)

                break

    for predator in predators:
        for fish in fishes:
            if predator.getrect().colliderect(fish.getrect()):
                predator.gethunger(1)
                fishes.remove(fish)

                break



def fishtofood():
    if len(foods) > 0:
        food = foods[0]
        for fish in fishes:
            fish.movetofood(food)

def predtofish():
    if len(fishes) > 0:
        fish = fishes[0]
        for predator in predators:
            predator.movetofish(fish)

def killpredator():
    for predator in predators:
        if predator.gethungerafter() == 5:
            predators.remove(predator)

            break

zpress = False
cpress = False
xpress = False
vpress = False
spress = False

run = True

while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_z:
                zpress = True
                if len(fishes) < 50:
                    fishes.append(Fish(rnd.randint(8, 16), 800, 500, rnd.choice(fish_colors)))
                    fishcount += 1

            if event.key == pg.K_c:
                cpress = True
                if len(foods) < 20:
                    foods.append(Food(10, 800, 500))
                    foodcount += 1

            if event.key == pg.K_x:
                xpress = True
                if len(predators) < 5:
                    predators.append(Predator(16, 800, 500))

            if event.key == pg.K_v:
                vpress = True
                if len(plants) < 20:
                    plants.append(Plant(8, 800, 500, rnd.choice(plant_colors)))

            if event.key == pg.K_s:
                while os.path.exists(os.path.join(downloads, filename)):
                    filename = name + " (" + str(count) + ")." + ext
                    count += 1

                pg.image.save(sub, os.path.join(downloads, filename))
                spress = True

            if event.key == pg.K_z:
                d = pg.key.get_pressed()
                if d[pg.K_d]:
                    fishes.clear()

            if event.key == pg.K_x:
                d = pg.key.get_pressed()
                if d[pg.K_d]:
                    predators.clear()

            if event.key == pg.K_c:
                d = pg.key.get_pressed()
                if d[pg.K_d]:
                    foods.clear()

            if event.key == pg.K_v:
                d = pg.key.get_pressed()
                if d[pg.K_d]:
                    plants.clear()

    display.fill(display_color)

    fishtofood()
    predtofish()
    killpredator()
    collider()

    for plant in plants:
        plant.grow()
        plant.draw(display)
        
    for food in foods:
        food.move()
        food.draw(display)

    for fish in fishes:
        fish.move()
        fish.draw(display)

    for predator in predators:
        predator.move()
        predator.draw(display)
    
    pg.draw.rect(display, (118, 172, 209), (800, 0, 190, 500))

    fishcount_txt = font.render("Fishes:          " + str(len(fishes)) + "/50", True, (0, 0, 0))
    display.blit(fishcount_txt, (815, 20))

    predcount_txt = font.render("Predators:     " + str(len(predators)) + "/5", True, (0, 0, 0))
    display.blit(predcount_txt, (815, 40))

    foodcount_txt = font.render("Food Pellets:  " + str(len(foods)) + "/20", True, (0, 0, 0))
    display.blit(foodcount_txt, (815, 60))

    plantcount_txt = font.render("Plants:           " + str(len(plants)) + "/20", True, (0, 0, 0))
    display.blit(plantcount_txt, (815, 80))

    screenshot_taken_txt = font.render("Screenshot Saved!", False, (0, 0, 0))
    if spress:
        display.blit(screenshot_taken_txt, (815, 100))
        spress = False
        tick.tick(2)

    display.blit(font.render("Hold D & Press:", True, (0, 0, 0)), (815, 140))
    dkey = pg.key.get_pressed()
    if dkey[pg.K_d]:
        display.blit(font.render("Z - Kill All Fish", True, (0, 0, 0)), (815, 165))
        display.blit(font.render("X - Kill All Predators", True, (0, 0, 0)), (815, 185))
        display.blit(font.render("C - Remove All Pellets", True, (0, 0, 0)), (815, 205))
        display.blit(font.render("V - Kill All Plants", True, (0, 0, 0)), (815, 225))

    pg.display.flip()
    tick.tick(8)

pg.quit()