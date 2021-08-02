import pygame
import os


UPGRADE_MENU_IMAGE = pygame.image.load(os.path.join("images", "upgrade_menu.png"))
UPGRADE_BTN_IMAGE = pygame.image.load(os.path.join("images", "upgrade.png"))
SELL_BTN_IMAGE = pygame.image.load(os.path.join("images", "sell.png"))


class UpgradeMenu:
    def __init__(self, x, y):
        self.menu = pygame.transform.scale(UPGRADE_MENU_IMAGE, (200, 200))
        self.rect = self.menu.get_rect()
        self.rect.center = (x, y)
        self.__buttons = [Button(UPGRADE_BTN_IMAGE, "upgrade", self.rect.centerx - 24, self.rect.centery - 95),
                          Button(SELL_BTN_IMAGE, "sell", self.rect.centerx - 24, self.rect.centery + 50)]  # (Q2) Add buttons here

    def draw(self, win):
        """
        (Q1) draw menu itself and the buttons
        (This method is call in draw() method in class TowerGroup)
        :return: None
        """
        # draw menu
        win.blit(self.menu, (self.rect.centerx - 100, self.rect.centery - 100))
        # draw button
        # win.blit(self.upgrade, (225, 280))
        # win.blit(self.sell, (210, 425))
        # (Q2) Draw buttons here
        for btn in self.__buttons:
            win.blit(btn.scale, (btn.x, btn.y))

    def get_buttons(self):
        """
        (Q1) Return the button list.
        (This method is called in get_click() method in class TowerGroup)
        :return: list
        """
        return self.__buttons


class Button:
    def __init__(self, image, name, x, y):
        self.name = name
        self.scale = pygame.transform.scale(image, (45, 45))
        self.x = x
        self.y = y
        self.rect = self.scale.get_rect()

    def clicked(self, x, y):
        """
        (Q2) Return Whether the button is clicked
        (This method is called in get_click() method in class TowerGroup)
        :param x: mouse x
        :param y: mouse y
        :return: bool
        """
        return True if self.rect.collidepoint(x, y) else False
        # pass

    def response(self):
        """
        (Q2) Return the button name.
        (This method is call in get_click() method in class TowerGroup)
        :return: str
        """
        return self.name






