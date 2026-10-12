import { GREEN, RED, RESET } from "./colors";

function auxFibonacci(n: number): number {
  if (n < 0) throw new Error("n must be non-negative");
  if (n < 2) return n;

  let prev = 0;
  let current = 1;

  for (let i = 2; i <= n; i++) {
    let sum = prev + current;
    prev = current;
    current = sum;
  }

  return current;
}

// Recursive
function recursiveFibonacci(n: number): number {
  if (n < 0) throw new Error("n must be non-negative");

  const fibo = new Map<number, number>([
    [0, 0],
    [1, 1],
  ]);

  const calculateFibonacci = (num: number): number => {
    if (num < 2) return num;
    if (fibo.has(num)) return fibo.get(num)!;

    const result = calculateFibonacci(num - 1) + calculateFibonacci(num - 2);

    fibo.set(num, result);

    return fibo.get(num)!;
  };

  return calculateFibonacci(n);
}

// Iterative
function iterativeFibonacci(n: number): number {
  if (n < 0) throw new Error("n must be non-negative");

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
  const aux = auxFibonacci(n);

  const passed = recursive === iterative && iterative === aux;
  const status = passed ? `${GREEN}PASS${RESET}` : `${RED}FAIL${RESET}`;

  console.log(`n=${n}: recursive=${recursive}, iterative=${iterative}, aux=${aux} ${status}`);
}
