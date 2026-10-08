// Problem Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

// Straight forward JS & most optimal solution
function strStr(haystack: string, needle: string): number {
  return haystack.indexOf(needle);
}

// Naive nested loop solution
function strStr(haystack: string, needle: string): number {
  if (haystack.length < needle.length) return -1;

  for (let i = 0; i < haystack.length; i++) {
    for (let j = 0; j < needle.length; j++) {
      if (needle[j] !== haystack[i + j]) break;
      if (j === needle.length - 1) return i;
    }
  }

  return -1;
}
