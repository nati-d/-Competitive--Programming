class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        N = len(cardPoints)
        window_sum = sum(cardPoints[:N-k])
        total_sum = sum(cardPoints)
        current_sum = total_sum - window_sum

        max_score = max(0, current_sum)
        l = 0

        for r in range(N - k, N):
            current_sum += cardPoints[l] - cardPoints[r]
            max_score = max(max_score, current_sum)
            l+=1

        return max_score