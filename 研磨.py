#!/usr/bin/env python3
import sys

人话 = "没法研磨：请给出一个不小于零的整数度数\n"

def 是非负整数(文本):
    if not 文本:
        return False
    for 字 in 文本:
        if 字 < "0" or 字 > "9":
            return False
    return True

def 换算(度数):
    if 度数 > 0 and 度数 % 360 == 0:
        圈 = 度数 // 360 - 1
    else:
        圈 = 度数 // 360
    if 圈 <= 0:
        档 = "淡"
    elif 圈 <= 2:
        档 = "中"
    else:
        档 = "浓"
    return 圈, 档

def 主程序(参数):
    if len(参数) != 1 or not 是非负整数(参数[0]) or 参数[0] == "缺":
        sys.stderr.write(人话)
        return 2
    圈, 档 = 换算(int(参数[0]))
    sys.stdout.write("%d圈\n%s\n" % (圈, 档))
    return 0

if __name__ == "__main__":
    raise SystemExit(主程序(sys.argv[1:]))
