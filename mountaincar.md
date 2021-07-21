# DQN - Mountain Car

# pre-prerequisite
The DQN expects you to pass in a state and a reward each time you make a move.
In this example we pass in the state via two images that are subtracted from one another.  
We use the reward from the Car Velocity. The higher the velocity, the higher the reward. So this DQN is trying to maximize the velocity of the car, not actually trying to reach the flag at the top.  
I figured, if it strives for the highest velocity, it will eventually reach the flag.


# prerequisite
You can read about the environment here:  
https://github.com/openai/gym/blob/master/gym/envs/classic_control/mountain_car.py

Important things are:

The observation
```
Observation:
    Type: Box(2)
    Num    Observation               Min            Max
    0      Car Position              -1.2           0.6
    1      Car Velocity              -0.07          0.07
```

And the actions
```
Actions:
    Type: Discrete(3)
    Num    Action
    0      Accelerate to the Left
    1      Don't accelerate
    2      Accelerate to the Right
    Note: This does not affect the amount of velocity affected by the
    gravitational pull acting on the car.
```

# The State
To get the state we first render the enviroment, however everytime we render it we save it as a matrix.
```
# line 76
screen = self.render('rgb_array').transpose((2, 0, 1)) # PyTorch expects CHW
```
The screen is now an `[[225,225,255],[225,225,255]...]` to reprecent the image.
We take this image and the previous one and subtract them to get the difference.
This way we will actually capture movements in one single image.

Then we pass in the processed image as the state.

# The Reward
In this example its easy to get the reward as we can get in from the `step()`
```
# line 48-49
state, reward, self.done, _ = self.env.step(action.item())
artificial_reward = np.float32(abs(state[1]))
```
Here we see that we retrive the tuple from the `step()` method. However we are actually interested in the state variable, more precise the velocity. We dont care if its going fast backward sor fast forward, hence the `abs()`.

This is what we pass in as the reward.