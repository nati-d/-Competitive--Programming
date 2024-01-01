#include <vector>
#include <algorithm>

class Solution {
public:
    int maxCoins(vector<int>& piles) {
        sort(piles.begin(), piles.end());

        int l=0;
        int r=piles.size()-2;
        int sum=0;

        while(l<=r){
            sum+=piles[r];
            r-=2;
            l++;
        }
return sum;
    }
};
