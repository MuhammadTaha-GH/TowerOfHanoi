# def towerOfHanoi(n, source, destination, auxiliary):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {destination}")
#         return    
#     towerOfHanoi(n - 1, source, auxiliary, destination)
#     print(f"Move disk {n} from {source} to {destination}")
#     towerOfHanoi(n - 1, auxiliary, destination, source)

# n = int(input("Enter the number of disks: "))
# if n <= 0:
#     print("Number of disks must be a positive integer.")
# else:
#     print(f"Steps to solve Tower of Hanoi with {n} disks:")
#     towerOfHanoi(n, 'A', 'C', 'B')


import pygame
import time

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tower of Hanoi")

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 102, 204)
red = (204, 0, 0)
green = (0, 204, 0)
yellow = (255, 204, 0)
gray = (200, 200, 200)

pegX = [200, 400, 600]
pegY = 400
diskHeight = 20

font = pygame.font.Font(None, 36)

def drawPeg(x, y):
    pygame.draw.rect(screen, black, (x - 5, y - 200, 10, 200))

def drawDisk(x, y, width, color):
    pygame.draw.rect(screen, color, (x - width // 2, y, width, diskHeight))

def initializeDisks(n):
    disks = []
    for i in range(n):
        width = 140 - i * 20
        color = [red, blue, green, yellow][i % 4]
        disks.append({'width': width, 'color': color})
    return disks

def drawScene(pegs, disks):
    screen.fill(white)
    for x in pegX:
        drawPeg(x, pegY)
    for pegIndex, pegDisks in enumerate(pegs):
        x = pegX[pegIndex]
        for i, disk in enumerate(pegDisks):
            y = pegY - (i + 1) * diskHeight
            drawDisk(x, y, disk['width'], disk['color'])
    pygame.display.update()

def moveDisk(n, source, destination, pegs, disks):
    disk = pegs[source].pop()
    pegs[destination].append(disk)
    drawScene(pegs, disks)
    time.sleep(0.5)

def towerOfHanoi(n, source, destination, auxiliary, pegs, disks):
    if n == 1:
        moveDisk(n, source, destination, pegs, disks)
        return
    towerOfHanoi(n - 1, source, auxiliary, destination, pegs, disks)
    moveDisk(n, source, destination, pegs, disks)
    towerOfHanoi(n - 1, auxiliary, destination, source, pegs, disks)

def inputNumber():
    input_active = True
    user_input = ""
    while input_active:
        screen.fill(white)
        prompt = font.render("Enter the number of disks (1-7):", True, black)
        screen.blit(prompt, (200, 250))
        
        input_box = pygame.Rect(300, 300, 200, 50)
        pygame.draw.rect(screen, gray, input_box, 0)
        pygame.draw.rect(screen, black, input_box, 2)
        
        text_surface = font.render(user_input, True, black)
        screen.blit(text_surface, (input_box.x + 10, input_box.y + 10))
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if user_input.isdigit() and 1 <= int(user_input) <= 7:
                        return int(user_input)
                    else:
                        user_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

def main():
    running = True
    clock = pygame.time.Clock()
    n = inputNumber()
    
    disks = initializeDisks(n)
    pegs = [[], [], []]
    pegs[0] = disks[:]
    drawScene(pegs, disks)
    time.sleep(1)
    towerOfHanoi(n, 0, 2, 1, pegs, disks)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(30)
    pygame.quit()

if __name__ == "__main__":
    main()
