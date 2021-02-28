'''
    https://leetcode-cn.com/problems/largest-rectangle-in-histogram/
    1.暴力:
        1.for i in (0, n-2):
            for j in (i+1, n-1):
                min(i, j)
                update max-area
        2. for i in (0, n-1):
               找到左边边界和右边界即第一个比他小的柱子
               update max-area = height[i] * (right - left)
        
                
    2.stack:
        

'''
# 维护一个排序的栈，栈底为-1.遍历时，发现当前值比栈的-1位置小则表明找到栈现有所有数值的右边界
# 此时将栈里的数值弹出计算面积
def largestRectangleArea(heights):
    stack = []
    # 在迭代的过程中，-1始终小于heights中的正常值，栈中始终有一个0值。
    # 如果没有最后的哨兵，导致栈无法被清空
    heights = [0] + heights + [0]
    res = 0
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            tmp = stack.pop()
            # 此时stack[-1]为tmp的左边界
            res = max(res, (i - stack[-1] - 1) * heights[tmp])
        stack.append(i)
    return res