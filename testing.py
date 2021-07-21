import gym

CartPole = gym.make('CartPole-v0').unwrapped
CartPole.reset()

print(CartPole.action_space)

Acrobot = gym.make('Acrobot-v1').unwrapped
Acrobot.reset()

print(Acrobot.action_space)

MountainCar = gym.make('MountainCar-v0').unwrapped
MountainCar.reset()
state, reward, done, _ = MountainCar.step(0)

print(MountainCar.action_space)
bajs = MountainCar.observation_space
print(state)
