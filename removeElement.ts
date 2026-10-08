// Remove Element using 2 pointer method. Most efficient.
function removeElement(nums: number[], val: number): number {
  let writeIndex = 0;
  let count = 0;

  for (let i = 0; i < nums.length; i++) {
    const num = nums[i];
    
    if(num !== val) {
      nums[writeIndex] = num;
      writeIndex++;
      count++;
    }
  }

  return count;
}

// My approach to use in-place swapping and maintaining the position to swap
function removeElement(nums: number[], val: number): number {
  let i = 0;
  let k = 0;

  while (i < nums.length) {
    if (nums[i] !== val) {
      i++;
      k++;
      continue;
    }

    let j = i + 1;

    while (j < nums.length && nums[j] === val) {
      j++;
    }

    if (j === nums.length) {
      break;
    }

    nums[i] = nums[j];
    nums[j] = val;

    i++;
    k++;
  }

  return k;
}
