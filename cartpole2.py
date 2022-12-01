import gym
# 環境の生成 
env = gym.make('CartPole-v0',render_mode="human")
# 環境の初期か
observation = env.reset()
for t in range(1000):
    # 現在の状況を表示させる
    env.render()
    # サンプルの行動をさせる　返り値は左から台車および棒の状態、得られた報酬、ゲーム終了フラグ、詳細情報
    observation, reward, done, info,_ = env.step(env.action_space.sample())
    if done:
        print("Finished after {} timesteps".format(t+1))
        break
# 環境を閉じる
env.close()