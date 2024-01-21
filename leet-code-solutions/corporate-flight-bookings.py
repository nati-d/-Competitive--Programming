class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        p_arr = [0] * n
        sm = 0
        for first,last,seat in bookings:
            p_arr[first-1] += seat
            if last < n:
                p_arr[last] -= seat
        

        for i in range(n):
            sm+=p_arr[i]
            p_arr[i] = sm
        return p_arr
        