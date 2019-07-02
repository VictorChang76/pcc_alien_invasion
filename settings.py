class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """initialise the game's settings."""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230) # light grey

        # Ship settings
        self.ship_speed = 1.5