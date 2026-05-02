class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let anagramMap = {};
        let groups = [];

        for (let i = 0; i < strs.length; i++) {
            let primary = strs[i].split("").sort().join("");
            if (!(primary in anagramMap)) {
                anagramMap[primary] = [strs[i]];
            } else {
                anagramMap[primary].push(strs[i]);
            }

        }


        return Object.values(anagramMap);
    }
}
