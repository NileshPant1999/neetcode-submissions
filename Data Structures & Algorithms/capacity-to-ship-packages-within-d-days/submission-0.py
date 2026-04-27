class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        min_bound = max(weights)
        max_bound = sum(weights)
        ans = max_bound

        def canCap(capacity):
            ship, cap = 1, capacity

            for weight in weights:
                if cap - weight < 0:
                    ship+=1
                    if ship > days:
                        return False
                    cap = capacity

                cap -= weight
            return True

        while min_bound <= max_bound:
            mid = (min_bound + max_bound) // 2
            if canCap(mid):
                ans = min(ans, mid)
                max_bound = mid - 1
            else:
                min_bound = mid + 1

        return ans