// Problem Link: https://leetcode.com/problems/two-sum/

// Implemented using Map and complement finding
function twoSum(nums: number[], target: number): number[] {
    const numsMap = new Map();

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];

        if (numsMap.has(complement)) {
            return [numsMap.get(complement), i];
        }

        numsMap.set(nums[i], i);
    }
};
