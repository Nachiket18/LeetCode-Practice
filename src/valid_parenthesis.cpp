class Solution {
public:
    bool isValid(string s) {
     
        stack <char> stk;
        
        for(int i=0; i < s.size();i++){
           
            if (s[i] == '(' || s[i] == '{' || s[i] == '['){
                stk.push(s[i]);
            }
            else {
                if (stk.empty()){
                    return false;
                }
                switch(s[i]){
                    case '}':
                        if (stk.top() != '{'){
                            return false;
                        }
                        cout << "Here";
                        break;
                    case ']':
                        cout << stk.top() << endl;
                        if (stk.top() != '['){
                            return false;
                        }
                        
                        cout << "Here - 2";
                        break;
                    case ')':
                        if (stk.top() != '('){
                            return false;
                        }
                        cout << "Here -3";
                        break;
                }
                stk.pop();
            }
                
        
        }
        if (stk.empty()){
            return true;
        }
        else{
            return false;
        }
        return true;
        
//         for(int i=(s.size()/2); i< s.size();i++){
           
//             if (stk.top() == '(' && s[i] == ')'){
//                 cout << "here - 1";
//                 stk.pop();    
//             }
//             else if (stk.top() == '{' && s[i] == '}'){
//                 cout << "here - 2";
//                 stk.pop();    
//             }
//             else if (stk.top() == '[' && s[i] == ']'){
//                 cout << "here - 3";
//                 stk.pop();    
//             }
            
//             else{
//                 return false;
//             }
            
//         }
        return true;
      
    }
};
