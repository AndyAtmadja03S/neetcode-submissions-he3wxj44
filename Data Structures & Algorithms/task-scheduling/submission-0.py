class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = sorted(Counter(tasks).values())
        maxf = count[-1]
        idle = (maxf - 1) * n

        for c in count[:-1]:
            idle -= min(maxf - 1, c)
        
        return max(0, idle) + len(tasks)