import pygame
from setup import*
from tileconfig import Tile
from playerconfig import Player
from debugfn import debug
from importfn import*
class Level:
    def __init__(self):
        
        #get displaysurf
        self.display_surface = pygame.display.get_surface()

        #Initialize Sprite Group
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        #setup sprite
        self.create_map()
    
    def create_map(self):
        layout = {
                    'boundary' : import_csv_layout('../graphics/map_data/mainmap_constraints.csv'),
                    'objects' : import_csv_layout('../graphics/map_data/mainmap_objects.csv'),
        } #1:38:59
        for style,layout in layout.items():
            for row_index,row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacle_sprites],'invisible')
#                if col  == 'x':
#                    Tile((x,y),[self.visible_sprites,self.obstacle_sprites])
#                if col == 'p':
#                    self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites)
        self.player = Player((2000,1575),[self.visible_sprites],self.obstacle_sprites)                  
                    
    
    def run(self):
        #Update and Draw
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        #Basic Initialization
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
        #Create Floor
        self.floor_surf = pygame.image.load('../graphics/mainmap/mainmap.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
        
    def custom_draw(self,player):
    
        #Get Offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        #drawing floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)
        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)