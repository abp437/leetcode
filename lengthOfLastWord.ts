// Problem Link: https://leetcode.com/problems/length-of-last-word/description/

// Iterate from the back - Best, Early Exit
function lengthOfLastWord(s: string): number {
  if (s.length === 0) return 0;
  let lastWordLength = 0;
  const maxIndex = s.length - 1;

  for (let i = maxIndex; i >= 0; i--) {
    const char = s[i];
    const isSpace = char === " ";

    if (isSpace) {
      if (lastWordLength > 0) return lastWordLength;
      continue;
    }

    lastWordLength++;
  }

  return lastWordLength;
}

// Iterate from the Front
function lengthOfLastWord(s: string): number {
  if (s.length === 0) return 0;
  let lastWordLength = 0;
  let hasEncounteredSpace = false;

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    const isSpace = char === " ";

    if (isSpace) {
      hasEncounteredSpace = true;
      continue;
    }

    if (hasEncounteredSpace) {
      hasEncounteredSpace = false;
      lastWordLength = 1;
    } else {
      lastWordLength++;
    }
  }

  return lastWordLength;
}

// Pure TypeScript, but less efficient, because it creates a new string, then an array, then array popping.
function lengthOfLastWord(s: string): number {
  return s.trim().split(" ").pop().length;
}
