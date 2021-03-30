import pygame
from pygame.locals import K_p, K_n

from Projekt2.Ball import Ball
from Projekt2.Player import Player
from Projekt2.levels.Level import Level


class GameLevel(Level):
    def __init__(self, screen, bricks):
        super(GameLevel, self).__init__(screen)
        self.player = Player(305, 450, self.width)
        self.ball = Ball(315, 440)
        self.bricks = bricks

    def nextLoop(self):
        if self.gameIsPaused is False:
            pressed_keys = pygame.key.get_pressed()
            self.player.update(pressed_keys)
            self.draw()
            if self.ball is not None:
                # self.handleCollision()
                self.ball.move()
        else:
            self.draw()
            # self.drawPausedText()

    def handleInput(self, key):
        if key == K_p:
            self.togglePause()
        if key == K_n:
            self.disactiveLevel()

    def draw(self):
        self.screen.fill((0, 0, 0))
        if self.player is not None:
            self.screen.blit(self.player.surf, self.player.rect)
        for brick in self.bricks:
            self.screen.blit(brick.surf, brick.rect)
        if self.ball is not None:
            self.screen.blit(self.ball.surf, self.ball.rect)