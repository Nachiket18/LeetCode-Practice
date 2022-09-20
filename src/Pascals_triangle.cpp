class Solution {
public:
    
    vector<vector<int>> p_triangle;
    vector<vector<int>> generate(int numRows) {
    
        if (numRows == 2) {
              
            if (p_triangle.size() < 2) {
                vector<int> tmp = {1};
                vector<int> tmp_2 = {1,1};
                p_triangle.push_back(tmp);
                p_triangle.push_back(tmp_2);
            
                
                return p_triangle;    
            }
            else {
                return p_triangle;
            }
            
        }
        else {
            
            
            
            if (p_triangle.size() < (numRows-1) ) {
                p_triangle = generate((numRows-1));
            }
            
            vector<int> prev = p_triangle[numRows-2];
            vector<int> tmp = {1};
                  
            for (int i=0; i < (prev.size()-1); i++) {
                
                cout << "Prev-data" << prev[i] << prev[i+1] << "\n";
                tmp.push_back((prev[i]+prev[i+1]));
            }
            tmp.push_back(1);
            p_triangle.push_back(tmp);
        
        }
        return p_triangle;
        
    }
};
