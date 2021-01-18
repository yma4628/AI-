import numpy as np

#1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。
answer_one = np.arange(0,21,1)
print("答案一：",answer_one)

#2.呈上題，將以上數列取出偶數。
print(f'答案二：{answer_one[0::2]}')

#3.呈1題，將數列取出3的倍數。
print(f'答案三：{answer_one[3::3]}')