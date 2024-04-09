import numpy as np
import ray

@ray.remote
class ParameterServer(object):
  def __init__(self, dim):
    # params 可以是一个将键映射到数组的字典
    self.params = np.zeros(dim) 
  def get_params(self):
    return self.params    
  def update_params(self, grad):
    self.params += grad