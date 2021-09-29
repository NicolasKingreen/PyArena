import pygame

from game_object import Player


class Game:

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen_surface = pygame.display.set_mode((1024, 640))
        self.render_surface = pygame.Surface((1024, 640))
        pygame.display.set_caption("Arena")

        self.is_running = False

    def run(self):

        player1 = Player((32*16, 20*16))

        self.is_running = True
        while self.is_running:

            frame_time_ms = self.clock.tick(24)
            frame_time_s = frame_time_ms / 1000.

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.stop()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.stop()

            player1.process_input()
            player1.update(frame_time_s)

            self.render_surface.fill((255, 255, 255))
            player1.draw(self.render_surface)
            self.screen_surface.blit(pygame.transform.scale(self.render_surface, self.screen_surface.get_size()), (0, 0))
            # self.screen_surface.blit(self.render_surface, (0, 0))
            pygame.display.update()

    def stop(self):
        self.is_running = False
        print("[Game] Stopping the game...")


if __name__ == "__main__":
    Game().run()
