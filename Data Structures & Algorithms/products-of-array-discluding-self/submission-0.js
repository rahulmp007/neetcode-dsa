class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    productExceptSelf(nums) {

        let prefix = 1;
        let prefixArray = [];
        for (let i = 0; i < nums.length; i++) {
            prefixArray[i] = prefix;
            prefix = prefix * nums[i];
        }


        console.log(prefixArray);


        let suffix = 1;
        let suffixArray = [];
        for (let j = nums.length - 1; j >= 0; j--) {
            suffixArray[j] = suffix;
            suffix = suffix * nums[j];
        }

        console.log(suffixArray);


        let output = [];
        for (let i = 0; i < nums.length; i++) {
            output[i] = prefixArray[i] * suffixArray[i];
        }
        console.log(output);
        return output;


    }
}
