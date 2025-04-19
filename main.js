// This was my solution for the leetcode problem "Best Time to Buy and Sell Stock in javascript".trying to think about this in python was a definite challenge
 
 
var maxProfit = function (prices) {
  //always buy stock when it's low and sell high!

  let maxProfit = 0;
  let buyPrice = prices[0];

  if (prices.length === 0) {
    return 0;
  }

  for (const price of prices) {
    maxProfit = Math.max(maxProfit, price - buyPrice);
    buyPrice = Math.min(buyPrice, price);
  }
  return maxProfit;
};
