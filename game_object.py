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


if __name__ == "__main__":
    mob1 = Mage((40, 50))
    mob1.move(Vector(-10, 50))
