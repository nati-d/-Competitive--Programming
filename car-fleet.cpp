class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        
        int n = position.size();
        

        
        vector<pair<int, int>> arr(n);
        
        for(int i = 0; i < n; i++)
        {
            arr[i] = {position[i], speed[i]};
        }
        
      
        
        sort(arr.begin(), arr.end());
        
        int count = 1;
        
        double ptime = (double) (target - arr[n - 1].first) / arr[n - 1].second;
   
        
        for(int i = n - 2; i >= 0; i--)
        {
            double ctime = (double) (target - arr[i].first) / arr[i].second;
            
            if(ctime > ptime)
            {
                count++;
                
                ptime = ctime;
            }
        }
        
        return count;
    }
};
