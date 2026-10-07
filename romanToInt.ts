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
