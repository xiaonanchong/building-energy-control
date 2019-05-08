import numpy as np

## define hyper parameters
input_size = 2*100
hidden_size = 100
output_size = 1

num_trace = 100
trace_length = 100
num_iteration = 1000000

## mlp initialization
w1 = np.random.randn(hidden_size, input_size) / np.sqrt(input_size)
b1 = np.random.randn(hidden_size) / np.sqrt(hidden_size)
w2 = np.random.randn(hidden_size, output_size) / np.sqrt(hidden_size)
b2 = np.random.randn(output_size)

def sample_trajectory(current_state, network, environment):
  
  return average_loss
  
def mlp_forward(input):
  
  return output

def mlp_backward(average_loss):
  
  
