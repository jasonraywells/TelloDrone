import pygame

def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))

#when creating a module use if command and set a logic
if __name__ == '__main__':
    init()



def getKey(KeyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(KeyName))
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey("LEFT"):
        print("Left Key Pressed")
    if getKey("RIGHT"):
        print("Right Key Pressed")

    #print(getKey("a"))

if __name__ == '__main__':
    init()
    while True:
        main()

