import gymnasium as gym

class BatteryWrapper(gym.Wrapper):
    def __init__(self, env):
        super().__init__(env)
