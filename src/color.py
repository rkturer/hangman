import colorama as color
color.init(autoreset=True)

class Color:
    """handles everything regarding colors """
    def __init__(self):
        """initializes the colors as attributes of Color class for further use"""
        self.reset = color.Style.RESET_ALL
        self.good = color.Fore.GREEN
        self.bad = color.Fore.RED 
        self.header = color.Fore.LIGHTYELLOW_EX 
        self.border = color.Fore.LIGHTCYAN_EX