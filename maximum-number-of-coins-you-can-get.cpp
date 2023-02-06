class Solution {
public:
    int maxCoins(vector<int>& piles) {
       sort(piles.begin(),piles.end());
int k = piles.size()/3;
int result = 0;
for(int i=k; i<piles.size(); i+=2){
result += piles[i];
}
return result;
    }
};
