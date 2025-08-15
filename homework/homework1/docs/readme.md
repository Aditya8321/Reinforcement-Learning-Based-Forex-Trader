# Stakeholder Memo  
**Project:** Reinforcement Learning Agent for Triangular Forex Arbitrage (USD–EUR–ZAR)  
**Prepared for:** Quantitative Traders, Algorithmic Researchers, and Financial Analysts  
**Date:** August 2025  

---

## Purpose  
This project will design a Reinforcement Learning (RL) agent to detect and act on triangular arbitrage opportunities in the USD–EUR–ZAR forex market using **tick-level bid/ask data** from TrueFX for **July 2025**.  
Triangular arbitrage involves converting one currency to another in a three-step loop (e.g., USD → EUR → ZAR → USD) when market rates are misaligned, generating a profit before costs.  
The RL agent will learn to trade only when the **net profit after spreads, commissions, and slippage** is positive.

---

## Why This Matters  
- **Practical Relevance:** Even though true arbitrage is rare in live markets, studying it provides valuable insights into market efficiency and microstructure.  
- **Educational Value:** The project shows how AI can learn optimal decision-making in cost-constrained environments.  
- **Applied Research:** Results can inform algorithmic trading strategies and transaction cost modeling.

---

## Scope & Approach  
- **Currencies Studied:** USD, EUR, ZAR.  
- **Pairs Used:** USD/ZAR, EUR/USD, EUR/ZAR.  
- **Dataset:** Tick-level bid/ask from TrueFX for July 2025.  
- **Key Analyses:**  
  1. Identify triangular arbitrage opportunities.  
  2. Apply transaction cost model (spread, commission, slippage).  
  3. Train RL agent to maximize cost-adjusted net profit.  
- **Execution Assumption:** All three trades in the loop occur within the same tick.

---

## Anticipated Outcomes  
- **Learned Policy:** RL model indicating when to execute trades.  
- **Profitability Analysis:** Net profit distribution after costs.  
- **Market Insights:** Patterns in volatility and spread that favor arbitrage.  
- **Baseline Comparison:** RL agent vs rule-based arbitrage detector.

---

## Next Steps & Deliverables  
1. **Data Processing:** Clean and align USD/ZAR, EUR/USD, EUR/ZAR ticks to a common timeline.  
2. **Cost Modeling:** Implement realistic spread, commission, and slippage adjustments.  
3. **RL Environment:** Create simulation environment to test agent behavior.  
4. **Model Training & Evaluation:** Train RL agent, compare to baseline.  
5. **Reporting:** Summarize findings in a research-style report with charts.
