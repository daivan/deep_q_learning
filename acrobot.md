# DQN - Acrobot

# pre-prerequisite
The DQN expects you to pass in a state and a reward each time you make a move.
In this example we pass in the state via two images that are subtracted from one another.  
We use the reward from the poles directions. The upwards direction of both poles is the reward. The more upwards both poles are pointing. The better the reward.


# prerequisite
You can read about the environment here:  
https://github.com/openai/gym/blob/master/gym/envs/classic_control/acrobot.py

Important things are:

The state
```
**STATE:**
    The state consists of the sin() and cos() of the two rotational joint
    angles and the joint angular velocities :
    [cos(theta1) sin(theta1) cos(theta2) sin(theta2) thetaDot1 thetaDot2].
    For the first link, an angle of 0 corresponds to the link pointing downwards.
    The angle of the second link is relative to the angle of the first link.
    An angle of 0 corresponds to having the same angle between the two links.
    A state of [1, 0, 1, 0, ..., ...] means that both links point downwards.
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
In this example we get the reward from the `step()`
```
# line 48-49
state, reward, self.done, _ = self.env.step(action.item())
artificial_reward = np.float32(((state[0]*1.5)+state[2])*-1)
```
Here we see that we retrive the tuple from the `step()` method. However we are actually interested in the state variable, more precise the cos() of both poles.
I feel that the first pole (inner pole) should have higher weight and have it multiplied by `1.5` so that the DQN prioritises getting that upright instead of the second pole.
When pointing down its +1. We need to inverse it with *-1 so that the reward is correct.

This is what we pass in as the reward.