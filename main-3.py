# coding=utf-8
# import library

import gym

# creating environment
env = gym.make('MountainCar-v0')

# welcoming the user
print("\n\n\t ***The Little Cart that Couldn't***")

# Let the user know what this is about
print("MountainCar-v0 is a cart that is positioned between two mountains.")
print(" The cart cannot make it up the mountain on the right, so it is forced to swing back and forth to get speed.")
print(" A reward of 0 is given if the cart reaches the flag, position 0.5, at the top of the mountain.")
print(" A reward of -1 is given if the position of the cart is anything less than position 0.5.")


# user determines how many times they wish to run.
number_of_steps = input("\n\nHow many times would you like to run the program?")
# run X number of times
for i_episode in range(int(number_of_steps)):
    # clear environment each run
    observation = env.reset()
    # each timestep, the agent (the cart), chooses an action and the environment returns the observation at the end
    for t in range(20):
        # render new environment on each run
        env.render()
        # display GUI for user
        print(observation)
        # sample an action
        action = env.action_space.sample()
        # populate Reinforcement learning information
        # observation, reward, done, info
        # observation is the environment-specific object
        # reward is the amount of reward received from the environment
        # done is when the environment is terminated
        observation, reward, done, info = env.step(action)
        # check if done flag is flipped (above us)
        if done:
            # summarize info for user
            print("\n\nEpisode Finished after {} timesteps".format(t + 1))
            # exit loop
            break
# start program exit information for the user
input("\n\n\t***EXAMINE GUI then PRESS ENTER WHEN FINISHED***")
env.close()
