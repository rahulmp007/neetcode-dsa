class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s) {
        const filtered = s.replace(/[^a-z0-9]/gi, '').toLowerCase();
    
    // Compare filtered string with its reverse
    const reversed = filtered.split('').reverse().join('');

    return filtered === reversed;
    }
}
