import pygame
import random
import math

import numpy as np

class JellyEnv():

    """
    Description:
        The agent (a car) is started at the bottom of a valley. For any given
        state the agent may choose to accelerate to the left, right or cease
        any acceleration.
    Source:
        The environment appeared first in Andrew Moore's PhD Thesis (1990).
    Observation:
        Type: Box(2)
        Num    Observation               Min            Max
        0      Car Position              -1.2           0.6
        1      Car Velocity              -0.07          0.07
    Actions:
        Type: Discrete(3)
        Num    Action
        0      Accelerate to the Left
        1      Don't accelerate
        2      Accelerate to the Right
        Note: This does not affect the amount of velocity affected by the
        gravitational pull acting on the car.
    Reward:
         Reward of 0 is awarded if the agent reached the flag (position = 0.5)
         on top of the mountain.
         Reward of -1 is awarded if the position of the agent is less than 0.5.
    Starting State:
         The position of the car is assigned a uniform random value in
         [-0.6 , -0.4].
         The starting velocity of the car is always assigned to 0.
    Episode Termination:
         The car position is more than 0.5
         Episode length is greater than 200
    """

    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second': 30
    }

    actions_num = 3

    def __init__(self):
        self.viewer = None
        high = 100
        low = -high
        self.observation_space = 3
        self.action_space = [0,1,2]
        self.state = None

    def reset(self):
        self.state = self.np_random.uniform(low=-0.1, high=0.1, size=(4,))
        return self._get_ob()

    def step(self, a):
        
        state = []
        done = False
        reward = -1. if not done else 0.
        return (state, reward, done, {})

    def render(self, mode='human'):
        print('drawing window')


    def draw_window(board, score):

        # clear screen    
        pygame.draw.rect(WIN, BLACK, BORDER)

        # Draw score
        score_text = STANDARD_FONT.render("Score: " + str(score), 1, WHITE)
        WIN.blit(score_text, (10, 760))
        
        # Draw game board with cubes

        draw_board(board)

        pygame.display.update()