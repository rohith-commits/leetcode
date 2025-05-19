class Solution {
    public boolean isPalindrome(int x) {
        String stringx = String.valueOf(x);
        
        for(int i=0; i<= stringx.length(); i++){
            int length_i = stringx.length() - i -1;
            if(length_i == 0){
                return true;
            }
            if(stringx.charAt(i) == stringx.charAt(length_i)){
                continue;
            }
            else{
                return false;
            }

        }
        return true;
    }
}