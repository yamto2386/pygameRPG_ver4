import pygame
from Player import *
from option import *
import sys
# user1 = MyClass ( ) の形は　インスタンスの作成

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        #self.font = pygame.font.Font()
        self.running = True
        self.font = pygame.font.Font("arial.ttf", 32)
        self.count = 1
        self.x = 0
        

        self.character_spritesheet = Spritesheet("img/character.png")
        self.terrain_spritesheet = Spritesheet("img/terrain.png")
        self.house_spritesheet = Spritesheet("img/house.png")
        self.enemy_spritesheet = Spritesheet("img/enemy.png")
        self.enemy_2_spritesheet = Spritesheet("img/enemy_2.png")
        self.attack_spritesheet = Spritesheet("img/attack.png")
        self.intro_background = pygame.image.load("./img/introbackground.png")
        self.go_background = pygame.image.load("./img/gameover.png")

    def createTilemap(self):
        for i, row in enumerate(tilemap):
            for j, colum in enumerate(row):
                self.ground = Ground(self, j, i)
                if colum == "B":
                    self.block = Block(self, j, i)
                if colum == "S":
                    self.stair = Stairs(self, j, i)
                if colum == "E":
                    self.enemy = Enemy(self, j, i)
                if colum == "X":
                    self.enemy_2 = Enemy_2(self, j, i)
                if colum == "P":
                    self.player = Player(self, j, i)


    def new(self):
        #a new game start
        self.playing = True
        #ここは全てのステータスにレイヤーの処理を持たせる
        self.all_sprites = pygame.sprite.LayeredUpdates() #レイヤーを制御し、OrderedUpdatesのように画像描写処理を行うLayeredUpdates Groupクラス
        self.blocks = pygame.sprite.LayeredUpdates()
        self.stairs = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.enemies_2 = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap()


    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.player.facing == 'up':
                        Attack(self, self.player.rect.x, self.player.rect.y - TILESIZE)
                    if self.player.facing == 'down':
                        Attack(self, self.player.rect.x, self.player.rect.y + TILESIZE)
                    if self.player.facing == 'left':
                        Attack(self, self.player.rect.x - TILESIZE, self.player.rect.y )
                    if self.player.facing == 'right':
                        Attack(self, self.player.rect.x + TILESIZE, self.player.rect.y )



    def update(self):
        #ok
        #game loop updates
        self.all_sprites.update()#update は各クラスのupdate
    
    def draw(self):
        #game loop draw
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def game_over(self):
        text = self.font.render("Game Over", True, WHITE)
        text_rect = text.get_rect(center=(WIN_WIDTH/2, WIN_HEIGHT/2))

        restart_button = Button(10, WIN_HEIGHT - 60, 120, 50, WHITE, BLACK, "Restart", 32)

        for sprite in self.all_sprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()

            self.screen.blit(self.go_background, (0, 0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()



    def intro_screen(self):
        intro = True

        title = self.font.render("Awesome Game", True, BLACK)
        title_rect = title.get_rect(x=10, y=10)

        play_button = Button(10, 50, 100, 50, WHITE, BLACK, "Play", 32)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False

            mouse_pos = pygame.mouse.get_pos() #マウスカーソルの位置情報を取得します。
            mouse_pressed = pygame.mouse.get_pressed() #マウスボタンの状態を取得します。

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            
            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def down_floor(self):
        tilemap_ch2.clear()
        self.make_tilemap()
        self.new_ch()
        self.main()
        self.count_floor()
        

    def count_floor(self):
        self.count +=1
        print("フロア数")
        print(self.count)
        print("count_floorでのスコープ")
        print(locals())
        
        
    def Boss_floor(self):
        print("動いてるよ2")
        self.CreateBoss_tilemap()
        self.Boss_ch()
        self.main()

    def new_ch(self):
        #a new game start
        self.playing = True
        #ここは全てのステータスにレイヤーの処理を持たせる
        self.all_sprites = pygame.sprite.LayeredUpdates() #レイヤーを制御し、OrderedUpdatesのように画像描写処理を行うLayeredUpdates Groupクラス
        self.blocks = pygame.sprite.LayeredUpdates()
        self.stairs = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.enemies_2 = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.createTilemap_ch()

    def Boss_ch(self):
        #a new game start
        self.playing = True
        #ここは全てのステータスにレイヤーの処理を持たせる
        self.all_sprites = pygame.sprite.LayeredUpdates() #レイヤーを制御し、OrderedUpdatesのように画像描写処理を行うLayeredUpdates Groupクラス
        self.blocks = pygame.sprite.LayeredUpdates()
        self.stairs = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.enemies_2 = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()

        self.CreateBoss_tilemap()


    def createTilemap_ch(self):
        print(self.count)
        print("createTilemap_chでのスコープ")
        print(locals())

        #if self.count == 10:
            #print("確認しました")
            #self.Boss_floor()

        for i, row in enumerate(tilemap_ch2):
            for j, colum in enumerate(row):
                self.ground = Ground(self, j, i)
                if colum == "B":
                    self.block = Block(self, j, i)
                if colum == "S":
                    self.stair = Stairs(self, j, i)
                if colum == "E":
                    self.enemy = Enemy(self, j, i)
                if colum == "X":
                    self.enemy_2 = Enemy_2(self, j, i)
                if colum == "P":
                    self.player = Player(self, j, i)

    def CreateBoss_tilemap(self):
        for i, row in enumerate(tilemap_Boss):
            for j, colum in enumerate(row):
                self.ground = Ground(self, j, i)
                if colum == "B":
                    self.block = Block(self, j, i)
                if colum == "S":
                    self.stair = Stairs(self, j, i)
                if colum == "E":
                    self.enemy = Enemy(self, j, i)
                if colum == "X":
                    self.enemy_2 = Enemy_2(self, j, i)
                if colum == "P":
                    self.player = Player(self, j, i)

    def make_tilemap(self):
        tilemap_ch2.append(ST_ED_Block)
        for num in range(13):
                x = random.randint(1,5)
                if num == 5:
                    tilemap_ch2.append(MakePlayerStair)
                elif x == 1:
                    tilemap_ch2.append('B..................B')
                elif x == 2:
                    tilemap_ch2.append('B.......B.....E....B')
                elif x == 3:
                    tilemap_ch2.append('B.............BBB..B')
                elif x == 4:
                    tilemap_ch2.append('B...............E..B')
                elif x == 5:
                    tilemap_ch2.append('B..X..........B....B')
        
        tilemap_ch2.append(ST_ED_Block)

g = Game() #インスタンス作成
g.intro_screen()
g.new()

while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()
