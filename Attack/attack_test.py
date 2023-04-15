import os
import ctypes
import struct

# 跟踪pid为1234的进程
pid = 5283
ctypes.CDLL("libc.so.6").ptrace(16, pid, 0, 0)

# 打开maps文件和mem文件
maps_file = open(f"/proc/{pid}/maps", "r")
mem_file = open(f"/proc/{pid}/mem", "rb", 0)

# 读取本地的A文件
local_file = open("/home/huangkepu/LiveAttackDrl/PongDqn/cpu_model/DQN_Pong_episode1480_cpu_model.pth", "rb")
local_data = local_file.read()

# 遍历maps文件中的每一行
for line in maps_file.readlines():
    # 解析每一行中的地址范围、权限、偏移量、设备号、索引节点号和文件名
    if len(line.split(maxsplit=6)) == 6:
        address, perms, offset, dev, inode, pathname = line.split(maxsplit=6)
    else:
        address, perms, offset, dev, inode = line.split(maxsplit=6)
        # print(address)
    # print(address)
    if len(address) == 17:
        start_address = address[0:8]
        end_address = address[9:17]
    else:
        start_address = address[0:12]
        end_address = address[13:15]
    # print(start_address)
    # print(end_address)
    start_address = int(start_address, 16)
    end_address = int(end_address, 16)
    perms = perms[0:4]
    offset = int(offset, 16)
    dev = dev.split(":")
    dev_major = int(dev[0], 16)
    dev_minor = int(dev[1], 16)
    inode = int(inode)
    pathname = pathname.strip()

    # 如果文件名是A文件，并且权限是可读可执行
    if pathname == "/home/huangkepu/LiveAttackDrl/PongDqn/cpu_model/DQN_Pong_episode1480_cpu_model.pth":
        # 定位到映射地址的起始位置
        mem_file.seek(start_address)
        # 读取映射地址范围内的数据
        data = mem_file.read(end_address - start_address)
        # 在数据中查找本地文件的内容
        index = data.find(local_data)
        # 如果找到了匹配，打印匹配的内存地址
        if index != -1:
            print(f"Found match at {hex(start_address + index)}")
            break
    else:
        print("no found")

# 关闭文件
maps_file.close()
mem_file.close()
local_file.close()