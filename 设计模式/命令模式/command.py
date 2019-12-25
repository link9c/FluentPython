class MacroCommand:
    """执行一组命令"""

    def __init__(self, commands):
        self.commands = list(commands)

    def __call__(self, *args, **kwargs):
        for command in self.commands:
            command()
