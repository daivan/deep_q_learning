from EnvironmentInterface import EnvironmentInterface
from gym import core, spaces
import random

class JellyEnvironment(EnvironmentInterface):



    BOARD = [1,2,3,4,5,6]

    def __init__(self):
        self.action_space = spaces.Discrete(3)

    def num_actions_available(self) -> int:
        """This should return a int of how many possible actions there are."""
        return 3
        
    def get_screen_height(self) -> int:
        """Extract height of the window."""
        return 2

    def get_screen_width(self) -> int:
        """Extract width of the window."""
        return 2

    def reset(self) -> None:
        """Should reset the whole environment also provide the step() ."""
        pass

    def step(self, action: int) -> dict:
        """Should return state, reward, done, and extra, (extra is seldom used)."""
        state = self.get_state()
        reward = action
        done = random.randint(0, 1)
        #done = False
        return (state, reward, done, {})

    def render(self):
        return self.BOARD

    def get_state(self):
        return self.BOARD        

    def close(self):
        return False

