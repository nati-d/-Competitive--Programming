class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        p_arr = [0] * 1001
        N = len(p_arr)

        for passenger,frm,to in trips:
            p_arr[frm] += passenger
            p_arr[to] -= passenger
            

        sm = 0
        for i in range(N):
            sm += p_arr[i]
            p_arr[i] = sm
            if p_arr[i] > capacity:
                return False

        return True