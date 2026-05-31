#!/usr/bin/python3
# -*- coding:utf-8 -*-

from manor import data_process, network_util

print(data_process.random_numeric_password(6))
def f(x):
    """待测试函数
    """
    y = x**3 + 2*x**2 + 6*x + 3
    return y

interval = (-2, 9)
zero_value = data_process.get_function_zero(f, interval, 0.00001)
print(zero_value)
if zero_value is not None:
    print(f(zero_value))


result = network_util.get_remotehost_ip("www.zengzhiying.net")
if result != "":
    print(result)


msg = b"this is test hahahaha"
bin_str = data_process.bytes2binstr(msg)

print(bin_str)

str1 = data_process.binstr2bytes(bin_str)
print(str1)
