"""
    https://leetcode-cn.com/problems/sliding-window-maximum/
    https://leetcode-cn.com/problems/sliding-window-maximum/solution/hua-dong-chuang-kou-zui-da-zhi-by-leetco-ki6m/

"""
# 优先队列
def maxSlidingWindow(nums, k) :
    n = len(nums)
    # 注意 Python 默认的优先队列是小根堆
    q = [(-nums[i], i) for i in range(k)]
    heapq.heapify(q)
    
    # 加上负号恢复原值
    ans = [-q[0][0]]
    # 遍历后续数组值，每次将值压入堆，再检查堆中最大值是否在窗口内，若在窗口外则删除，然后将堆顶的值取出
    for i in range(k, n):
        heapq.heappush(q, (-nums[i], i))
        while q[0][1] <= i - k:
            heapq.heappop(q)
        ans.append(-q[0][0])

    return ans

#  单调队列
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        q = collections.deque()
        # q为一个单调队列（栈），每次有新元素加入前，总是保证队列前面的数值比它大
        # 他们的下标是单调递增，数值单调递增
        for i in range(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            
        # 初始化为第0个K大小窗口的最大值
        ans = [nums[q[0]]]
        for i in range(k, n):
            # 有新的元素加入，先弹出队列（栈）中所有比它小的值
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
            # 单调队列中idx为单调递增，此时前面的元素若超过窗口则弹出
            # 直到在当前窗口正常范围内
            while q[0] <= i - k:
                q.popleft()
            # 此时的q为窗口范围内的，下标递增，数值递减的单调队列
            ans.append(nums[q[0]])

        return ans