class MinStack {
public:
    stack <int> s1;
    stack <int> s2;
    MinStack() {
        
    }
    
    void push(int val) {
        if (s1.empty() || val<=getMin())
        {
            s2.push(val);
        }
        s1.push(val);
    }
    
    void pop() {
      
            if(!s1.empty() && s1.top()==getMin())
            {
              
                    s2.pop();

   
            }
        
        s1.pop();
        
    }
    
    int top() {
        return s1.top();
        
    }
    
    int getMin() {
        return s2.top();
        
    }
};
