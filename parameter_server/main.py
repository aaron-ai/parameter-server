import ray
from parameter_server import ParameterServer

if __name__ == "__main__":
    ray.init()
    ps = ParameterServer.remote(10)
    params_id = ps.get_params.remote()
    print(params_id)
    print(ray.get(params_id))