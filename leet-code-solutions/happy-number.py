class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(num):
            return sum(int(digit) ** 2 for digit in str(num))

        seen_numbers = set()

        while n != 1 and n not in seen_numbers:
            seen_numbers.add(n)
            n = get_next(n)

        return n == 1

        

