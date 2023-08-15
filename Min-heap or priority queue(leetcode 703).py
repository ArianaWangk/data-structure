class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # minHeap w/ K largest integers
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) 
        # heapify−将普通列表转换为堆。在结果堆中，最小的元素被推到索引位置0。但是其余的数据元素没有必要排序。heappush−该函数在不改变当前堆的情况下向堆中添加元素。
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
