import gym
#import jellygame as testar
from gym_jelly import JellyEnv
from JellyEnvironment import JellyEnvironment

CartPole = gym.make('CartPole-v0').unwrapped
CartPole.reset()

print(CartPole.action_space)

Acrobot = gym.make('Acrobot-v1').unwrapped
Acrobot.reset()

print(Acrobot.action_space)

MountainCar = gym.make('MountainCar-v0').unwrapped
MountainCar.reset()


print(MountainCar.action_space)


em = JellyEnvironment()
actions = em.num_actions_available()
width = em.num_actions_available()
height = em.num_actions_available()
print(actions)

