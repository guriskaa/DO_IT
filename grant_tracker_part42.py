# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: GrantTracker
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    HIDDEN = "\033[8m"
    COLORS = {
        "black": "\033[30m", "red": "\033[31m", "green": "\033[32m",
        "yellow": "\033[33m", "blue": "\033[34m", "magenta": "\033[35m",
        "cyan": "\033[36m", "white": "\033[37m",
        "bg_black": "\033[40m", "bg_red": "\033[41m", "bg_green": "\033[42m",
        "bg_yellow": "\033[43m", "bg_blue": "\033[44m", "bg_magenta": "\033[45m",
        "bg_cyan": "\033[46m", "bg_white": "\033[47m",
    }

    @classmethod
    def enable(cls):
        try:
            import os; os.environ["NO_COLOR"] = ""
            cls._enabled = True
        except Exception:
            cls._enabled = False

    @classmethod
    def disable(cls):
        try:
            import os; os.environ["NO_COLOR"] = "1"
            cls._enabled = False
        except Exception:
            pass

    @classmethod
    def _is_enabled(cls):
        return cls._enabled if hasattr(cls, "_enabled") else False

    @classmethod
    def text(cls, text, color=None, bg=None, bold=False):
        if not cls._is_enabled():
            return text
        prefix = ""
        if bold:
            prefix += cls.BOLD
        if color and color in cls.COLORS:
            prefix += cls.COLORS[color]
        if bg and bg in cls.COLORS:
            prefix += cls.COLORS[bg]
        suffix = cls.RESET
        return f"{prefix}{text}{suffix}"
