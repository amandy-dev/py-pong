import utils.racket as racket
import utils.pygame

rack = racket.Racket("left")
dove = racket.Racket("right")

rackets = [rack, dove]

while utils.pygame.running:
    utils.pygame.keys = utils.pygame.pygame.key.get_pressed()
    for event in utils.pygame.pygame.event.get():
        if(event.type == utils.pygame.pygame.QUIT or utils.pygame.keys[utils.pygame.pygame.K_ESCAPE] == True):
            utils.pygame.running = False

    for racketi in rackets:
        racketi.move(utils.pygame.keys)

    utils.pygame.screen.fill("black")
    
    for racketi in rackets:
        racketi.draw()

    utils.pygame.pygame.display.flip()

    utils.pygame.dt = utils.pygame.clock.tick(60) / 1000

utils.pygame.pygame.quit()