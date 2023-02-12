class Solution {
public:
    int calculate(string s) {
        istringstream iss('+'+s+'+');
        int total = 0;
        int leftOperand = 0;
        int rightOperand = 0;
        char op;
        while(iss >> op){
            if(op == '+' || op == '-'){
                total += leftOperand;
                iss >> leftOperand;
                leftOperand *= (op == '+' ? 1 : -1);
            }else{
                iss >> rightOperand;
                if(op == '*') leftOperand *= rightOperand;
                else leftOperand /= rightOperand;
            }
        }
        return total;
    }
};
