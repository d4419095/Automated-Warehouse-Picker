import gymnasium as gym

class CurriculumWrapper(gym.Wrapper):
    def __init__(self, env):
        super().__init__(env)
