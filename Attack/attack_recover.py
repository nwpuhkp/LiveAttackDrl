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

if __name__ == "__main__":
    for pid in sys.argv[1:]:
        # 查找/寻址
        with open('./pickled_model/conv1.weight.pkl', 'rb') as f:
            conv1_w = pickle.load(f)
            f.close()
        conv1_w = conv1_w.numpy().tobytes()
        with open('./pickled_patched_model/conv1.weight.pkl', 'rb') as f:
            conv1_w_patched = pickle.load(f)
            f.close()
        conv1_w_patched = conv1_w_patched.numpy().tobytes()
        # 原始处理（已弃用）
        # conv1_w = open("./sliced_model/conv1.weight.bin", 'rb').read()
        # conv1_w_patched = open("./sliced_patched_model/conv1.weight.bin", 'rb').read()

        # 复原
        found_1 = locate_proc_mem(pid, re.escape(conv1_w_patched))
        if len(found_1):
            print("Found addresses for conv1_w_patched")
            for first in found_1:
                patch_proc_mem(pid, first[0].start() + first[1], conv1_w)
                print("Successfully recovered conv1_w")
        else:
            print("couldn't find conv1_w_patched")

        with open('./pickled_model/conv2.weight.pkl', 'rb') as f:
            conv2_w = pickle.load(f)
            f.close()
        conv2_w = conv2_w.numpy().tobytes()
        with open('./pickled_patched_model/conv2.weight.pkl', 'rb') as f:
            conv2_w_patched = pickle.load(f)
            f.close()
        conv2_w_patched = conv2_w_patched.numpy().tobytes()

        found_2 = locate_proc_mem(pid, re.escape(conv2_w_patched))
        if len(found_2):
            print("Found addresses for conv2_w_patched")
            for first in found_2:
                patch_proc_mem(pid, first[0].start() + first[1], conv2_w)
                print("Successfully recovered conv2_w")
        else:
            print("couldn't find conv2_w_patched")

        with open('./pickled_model/conv3.weight.pkl', 'rb') as f:
            conv3_w = pickle.load(f)
            f.close()
        conv3_w = conv3_w.numpy().tobytes()
        with open('./pickled_patched_model/conv3.weight.pkl', 'rb') as f:
            conv3_w_patched = pickle.load(f)
            f.close()
        conv3_w_patched = conv3_w_patched.numpy().tobytes()

        found_3 = locate_proc_mem(pid, re.escape(conv3_w_patched))
        if len(found_3):
            print("Found addresses for conv3_w_patched")
            for first in found_3:
                patch_proc_mem(pid, first[0].start() + first[1], conv3_w)
                print("Successfully recovered conv3_w")
        else:
            print("couldn't find conv3_w_patched")

        with open('./pickled_model/fc4.weight.pkl', 'rb') as f:
            fc_4_w = pickle.load(f)
            f.close()
        fc_4_w = fc_4_w.numpy().tobytes()
        with open('./pickled_patched_model/fc4.weight.pkl', 'rb') as f:
            fc_4_w_patched = pickle.load(f)
            f.close()
        fc_4_w_patched = fc_4_w_patched.numpy().tobytes()

        found_4 = locate_proc_mem(pid, re.escape(fc_4_w_patched))
        if len(found_4):
            print("Found addresses for fc_4_w_patched")
            for first in found_4:
                patch_proc_mem(pid, first[0].start() + first[1], fc_4_w)
                print("Successfully recovered fc_4_w")
        else:
            print("couldn't find fc_4_w_patched")

        with open('./pickled_model/head.weight.pkl', 'rb') as f:
            head_w = pickle.load(f)
            f.close()
        head_w = head_w.numpy().tobytes()
        with open('./pickled_patched_model/head.weight.pkl', 'rb') as f:
            head_w_patched = pickle.load(f)
            f.close()
        head_w_patched = head_w_patched.numpy().tobytes()

        found_5 = locate_proc_mem(pid, re.escape(head_w_patched))
        if len(found_5):
            print("Found addresses for head_w_patched")
            for first in found_5:
                patch_proc_mem(pid, first[0].start() + first[1], head_w)
                print("Successfully recovered head_w")
        else:
            print("couldn't find head_w_patched")
