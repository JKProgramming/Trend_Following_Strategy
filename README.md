# Trend_Following_Strategy


The concept of a trend following strategy is that the security's price usually follows the current trend's direction.

The basic principles of a trend following strategy involve the following:

•	If the fast signal crosses above the slow signal, the market is bullish, and an uptrend is forming. This is classed as a buy signal.

•	If the fast signal crosses below the slow signal, the market is bearish, and a downtrend is forming. This is classed as a sell signal.

•	If the fast signal and the slow signal are close together, it indicated sideways movement in the market as there is no clear buy/sell signal.

Recent Modifications 11/09/2023
Here are the modifications I applied:

 •	To make it clearer, I renamed the variable df as data.
 
 •	 To be more precise, I used SMA-10 instead of MA-10, which means simple moving average.
 
 •	 To increase the complexity, I switched MA-50 to EMA-50, which means exponential moving average. An EMA emphasizes the latest prices and adjusts more quickly to price movements.
 
 •	 To enhance the accuracy, I included an additional criterion for the buy and sell signals, which is that the price has to be higher than the SMA-10 for a buy signal, and lower than the SMA-10 for a sell signal. This provides an extra validation and minimizes false signals.


References

•	A Step-by-Step Guide Towards a Trend-Following Trading Strategy. (2020). *Medium*. Available at: https://medium.com/swlh/a-step-by-step-guide-towards-a-trend-following-trading-strategy-814b198b815 (Accessed: 12 October 2022).

•	Graham, J. (2018). The Speed of Trend-Following. *CME Group*. Available at: https://www.cmegroup.com/education/files/speed-of-trend-graham-research-march-2018.pdf (Accessed: 12 October 2022).

•	Moving Average Crossover Strategies. (n.d.). *TrendSpider Learning Center*. Available at: https://trendspider.com/learning-center/moving-average-crossover-strategies/ (Accessed: 12 October 2022).

•	Moving Average Trading Strategies (Rules And Backtest) – What Is The Best Moving Average? (2021). *Quantified Strategies*. Available at: https://www.quantifiedstrategies.com/moving-average-trading-strategy/ (Accessed: 12 October 2022)

•	How To Use A Moving Average For Trend Following. (2020). *The5%ers*. Available at: https://the5ers.com/moving-average-for-trend-following/ (Accessed: 12 October 2022).

