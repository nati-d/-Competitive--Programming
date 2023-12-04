class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        minn=min(start, destination)
        maxx=max(start, destination)
        sum1=sum(distance[minn:maxx])
        sum2=sum(distance[:minn])+sum(distance[maxx:])
        return min(sum1,sum2)












        if destination == len(distance)-1:
            return min(sum(distance[0:destination]), distance[destination])
        else:
            return min(sum(distance[0:destination]), sum(distance[destination: -1]))