from citylearn.citylearn import CityLearnEnv
from citylearn.agents.rbc import BasicRBC as RBCAgent

dataset_name = 'citylearn_challenge_2022_phase_all'
env = CityLearnEnv(dataset_name, central_agent=True)
model = RBCAgent(env)
model.learn(episodes=1)

# print cost functions at the end of episode
for n, nd in env.evaluate().groupby('name'):
    nd = nd.pivot(index='name', columns='cost_function', values='value').round(3)
    print(n, ':', nd.to_dict('records'))