from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.accu = [0]
        for num in nums:
            self.accu.append(self.accu[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.accu[right + 1] - self.accu[left]
