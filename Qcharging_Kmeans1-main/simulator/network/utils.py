import random
import pickle

from simulator.network.package import Package


def uniform_com_func(net):
    for node in net.node:
        if node.id in net.target and random.random() <= node.prob and node.is_active:
            package = Package(package_size=net.package_size)
            node.send(net, package)
            # print(package.path)
    return True


def to_string(net):
    min_energy = 10 ** 10
    min_node = -1
    for node in net.node:
        if node.energy < min_energy:
            min_energy = node.energy
            min_node = node
    min_node.print_node()


def count_package_function(net):
    count = 0
    for target_id in net.target:
        package = Package(is_energy_info=True)
        net.node[target_id].send(net, package)
        if package.path[-1] == -1:
            count += 1
    return count

def set_checkpoint(t=0, network=None, optimizer=None, dead_time=0):
    # exp_index = int(network.experiment.split('_')[1])
    exp_type = network.experiment.split('_')[0]
    nb_run = int(network.experiment.split('_')[1])
    checkpoint = {
        'time'              : t,
        'experiment_type'   : exp_type,
        # 'experiment_index'  : exp_index,
        'nb_run'            : nb_run,
        'network'           : network,
        'optimizer'         : optimizer,
        'dead_time'         : dead_time
    }
    with open('checkpoint/checkpoint_{}.pkl'.format(exp_type), 'wb') as f:
        pickle.dump(checkpoint, f)
    print("[Simulator] Simulation checkpoint set at {}s".format(t))

def generate_random_array(n, array):
  selected_elements = set()

  random_array = []
  for _ in range(n):
    random_element = random.randint(0, n - 1)

    while random_element in selected_elements:
      random_element = random.randint(0, n - 1)

    selected_elements.add(random_element)
    random_array.append(random_element)

  return random_array