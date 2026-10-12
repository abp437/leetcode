import { GREEN, RED, RESET } from "./colors";

function buildFibonacci(n: number): number[] {
  if (n < 0) throw new Error("n must be non-negative");

  const series = [0, 1];

  if (n < 2) return series;

  for (let i = 2; i <= n; i++) {
    series[i] = series[i - 1] + series[i - 2];
    if (series[i] > n) break;
  }

  return series;
}

function threeFibonacciSum(n: number): boolean {
  const fibonacciSeries = buildFibonacci(n);

  for (let i = 0; i < fibonacciSeries.length - 2; i++) {
    const sum = fibonacciSeries[i] + fibonacciSeries[i + 1] + fibonacciSeries[i + 2];
    if (sum > n) return false;
    if (sum === n) return true;
  }

  return false;
}

const threeFibonacciSumTestCases = [0, 1, 2, 3, 4, 5, 6, 7, 10, 30];

const expectedResults: Record<number, boolean> = {
  0: false,
  1: false,
  2: true, // 0 + 1 + 1
  3: false,
  4: true, // 1 + 1 + 2
  5: false,
  6: true, // 1 + 2 + 3
  7: false,
  10: true, // 2 + 3 + 5
  30: false,
};

for (const n of threeFibonacciSumTestCases) {
  const result = threeFibonacciSum(n);
  const expected = expectedResults[n];

  const passed = result === expected;
  const status = passed ? `${GREEN}PASS${RESET}` : `${RED}FAIL${RESET}`;

  console.log(`n=${n}: result=${result}, expected=${expected} ${status}`);
}
