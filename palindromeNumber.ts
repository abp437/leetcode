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
