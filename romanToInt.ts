// Problem Link: https://leetcode.com/problems/roman-to-integer/

// Implemented using current and previous character value comparisons:
function romanToInt(s: string): number {
  const values: Record<string, number> = {
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,
  };

  let accumulator = 0;
  if (s.length === 1) return values[s];

  let i = 0;

  while (i < s.length) {
    const nextCharOverflow = i + 1 === s.length;
    const currentChar = s[i];
    const currentValue = values[currentChar];

    if (nextCharOverflow) {
      accumulator += currentValue;
      break;
    } 

    const nextChar = s[i + 1];
    const nextValue = values[nextChar];
    const isSubtractive = currentValue < nextValue;

    if (isSubtractive) {
      accumulator += (values[nextChar] - values[currentChar]);
      i += 2;
    } else {
      accumulator += values[currentChar];
      i++;
    }
  }

  return accumulator;
}

// Older Solution, comparing character matching of 2 subtractive chars:
function romanToInt(s: string): number {
  const values: Record<string, number> = {
    // Additive
    I: 1,
    V: 5,
    X: 10,
    L: 50,
    C: 100,
    D: 500,
    M: 1000,

    // Subtractive
    IV: 4,
    IX: 9,
    XL: 40,
    XC: 90,
    CD: 400,
    CM: 900,
  };

  let accumulator = 0;
  if (s.length === 1) return values[s];

  let i = 0;

  while (i < s.length) {
    const currentValue = s[i];
    const postfixValue = (i + 1) === s.length ? 0 : s[i + 1];
    const comboValue = `${currentValue}${postfixValue}`;
    const isSubtractive = Object.hasOwn(values, comboValue);

    if (isSubtractive) {
      accumulator += values[comboValue];
      i += 2;
    } else {
      accumulator += values[currentValue];
      i++;
    }
  }

  return accumulator;
}
