class GameSetting():
    """docstring for Game_Setting"""

    def __init__(self):
        self.game_width = 1200
        self.game_height = 600
        self.game_bgColor = (230, 230, 230)
        self.game_name = "星球大战"
        self.ship_speed_factor = 1.5
        self.ship_limit = 3
        self.bullet_speed_factor = 4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 50
        self.star_count = 100
        self.alien_speed_factor = 0.5
        self.fleet_drop_speed = 10
        self.fleet_direction = 1
