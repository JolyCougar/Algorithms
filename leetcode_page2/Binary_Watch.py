from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        if turnedOn >= 9:
            return []
        fin_lst = []
        for hour in range(12):
            for minute in range(60):
                if str(bin(hour)).count('1') + str(bin(minute)).count('1') == turnedOn:
                    fin_lst.append(f"{hour}:{minute:02d}")

        return fin_lst


# ---------------------------------------------------------------------------------------
# res = []
#
#
# def backtracking(leds, idx, lights_num):
#     if lights_num == turnedOn:
#         hour, minute = int(''.join(leds[:4]), 2), int(''.join(leds[4:]), 2)
#         if hour < 12 and minute < 60:
#             res.append('{}:{:02d}'.format(hour, minute))
#         return
#     for j in range(idx, 10):
#         leds[j] = '1'
#         backtracking(leds[:], j + 1, lights_num + 1)
#         leds[j] = '0'
#
#
# backtracking(['0'] * 10, 0, 0)
# return res

print(Solution().readBinaryWatch(1))
