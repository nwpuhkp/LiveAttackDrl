#!/usr/bin/env python
import ctypes, re, sys, binascii
import numpy as np

## Parse a line in /proc/$pid/maps. Return the boundaries of the chunk
## the read permission character.
"""
maps_line_range函数的作用是解析/proc/$pid/maps中的一行。
返回该行所表示的内存块的边界和读取权限。
具体来说，该函数使用正则表达式匹配行中的三个部分：起始地址、结束地址和读取权限。
然后将起始地址和结束地址转换为十进制整数，并将它们和读取权限一起返回。
"""
def maps_line_range(line):
    m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
    return [int(m.group(1), 16), int(m.group(2), 16), m.group(3)]

## Find memory wiht in a process memory mapped by a process
"""
locate_proc_mem函数的作用是在进程的内存映射中查找特定的字符串,并返回该字符串在内存中的地址。
具体来说,该函数接受两个参数:pid和patch_str。
其中,pid是进程的ID,patch_str是要查找的字符串。
该函数首先打开/proc/$pid/maps文件,解析其中的每一行,获取每个内存块的起始地址、结束地址和读取权限。
然后，该函数打开/proc/$pid/mem文件,读取每个可读的内存块,并在其中查找patch_str。
如果找到了patch_str,则将其在内存中的地址和patch_str在内存块中的偏移量存储在一个元组中,并将该元组添加到addresses列表中。
最后,该函数返回addresses列表。
"""
def locate_proc_mem(pid, patch_str):
    mem_list = []
    addresses = []
    pattern = re.compile(patch_str)
    maps_file = open("/proc/" + pid + "/maps", 'r')
    ranges = map(maps_line_range, maps_file.readlines())
    maps_file.close()
    ## Read the readable mapped ranges
    mem_file = open("/proc/" + pid + "/mem", 'rb', 0)
    for r in ranges:
        if r[2] == 'r':
            try:
                mem_file.seek(r[0])
                chunk = mem_file.read(r[1] - r[0])
                if pattern.search(bytearray(chunk)):
                    addresses.append((pattern.search(chunk), r[0]))
            except:
                continue
    mem_file.close()
    return addresses

"""
patch_proc_mem函数的作用是将target写入到进程pid的内存地址addr处。
具体来说,该函数首先打开/proc/$pid/mem文件,然后将文件指针移动到addr处,最后将target写入到该位置。
"""
def patch_proc_mem(pid, addr, target):
    mem_file = open("/proc/" + pid + "/mem", 'wb', 0)
    mem_file.seek(addr)
    mem_file.write(target)


if __name__ == "__main__":
    for pid in sys.argv[1:]:
        w1 = open("./PDF_weights/w1.bin", 'rb').read()
        w1_patched = open("./PDF_weights/w1_patched.bin", 'rb').read()


        found_1 = locate_proc_mem(pid, re.escape(w1))
        if len(found_1):
            print("Found addresses for w1")
            for first in found_1:
                patch_proc_mem(pid, first[0].start() + first[1], w1_patched)
        else:
            print("couldn't find weight")

        w2 = open("./PDF_weights/w2.bin", 'rb').read()
        w2_patched = open("./PDF_weights/w2_patched.bin", 'rb').read()


        found_2 = locate_proc_mem(pid, re.escape(w2))
        if len(found_2):
            print("Found addresses for w2")
            for first in found_2:
                patch_proc_mem(pid, first[0].start() + first[1], w2_patched)
        else:
            print("couldn't find weight")


        w3 = open("./PDF_weights/w3.bin", 'rb').read()
        w3_patched = open("./PDF_weights/w3_patched.bin", 'rb').read()


        found_3 = locate_proc_mem(pid, re.escape(w3))
        if len(found_3):
            print("Found addresses for w3")
            for first in found_3:
                patch_proc_mem(pid, first[0].start() + first[1], w3_patched)
        else:
            print("couldn't find weight")

        w4 = open("./PDF_weights/w4.bin", 'rb').read()
        w4_patched = open("./PDF_weights/w4_patched.bin", 'rb').read()


        found_4 = locate_proc_mem(pid, re.escape(w4))
        if len(found_4):
            print("Found addresses for w4")
            for first in found_4:
                patch_proc_mem(pid, first[0].start() + first[1], w4_patched)
        else:
            print("couldn't find weight")
