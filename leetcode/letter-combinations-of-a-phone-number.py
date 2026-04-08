class Solution {
    List<String> answer = new ArrayList<>();
    Map<Character, String> map = new HashMap<>();

    void helper(String digits, int idx, StringBuilder sb) {
        if(idx == digits.length()){
            answer.add(new String(sb));
            return;
        }

        char ch = digits.charAt(idx);
        String letter = map.get(ch);

        for(int i = 0 ; i < letter.length() ; i++){
            sb.append(letter.charAt(i));
            helper(digits , idx+1 , sb);
            sb.deleteCharAt(sb.length() - 1);
        }
    }

    public List<String> letterCombinations(String digits) {
        map.put('2', "abc");
        map.put('3', "def");
        map.put('4', "ghi");
        map.put('5', "jkl");
        map.put('6', "mno");
        map.put('7', "pqrs");
        map.put('8', "tuv");
        map.put('9', "wxyz");

        StringBuilder sb = new StringBuilder();

        helper(digits, 0, sb);
        return answer;
    }
}