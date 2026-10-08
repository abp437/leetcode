// Problem Link: https://leetcode.com/problems/valid-parentheses/description/

function isValid(s: string): boolean {
  if (s.length % 2 === 1) return false;

  const bracketStack: string[] = [];
  const bracketsMap = new Map<string, string>([
    [")", "("],
    ["}", "{"],
    ["]", "["],
  ]);

  for (const char of s) {
    if (char === "(" || char === "{" || char === "[") {
      bracketStack.push(char);
    } else if (
      bracketStack[bracketStack.length - 1] === bracketsMap.get(char)
    ) {
      bracketStack.pop();
    } else {
      return false;
    }
  }

  return bracketStack.length === 0;
}
