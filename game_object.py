import pygame

Vector = pygame.math.Vector2
Sprite = pygame.sprite.Sprite


def load_sprites(sprite_sheet_path, sprite_size):
    sprite_sheet = pygame.image.load(sprite_sheet_path)
    # TODO:


class GameObject:

    def __init__(self, spawn_coordinates):
        self._coordinates = Vector(spawn_coordinates)

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, new_coordinates):
        if isinstance(new_coordinates, Vector):
            self._coordinates = new_coordinates
        else:
            raise TypeError()


class Entity(GameObject, Sprite):

    def __init__(self, spawn_coordinates, *groups):
        super().__init__(spawn_coordinates)
        pygame.sprite.Sprite.__init__(self, *groups)
        print(f"{self.__class__.__name__} ({self.coordinates}) created")

    def move(self, move_vector: Vector):
        self.coordinates += move_vector
        print(f"Moved to {self.coordinates}")

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.coordinates, (32, 32)))


class Mage(Entity):
    pass


class Player(Entity):
    def __init__(self, spawn_coordinates):
        super().__init__(spawn_coordinates)
        self.image = pygame.image.load("sprites/male1.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 16, self.image.get_height() * 16))
        self.rect = self.image.get_rect(center=spawn_coordinates)
        self.moving_direction = pygame.math.Vector2()
        self.speed = 1000
        self.facing_right = True

    def process_input(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_d]:
            self.moving_direction.x = 1
        if pressed_keys[pygame.K_a]:
            self.moving_direction.x = -1
        if pressed_keys[pygame.K_s]:
            self.moving_direction.y = 1
        if pressed_keys[pygame.K_w]:
            self.moving_direction.y = -1

        if self.moving_direction:
            self.moving_direction = self.moving_direction.normalize()
        # print(self.moving_direction)
    
    def update(self, frame_time_s):

        if self.moving_direction.x > 0:
            if self.facing_right is not True:
                self.facing_right = True
                self.image = pygame.transform.flip(self.image, True, False)
                print("Changed to right")
        elif self.moving_direction.x < 0:
            if self.facing_right is not False:
                self.facing_right = False
                self.image = pygame.transform.flip(self.image, True, False)
                print("Changed to left")

        move_vector = self.moving_direction * self.speed * frame_time_s
        self.coordinates += move_vector
        self.rect.center = self.coordinates
        self.moving_direction = pygame.math.Vector2()
        # print(self.rect.center)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


if __name__ == "__main__":
    mob1 = Mage((40, 50))
    mob1.move(Vector(-10, 50))
