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

def advantage(r):
  """ take 1D float array of rewards in samples trajectory and compute the advantage """
  
def policy_forward(x):
  h = np.dot(model['w1'],x)
  h[h<0] = 0 # ReLU
  logp = np.dot(model['w2'],h)
  p = sigmoid(logp)
  return p, h
  
