import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--width', type=int, help='屏幕宽度',default=3840)
parser.add_argument('--height', type=int, help='屏幕高度',default=2160)
parser.add_argument('--mode', type=str, help='显示模式 全屏 无边框 窗口',default="boardless")
parser.add_argument('--scale', type=int, help='系统缩放倍率',default="2")
parser.add_argument('--times', type=int, help='抽奖次数',default=min(165,9999//30))
targetsArray=[
    ["牵绊特","效异特"],
    ["牵绊特","效异大"],
    ["正面特","效异特"],
    ["正面特", "效异大"]
]
args = parser.parse_args()
