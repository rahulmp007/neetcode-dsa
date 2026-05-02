class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let minPrice = Infinity;
        let maximumProfit = 0;

        for(let price of prices){
            if(price < minPrice){
                minPrice = price
            }else{
                maximumProfit = Math.max(maximumProfit,price-minPrice);
            }

        }

        return maximumProfit;
    }
}
