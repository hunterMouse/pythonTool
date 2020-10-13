import zlib
import requests

def str_zlib():

    req = requests.get("assets/config/layares.dat")
    message = req.text
    compressed = str.encode(message)# 采用爬虫的结果作为输入数据
    #compressed = zlib.compress(bytes_message, zlib.Z_BEST_COMPRESSION)
    decompressed = zlib.decompress(compressed)      # str、repr的区别
    print("original string:", len(message))
    print("original bytes:",  len(bytes_message))
    print("compressed:",  len(compressed))
    print("decompressed:",  len(decompressed))
    print("decompressed:", decompressed)




