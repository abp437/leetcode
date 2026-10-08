// Problem Link: https://leetcode.com/problems/palindrome-number/

// Implemented using Reverse matching and some clever math, could have also been implemented using Two Pointers
function isPalindrome(x: number): boolean {
  if (x < 0) return false;

  const original = x;
  let reversed = 0;
  let remainder = 0;

  while(x > 0) {
    remainder = x % 10;
    reversed = (reversed * 10) + remainder;
    x = Math.floor(x / 10);
  }

  return original === reversed;
}
