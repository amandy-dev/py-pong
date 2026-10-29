import utils.pygame


class Racket:
    posX=0
    posY=0
    width=0
    height=0
    color=""

    def __init__(self, side: string, width=10, height=50, color="white"):
        if(side == "left"):
            self.posX = 5
        elif(side == "right"):
            self.posX = utils.pygame.screen.get_width() - (5 + width)
        else:
            print("ERROR: Could not identify racket side!")

        self.posY = (utils.pygame.screen.get_height() / 2) - (height / 2)
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        utils.pygame.pygame.draw.rect(utils.pygame.screen, self.color, (self.posX, self.posY, self.width, self.height))

    def move(self, move_keys):
        self.posY += (move_keys[utils.pygame.pygame.K_DOWN] - move_keys[utils.pygame.pygame.K_UP]) * 500 * utils.pygame.dt

