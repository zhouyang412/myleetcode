"""
    https://leetcode-cn.com/problems/132-pattern/
    https://leetcode-cn.com/problems/132-pattern/solution/zhan-jie-fa-chao-xiang-xi-ti-jie-by-siyy/

"""
def find132pattern(nums):
    le = len(nums)
    if le<2: return False
    
    # 每个位置左边的最小值
    # 为非递增数组，后面的值都小于等于当前的位置的值
    mi = [nums[0]]
    for i in range(1, le):
        mi.append(min(nums[i], mi[-1]))
        
    stack = []
    # 从后往前遍历数组
    for i in range(le-1, -1, -1):
        if nums[i]>mi[i]:
            # 持续出栈，直到比当前mi[i]要大，即比mi[i]大的最小值
            # mi为一个非递增数组，m[i]>=m[i+1]，若此时的值比当前值小，那么也一定比mi[i-1]的值小，因为此时是从后往前遍历
            # 因此可以直接出栈，因为需要右侧值比左侧的大
            while stack and mi[i]>=stack[-1]:
                stack.pop()
            # 此时，mi中的值为num的左边的小于num的值
            # stack中的值为在num右边且大于num对应的mi中的值，当stack[-1]小于当前num[i]
            # 满足题目要求
            if stack and stack[-1]<nums[i]:
                return True
            
            # 如果栈顶的数大于num则已经结束，否则就是大于num的，此时可以直接入栈
            stack.append(nums[i])
    return False
