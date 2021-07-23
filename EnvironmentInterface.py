import abc

class EnvironmentInterface(abc.ABC):

    @abc.abstractmethod
    def num_actions_available(self) -> int:
        """This should return a int of how many possible actions there are."""
        pass

    @abc.abstractmethod
    def get_screen_height(self) -> int:
        """Extract height of the window."""
        pass

    @abc.abstractmethod
    def get_screen_width(self) -> int:
        """Extract width of the window."""
        pass

    @abc.abstractmethod
    def reset(self) -> None:
        """Should reset the whole environment."""
        pass

    @abc.abstractmethod
    def step(self, action: int) -> dict:
        """Should reset the whole environment."""
        pass

    @abc.abstractmethod
    def render(self):
        """Should reset the whole environment."""
        pass

