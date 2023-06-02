class Modes:
    CUSTOM_WINDOWS = 0
    MINING_PROJECT_GREEN = 1  # Работает только на Вентуре с дронами


class ProgramMode:
    state = None

    def __init__(self, state: int):
        self.state = state
