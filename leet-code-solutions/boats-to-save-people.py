class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        N = len(people)
        l, r = 0, N - 1
        count = 0

        while l <= r:
            if people[l] + people[r] <= limit:
                l += 1

            r -= 1
            count += 1

        return count
