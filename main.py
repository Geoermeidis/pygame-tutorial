import pygame

pygame.init()  # Ξεκιναει το παιχινιδι

win = pygame.display.set_mode((500, 480))  # παράθυρο του πΑιχνιδιού ((width, height))

pygame.display.set_caption("First game")  # Όνομα παιχνιδιού

walkRight = [pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\R1.png'),
             pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\R2.png'),
             pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\R3.png'),
             pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\R4.png'),
             pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\R5.png'),
             pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\R6.png'),
             pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\R7.png'),
             pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\R8.png'),
             pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\R9.png')]
walkLeft = [pygame.image.load("C:\\Users\\ermei\\Desktop\\Game\\L1.png"),
            pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\L2.png'),
            pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\L3.png'),
            pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\L4.png'),
            pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\L5.png'),
            pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\L6.png'),
            pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\L7.png'),
            pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\L8.png'),
            pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\L9.png')]
# ΔΥΟ ΛΙΣΤΕΣ Ο ΧΑΡΑΚΤΗΡΑΣ ΚΙΝΕΙΤΑΙ ΔΕΞΙΑ ΚΑΙ ΑΡΙΣΤΕΡΑ
bg = pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\bg.jpg')  # BACKGROUND image
char = pygame.image.load('C:\\Users\\ermei\\Desktop\\Game\\standing.png')  # ΕΙΚΟΝΑ ΤΟΥ ΧΑΡΑΚΤΗΡΑ ΟΤΑΝ ΕΙΝΑΙ ΣΤΑΘΕΡΟΣ

screenwidth = 500
screenheight = 480

clock = pygame.time.Clock()
x = 50  # Θεση χ του χαρακτήρα
y = 400  # Θεση υ του χαρακτήρα
width = 40  # Μάκρος του
height = 60  # Ύψος του
vel = 5  # Ταχύτητα - velocity του

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0


def redraw():
    global walkCount
    win.blit(bg, (0, 0))
    # ΓΕΜΙΖΕΙ ΤΟ ΠΑΡΑΘΥΡΟ ΞΑΝΑ, ΕΤΣΙ Ο ΧΑΡΑΚΤΗΡΑΣ ΦΕΝΕΤΑΙ ΝΑ ΚΙΝΕΙΤΑΙ ΚΑΘΕ ΦΟΡΑ ΚΙΑ ΟΧΙ ΑΠΛΑ ΝΑ ΣΕΡΝΕΤΑΙ
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
    pygame.display.update()


run = True
while run:
    clock.tick(27)

    for event in pygame.event.get():  # event in python είναι οτιδήποτε κάνει ο χρήστης π.χ κουναάει το ποντίκι
        # pygame.event.get = λιστα όλων των event
        if event.type == pygame.QUIT:  # Exit button
            run = False

    keys = pygame.key.get_pressed()  # ΛΙΣΤΑ ΚΟΥΜΠΙΩΝ
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screenwidth - width - vel:
        x += vel
        left = False
        right = True
    else:
        right = False
        left = False
        walkCount = 0
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) / 2 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    redraw()
pygame.quit()
