# -*- coding: UTF-8 -*-
import ctypes
import pickle
import re
import sys

from realtime_attack.mem_search import locate_proc_mem, patch_proc_mem

# main
c_ptrace = ctypes.CDLL("libc.so.6").ptrace
c_pid_t = ctypes.c_int32  # This assumes pid_t is int32_t
c_ptrace.argtypes = [ctypes.c_int, c_pid_t, ctypes.c_void_p, ctypes.c_void_p]


def replace_neurons(model_name, neuron_name):
    with open('./pickled_model/' + neuron_name + '.pkl', 'rb') as f:
        neurons = pickle.load(f)
        f.close()
    neurons = neurons.numpy().tobytes()
    with open('./' + model_name + '_pickled_patched_model/' + neuron_name + '.pkl', 'rb') as f:
        neurons_patched = pickle.load(f)
        f.close()
    neurons_patched = neurons_patched.numpy().tobytes()

    found = locate_proc_mem(pid, re.escape(neurons_patched))
    if len(found):
        print("Found addresses for " + neuron_name + "_patched")
        for first in found:
            patch_proc_mem(pid, first[0].start() + first[1], neurons)
            print("Successfully recovered " + neuron_name)
    else:
        print("couldn't find " + neuron_name + "_patched")


if __name__ == "__main__":
    recover_model = "last_layer"
    attack_model = "frozen"
    frozen_attack_neurons_list = ["head.weight", "head.bias"]
    all_attack_neurons_list = ["conv1.weight", "conv1.bias", "conv2.weight", "conv2.bias", "conv3.weight", "conv3.bias",
                               "fc4.weight", "fc4.bias", "head.weight", "head.bias"]
    for pid in sys.argv[1:]:
        if recover_model == "all":
            for neurons_name in all_attack_neurons_list:
                replace_neurons(attack_model, neurons_name)
        elif recover_model == "last_layer":
            for neurons_name in frozen_attack_neurons_list:
                replace_neurons(attack_model, neurons_name)
        else:
            print("Invalid replace model")
            exit(1)
