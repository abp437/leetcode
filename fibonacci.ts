// Recursive
function recursiveFibonacci(n: number): number {
  const calculateFibonacci = (num: number): number => {
    if (num < 2) return num;
    return calculateFibonacci(num - 1) + calculateFibonacci(num - 2);
  };

  return calculateFibonacci(n);
}

// Iterative
function iterativeFibonacci(n: number): number {
  const initialSequence = [0, 1];

  if (n < 2) return initialSequence[n];

  for (let i = 2; i <= n; i++) {
    initialSequence[i] = initialSequence[i - 1] + initialSequence[i - 2];
  }

  return initialSequence[n];
}

const fibonacciTestCases = [1, 2, 3, 5, 10, 30];

for (const n of fibonacciTestCases) {
  const recursive = recursiveFibonacci(n);
  const iterative = iterativeFibonacci(n);

  console.log(`n=${n}: recursive=${recursive}, iterative=${iterative}`, recursive === iterative ? "PASS" : "FAIL");
}
