#-*- coding:utf-8 -*-
'''
机器人在一个无限大小的网格上行走，从点（0,0）处开始出发，面向北方。该机器人可以
接收以下三种类型的命令：
-2：向左转90度
-1：想右转90度
1<=x<=9:向前移动x个单位长度
在网格上有些格子被视为障碍物
第i个障碍物位于网格点（obstacles[i][0],obstacles[i][1]）
如果机器人试图走到障碍物上方，那么它将停留在障碍物的前一个网格方块上，但仍然可以继续
该线路的其他你分。
返回从原点到机器人的最大欧式距离的平方
'''
class Solution(object):
	def robotSim(self, commands, obstacles):
		dx = [0, 1, 0, -1]
		dy = [1, 0, -1, 0]
		x = y = di = 0
		obstacleSet = set(map(tuple, obstacles))
		ans = 0

		for cmd in commands:
			if cmd == -2:#left
				di = (di - 1) % 4
			elif cmd == -1:#right
				di = (di + 1) % 4
			else:
				for k in xrange(cmd):
					if (x+dx[di], y+dy[di]) not in obstacleSet:
						x += dx[di]
						y += dy[di]
						ans = max(ans, x*x +y*y)
		return ans


if __name__ == '__main__':
	a = Solution()
	print a.robotSim([4,-1,3],[])
				
