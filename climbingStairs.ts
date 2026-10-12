// Recursive
function recursiveClimbStairs(n: number): number {
  if (n < 0) throw new Error("n must be non-negative");

  const computed: { [key: number]: number } = { 1: 1, 2: 2 };

  const computeSteps = (num: number): number => {
    if (computed[num]) return computed[num];

    const firstNumSteps = computeSteps(num - 1);
    const secondNumSteps = computeSteps(num - 2);

    computed[num] = firstNumSteps + secondNumSteps;

    return computed[num];
  };

  return computeSteps(n);
}

// Iterative
function iterativeClimbStairs(n: number): number {
  if (n < 0) throw new Error("n must be non-negative");
  if (n < 1) return 0;

  const preComputed: number[] = [1, 2];

  if (n < 3) return preComputed[n - 1];

  for (let i = 2; i < n; i++) {
    preComputed[i] = preComputed[i - 1] + preComputed[i - 2];
  }

  return preComputed[n - 1];
}

// Test cases
const stairsTestCases = [1, 2, 3, 5, 10, 30];

for (const n of stairsTestCases) {
  const recursive = recursiveClimbStairs(n);
  const iterative = iterativeClimbStairs(n);

  console.log(`n=${n}: recursive=${recursive}, iterative=${iterative}`, recursive === iterative ? "PASS" : "FAIL");
}
