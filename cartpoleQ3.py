import gym
import numpy as np

env = gym.make('CartPole-v0',render_mode="human")

goal_average_steps = 195
max_number_of_steps = 200
num_consecutive_iterations = 100
num_episodes = 2000
last_time_steps = np.zeros(num_consecutive_iterations)

# Qテーブル作成
q_table = np.random.uniform(low=-1, high=1, size=(4 ** 4, env.action_space.n))

def bins(clip_min, clip_max, num):
    return np.linspace(clip_min, clip_max, num + 1)[1:-1]

def digitize_state(observation):
    # 各値を4個の離散値に変換
    cart_pos, cart_v, pole_angle, pole_v= observation
    digitized = [np.digitize(cart_pos, bins=bins(-2.4, 2.4, 4)),
                 np.digitize(cart_v, bins=bins(-3.0, 3.0, 4)),
                 np.digitize(pole_angle, bins=bins(-0.5, 0.5, 4)),
                 np.digitize(pole_v, bins=bins(-2.0, 2.0, 4))]
    # 0~255に変換
    return sum([x * (4 ** i) for i, x in enumerate(digitized)])

def get_action(state, action, observation, reward):
    next_state = digitize_state(observation)
    next_action = np.argmax(q_table[next_state])

    # Qテーブルの更新
    alpha = 0.2
    gamma = 0.99
    q_table[state, action] = (1 - alpha) * q_table[state, action] +\
            alpha * (reward + gamma * q_table[next_state, next_action])

    return next_action, next_state

for episode in range(num_episodes):
    # 環境の初期化
    observation, _ = env.reset()

    state = digitize_state(observation)
    action = np.argmax(q_table[state])

    episode_reward = 0
    for t in range(max_number_of_steps):
        # CartPoleの描画
        env.render()
        #if env.viewer == None:
         #   env.render()
        
        # 行動の実行とフィードバックの取得
        observation, reward, done, info ,_= env.step(action)
        # 行動の選択
        action, state = get_action(state, action, observation, reward)
        episode_reward += reward

        if done:
            print('%d Episode finished after %d time steps / mean %f' % (episode, t + 1,
                last_time_steps.mean()))
            last_time_steps = np.hstack((last_time_steps[1:], [episode_reward]))
            break

    if (last_time_steps.mean() >= goal_average_steps): # 直近の100エピソードが195以上であれば成功
        print('Episode %d train agent successfuly!' % episode)
        break

