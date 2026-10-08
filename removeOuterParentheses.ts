// Problem Link: https://leetcode.com/problems/remove-outermost-parentheses/description/

function removeOuterParentheses(s:  string): string {
  if (s.length % 2 !== 0) return "";
  
  let accumulator = "";
  let balance = 0;

  for (let i = 0; i < s.length; i++) {
    const bracket = s[i];
    const isOpeningBracket = bracket === '(';
  
    if (isOpeningBracket) {
      balance++; 
      if (balance >  1) {
        accumulator += '(';
      }
    } else {
      balance--;
      if (balance > 0) {
        accumulator += ')';
      }
    }
  }

  return accumulator;
};
