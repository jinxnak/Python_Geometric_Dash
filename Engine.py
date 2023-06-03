import pygame

class Game:
     def __init__ (self):
        pygame.init ()
        self.runing, self.playing = True, True
        self.WIDTH , self.HIGH = 1880, 900
        self.Font_name = "font1.ttf"
        self.screen = pygame.display.set_mode((self.WIDTH, self.HIGH))
        self.Black, self.Withe = (0, 0, 0), (255, 255, 255)
        self.x_ply, self.y_ply = 400, 400
        self.player = pygame.Rect(self.x_ply, self.y_ply, 50, 50)
        self.v0 = 1
        self.ground = pygame.Rect(550, 600, 5000, 100)
        self.color_ground = self.Withe
        self.color_player = self.Withe
        self.camera_x, self.camera_y = 0, 0

     def play (self):
         pygame.display.set_caption ("Geometic-Dash")
         clock = pygame.time.Clock ()
         while self.playing:
             clock.tick(60)
             self.check_events ()
             pygame.draw.rect(self.screen, self.color_player, self.player, 0)
             pygame.draw.rect(self.screen, self.color_ground, self.ground, 0)
             print (clock.get_time())
             pygame.display.update ()
             pygame.display.flip ()
    

     def init_joystick (self):
        joysticks = []
        for i in range (0,  pygame.joystick.get_count()):
            joysticks.append (pygame.joystick.Joystick (i))
            joysticks[-1].init ()

     def check_events (self):
         self.init_joystick ()
         for events in pygame.event.get ():
            if events.type == pygame.QUIT:
                self.playing, self.runing = False, False
            if events.type == pygame.JOYBUTTONDOWN:
                if events.button == 0:
                    print ("A")
                if events.button == 1:
                    print ("B")
                if events.button == 2:
                    print ("X")
                if events.button == 3:
                    print ("Y")
                if events.button == 4:
                    print ("LB")
                if events.button == 5:
                    print ("RB")
                if events.button == 6:
                    print ("BACK")
                if events.button == 7:
                    print ("START")
                if events.button == 8:
                    print ("Xbox")
                if events.button == 9:
                    print ("click joy1")
                if events.button == 10:
                    print ("click joy2")
                if events.button == 11:
                    print ("11")
    

     def print_text (self, text, size, color, x, y):
        font = pygame.font.Font (self.Font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect ()
        text_rect.center = (x, y)
        self.screen.blit (text_surface, text_rect)

     #def move_player (self, time):