class Solution {
public:
vector<int> spiralOrder(vector<vector<int>>& matrix) {
    int rows=matrix.size();
    int column=matrix[0].size();

    vector<int>temp;
    
    int top=0;
    int down=rows-1;
    int left=0;
    int right=column-1;
    int dir=0;
    
    while(top<=down && left<=right)
    {
        if(dir==0)
        {for(int i=left;i<=right;i++)
                temp.push_back(matrix[top][i]);
            top+=1;}
        
        else if(dir==1)
        {for(int i=top ;i<=down;i++)
                temp.push_back(matrix[i][right]);
                
        right-=1;
        }
        else if(dir==2)
        {   for(int i=right;i>=left;i--)
                temp.push_back(matrix[down][i]);
                
        down-=1;
        }
        else if(dir==3)
        {   for(int i=down;i>=top;i--)
                temp.push_back(matrix[i][left]);
        left+=1;
        }
        dir=(dir+1)%4;
    }
return temp;
}
};
