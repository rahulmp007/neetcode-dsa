class Solution {
    /**
     * @param {number[]} nums
     * @return {number[][]}
     */
    threeSum(nums) {

        let groups = [];
        nums.sort((a, b) => a - b);
        console.log(nums);
        for (let pointer = 0; pointer < nums.length - 2; pointer++) {
             if (pointer > 0 && nums[pointer] === nums[pointer - 1]) continue;
            let i = pointer + 1;
            let j = nums.length - 1;

            while (i < j) {
                let sum = nums[pointer] + nums[i] + nums[j];
                let grp = [nums[pointer], nums[i], nums[j]];


                if (sum === 0) {
                    groups.push(grp);
                   
                i++;
                j--;

            while (i < j && nums[i] === nums[i - 1]) i++;
            while (i < j && nums[j] === nums[j + 1]) j--;
            continue;
                }

                if (sum > 0) {
                    j--;
                } else {
                    i++;
                }

            }


        }
        console.log(groups);
        return groups;

    }
}