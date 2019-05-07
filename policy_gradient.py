import numpy as np
import _pickle as pickle
import gym

H = 200 # hidden layer
batch_size = 10 # num of episodes
learning_rate = 1e-4
gamma = 0.99 # dicount factor
decay_rate = 0.99 # ?
resume = False # ?
render = False # ?

D = 2*100
if resume:
  model = pickle.load(open('save.p'), 'rb')
else:
  model = {}
  model['w1'] = np.random.randn(H, D) / np.sqrt(D)
  model['w2'] = np.random.randn(H) / np.sqrt(H) 

grad_buffer = {k: np.zeros_like(v) for k,v in model.items()}
rmsprop_cache = {k: np.zeros_like(v) for k,v in model.items()}

def sigmoid(x):
  return 1.0 / (1.0 + np.exp(-x))

def discount_rewards(r):
  
