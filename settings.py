# -*- coding: utf-8 -*-
"""
Created on =2020-09-14

@author: wenshijie
"""


class Settings:
    """储存《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""

        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        # self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # 子弹设置
        # self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 外星人设置
        # self.alien_speed_factor = 1
        self.fleet_drop_speed = 3

        # fleet_direction为1表示向右移动，为-1表示向左移
        # self.fleet_direction = 1

        # 以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随机游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction为1表示向右移动，为-1表示向左移
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale