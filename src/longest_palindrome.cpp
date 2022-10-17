class Solution {
public:
    string longestPalindrome(string s) {
        
        string longestSubstring = 0;
        for (int i=1; i<s.size(); i++){
            stack<char> stk;
            string substring = s.substr(0,i);
            if ( (substring.size() % 2) == 0 ){
                
                cout << "Till here" << endl;
                for(int j=0; j <= (substring.size()/2)-1; j++){
                    stk.push(substring[j]);
                }
                cout << "Till here - 2 " << endl;
                for(int j=(substring.size()/2); j <= substring.size(); j++){
                    if (stk.top() == substring[j]){
                        stk.pop();
                    }
                }
                cout << "Till here - 3" << endl;
                
                if (stk.empty() == true && i > longestSubstring.size()){
                    longestSubstring = substring;
                }
            }
            else{
                
                cout << "Till here - 4" << endl;
                for(int j=0; j <= ((substring.size()-1)/2)-1; j++){
                    stk.push(substring[j]);
                }
                cout << "Till here - 5" << endl;
                
                for(int j=((substring.size()-1)/2)+1; j <= substring.size(); j++){
                    if (stk.top() == substring[j]){
                        stk.pop();
                    }
                }
                
                cout << "Till here - 6" << endl;
                if (stk.empty() == true && i > longestSubstring.size()){
                    longestSubstring = substring;
                }
                
            }
        
        }
        return longestSubstring;
    }
};
