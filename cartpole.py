import gym

#env = gym.make('CartPole-v0',render_mode="rgb_array")    # Cartpole定義
env = gym.make('CartPole-v0',render_mode="human")
env.reset()    # Cartpoleの状態初期化

for i in range(100):
    env.render()    # Cartpoleのアニメーション
    observation, reward, done, info ,_ = env.step(env.action_space.sample())  # カートを動かし、結果を返す
    print("Step:",i,done,"Reward:",reward,"Obs:",observation)

env.close()