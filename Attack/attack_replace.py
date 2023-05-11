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


def replace_conv1_w():
    # 查找/寻址
    with open('./pickled_model/conv1.weight.pkl', 'rb') as f:
        conv1_w = pickle.load(f)
        f.close()
    conv1_w = conv1_w.numpy().tobytes()
    with open('./pickled_patched_model/conv1.weight.pkl', 'rb') as f:
        conv1_w_patched = pickle.load(f)
        f.close()
    conv1_w_patched = conv1_w_patched.numpy().tobytes()
    # 替换
    found_1 = locate_proc_mem(pid, re.escape(conv1_w))
    if len(found_1):
        print("Found addresses for conv1_w")
        for i in found_1:
            patch_proc_mem(pid, i[0].start() + i[1], conv1_w_patched)
            print("Successfully replaced conv1_w")
    else:
        print("couldn't find conv1_w")


def replace_conv2_w():
    with open('./pickled_model/conv2.weight.pkl', 'rb') as f:
        conv2_w = pickle.load(f)
        f.close()
    conv2_w = conv2_w.numpy().tobytes()
    with open('./pickled_patched_model/conv2.weight.pkl', 'rb') as f:
        conv2_w_patched = pickle.load(f)
        f.close()
    conv2_w_patched = conv2_w_patched.numpy().tobytes()
    found_2 = locate_proc_mem(pid, re.escape(conv2_w))
    if len(found_2):
        print("Found addresses for conv2_w")
        for i in found_2:
            patch_proc_mem(pid, i[0].start() + i[1], conv2_w_patched)
            print("Successfully replaced conv2_w")
    else:
        print("couldn't find conv2_w")


def replace_conv3_w():
    with open('./pickled_model/conv3.weight.pkl', 'rb') as f:
        conv3_w = pickle.load(f)
        f.close()
    conv3_w = conv3_w.numpy().tobytes()
    with open('./pickled_patched_model/conv3.weight.pkl', 'rb') as f:
        conv3_w_patched = pickle.load(f)
        f.close()
    conv3_w_patched = conv3_w_patched.numpy().tobytes()

    found_3 = locate_proc_mem(pid, re.escape(conv3_w))
    if len(found_3):
        print("Found addresses for conv3_w")
        for i in found_3:
            patch_proc_mem(pid, i[0].start() + i[1], conv3_w_patched)
            print("Successfully replaced conv3_w")
    else:
        print("couldn't find conv3_w")


def replace_fc4_w():
    with open('./pickled_model/fc4.weight.pkl', 'rb') as f:
        fc_4_w = pickle.load(f)
        f.close()
    fc_4_w = fc_4_w.numpy().tobytes()
    with open('./pickled_patched_model/fc4.weight.pkl', 'rb') as f:
        fc_4_w_patched = pickle.load(f)
        f.close()
    fc_4_w_patched = fc_4_w_patched.numpy().tobytes()

    found_4 = locate_proc_mem(pid, re.escape(fc_4_w))
    if len(found_4):
        print("Found addresses for fc_4_w")
        for i in found_4:
            patch_proc_mem(pid, i[0].start() + i[1], fc_4_w_patched)
            print("Successfully replaced fc_4_w")
    else:
        print("couldn't find fc_4_w")


def replace_head5_w():
    with open('./pickled_model/head.weight.pkl', 'rb') as f:
        head_w = pickle.load(f)
        f.close()
    head_w = head_w.numpy().tobytes()
    with open('./pickled_patched_model/head.weight.pkl', 'rb') as f:
        head_w_patched = pickle.load(f)
        f.close()
    head_w_patched = head_w_patched.numpy().tobytes()

    found_5 = locate_proc_mem(pid, re.escape(head_w))
    if len(found_5):
        print("Found addresses for head_w")
        for first in found_5:
            patch_proc_mem(pid, first[0].start() + first[1], head_w_patched)
            print("Successfully replaced head_w")
    else:
        print("couldn't find head_w")


def replace_head5_b():
    with open('./pickled_model/head.bias.pkl', 'rb') as f:
        head_b = pickle.load(f)
        f.close()
    head_b = head_b.numpy().tobytes()
    with open('./pickled_patched_model/head.bias.pkl', 'rb') as f:
        head_b_patched = pickle.load(f)
        f.close()
    head_b_patched = head_b_patched.numpy().tobytes()

    found_5_b = locate_proc_mem(pid, re.escape(head_b))
    if len(found_5_b):
        print("Found addresses for head_b")
        for first in found_5_b:
            patch_proc_mem(pid, first[0].start() + first[1], head_b_patched)
            print("Successfully replaced head_b")
    else:
        print("couldn't find head_b")


def replace_neurons(model_name, neuron_name):
    with open('./pickled_model/' + neuron_name + '.pkl', 'rb') as f:
        neurons = pickle.load(f)
        f.close()
    neurons = neurons.numpy().tobytes()
    with open('./' + model_name + '_pickled_patched_model/' + neuron_name + '.pkl', 'rb') as f:
        neurons_patched = pickle.load(f)
        f.close()
    neurons_patched = neurons_patched.numpy().tobytes()

    found = locate_proc_mem(pid, re.escape(neurons))
    if len(found):
        print("Found addresses for " + neuron_name)
        for first in found:
            patch_proc_mem(pid, first[0].start() + first[1], neurons_patched)
            print("Successfully replaced " + neuron_name)
    else:
        print("couldn't find " + neuron_name)


if __name__ == "__main__":
    replace_model = "last_layer"
    attack_model = "frozen"
    frozen_attack_neurons_list = ["head.weight", "head.bias"]
    all_attack_neurons_list = ["conv1.weight", "conv1.bias", "conv2.weight", "conv2.bias", "conv3.weight", "conv3.bias",
                               "fc4.weight", "fc4.bias", "head.weight", "head.bias"]
    for pid in sys.argv[1:]:
        if replace_model == "all":
            for neurons_name in all_attack_neurons_list:
                replace_neurons(attack_model, neurons_name)
        elif replace_model == "last_layer":
            for neurons_name in frozen_attack_neurons_list:
                replace_neurons(attack_model, neurons_name)
        else:
            print("Invalid replace model")
            exit(1)
