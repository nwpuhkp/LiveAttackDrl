import ctypes, re, sys, binascii
import numpy as np

# Parse a line in /proc/$pid/maps. Return the boundaries of the chunk
# the read permission character.

"""
maps_line_range函数的作用是解析/proc/$pid/maps中的一行。
返回该行所表示的内存块的边界和读取权限。
具体来说，该函数使用正则表达式匹配行中的三个部分：起始地址、结束地址和读取权限。
然后将起始地址和结束地址转换为十进制整数，并将它们和读取权限一起返回。
"""


def maps_line_range(line):
    m = re.match(r'([0-9A-Fa-f]+)-([0-9A-Fa-f]+) ([-r])', line)
    return [int(m.group(1), 16), int(m.group(2), 16), m.group(3)]


# Find memory with in a process memory mapped by a process
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
    # Read the readable mapped ranges
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


# 主函数
if __name__ == '__main__':
    # pid由用户输入
    pid = sys.argv[1]
    # 被查找的字符串由用户输入
    # patch_str = sys.argv[2]
    patch_str = open("/home/huangkepu/LiveAttackDrl/PongDqn/cpu_model/DQN_Pong_episode1480_cpu_model.pth", 'rb').read()
    # 将字符串转换为字节数组
    # patch_str = patch_str.encode('utf-8')
    # 查找字符串patch_str在内存中的位置
    addresses = locate_proc_mem(pid, re.escape(patch_str))
    # 如果找到了字符串patch_str
    if addresses:
        # 输出恭喜信息
        print("Found !")
    else:
        # 输出未找到信息
        print("Not found")
