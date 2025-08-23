# Project Title
**Reinforcement Learning Agent for Triangular Forex Arbitrage (USD–EUR–ZAR)**  
**Stage:** Problem Framing & Scoping (Stage 01)  

---

## Problem Statement
Triangular arbitrage in the forex market exploits price discrepancies between three currency pairs to generate a profit.  
For example, trading USD → EUR → ZAR → USD can yield a gain if the cross-rate pricing is inconsistent.  
While theoretically risk-free, in real markets the opportunity often disappears after accounting for **transaction costs** such as bid–ask spreads, commissions, and slippage.  
This project will develop a **Reinforcement Learning (RL) agent** trained on **tick-level bid/ask data** from TrueFX for **July 2025** to learn an optimal trading policy that maximizes **net profit after costs**.

---

## Stakeholder & User
**Primary Stakeholder:** Quantitative trading teams, hedge funds, and algorithmic trading researchers.  
**End Users:**  
- Algorithmic traders developing execution models.  
- Finance students studying arbitrage strategies.  
- Researchers analyzing market efficiency and AI decision-making.  
**Timing & Workflow Context:**  
The model is for **backtesting and educational simulation**, not live market execution.

---

## Useful Answer & Decision
The RL agent will provide:
- A **policy** indicating when to execute the USD–EUR–ZAR arbitrage loop.
- Profitability estimates **after transaction costs**.
- Insights on conditions (spread size, volatility) that make arbitrage viable.

---

## Assumptions & Constraints
- **Data:** Tick-level bid/ask prices from TrueFX for USD/ZAR, EUR/USD, EUR/ZAR (July 2025).
- **Costs:** Bid–ask spread, commission per trade, and slippage will be modeled.
- **Execution:** All three trades in the arbitrage loop are assumed to occur within the same tick for proof-of-concept.
- **Limitation:** Opportunities in real-time markets are extremely short-lived and require HFT infrastructure.

---

## Known Unknowns / Risks
- Accurate cost modeling — spreads in emerging market FX (like ZAR) can be wide and volatile.
- Risk of overfitting the RL agent to one month's market conditions.
- Dataset alignment issues if ticks between currency pairs are not perfectly synchronized.

---

## Lifecycle Mapping
Goal → Stage → Deliverable
- Identify arbitrage opportunities in USD–EUR–ZAR → Stage 02: Data Collection → Tick-level merged dataset.
- Model and apply realistic transaction costs → Stage 03: Data Preparation → Cost-adjusted dataset.
- Train RL agent on simulated environment → Stage 04: Modeling → Trained policy & performance metrics.
- Evaluate against baseline strategies → Stage 05: Reporting → Research report with charts & conclusions.

---

## Repo Plan
- `/data/` → Tick-level bid/ask data from TrueFX for USD/ZAR, EUR/USD, EUR/ZAR.
- `/src/` → Data processing scripts, RL environment code, training scripts.
- `/notebooks/` → Exploratory analysis, baseline detection algorithms.
- `/docs/` → Stakeholder memo, methodology document, final report.

**Update Cadence:** Weekly commits showing progress from raw data → processed → model training → results.
