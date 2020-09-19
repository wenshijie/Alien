# -*- coding: utf-8 -*-
"""
Created on =2020-09-14

@author: wenshijie
"""
import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)
        # 更新飞船位置
        ship.update()
        # 每次循环都重绘屏幕并绘制
        gf.update_screen(ai_settings, screen, ship)


run_game()
