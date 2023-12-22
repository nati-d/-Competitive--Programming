class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            i.reverse()
        for i in image:
            for j in range(len(i)):
                if i[j] == 1:
                    i[j] = 0
                else:
                    i[j] = 1
        return image
