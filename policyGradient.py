import numpy as np

## define hyper parameters
input_size = 2*100
hidden_size = 100
output_size = 1

num_trace = 100
trace_length = 100
max_iteration = 1000000

## mlp initialization
w1 = np.random.randn(hidden_size, input_size) / np.sqrt(input_size)
b1 = np.random.randn(hidden_size) / np.sqrt(hidden_size)
w2 = np.random.randn(hidden_size, output_size) / np.sqrt(hidden_size)
b2 = np.random.randn(output_size)

  
def mlp_forward(input):
  h1 = np.dot(w1, input) + b1
  h1[h1<0] = 0
  h2 = np.dot(w2, h2) + b2
  output = 1.0 / (1.0 + np.exp(-h2))
  return output

def sample_action(output):
  from random import choices
  population = [0, 1]
  weights = [output, 1-output]
  action = choices(population, weights)


def sample_trajectory(current_state, network, environment):
  
  return average_loss

def mlp_backprop(average_loss):
  
  
## policy gradient
iteration = 0
while iteration < max_iteration:
  loss = 0
  for n in range(num_trace):
    for t in range(trace_length):
      
      
  
  mlp_backprop(loss / num_trace)
  iteration+= 1
