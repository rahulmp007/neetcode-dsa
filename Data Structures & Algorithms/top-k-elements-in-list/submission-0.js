class Solution {
    /**
     * @param {number[]} nums
     * @param {number} k
     * @return {number[]}
     */
    topKFrequent(nums, k) {

       

        let numMap = {};
        for (let i = 0; i < nums.length; i++) {
          
          if (!(nums[i] in numMap)) {
            numMap[nums[i]] = 0;
        }
        numMap[nums[i]] += 1;
          
        }
        
       let sorted =  Object.entries(numMap).sort((a,b) => b[1] - a[1] );


        console.log(sorted);
        
        return sorted.slice(0,k).map((k,v)=> Number(k[0]));



    }
}
