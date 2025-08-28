# Project Title
**Reinforcement Learning Agent for Triangular Forex Arbitrage (USD–EUR–ZAR)**  
**Stage:** Problem Framing & Scoping (Stage 01)  

---

## Problem Statement
In the on-going world, agentic trading has become quite popular. This project is going to simulate a reinforcement learning agent that will be trading on a forex currency exchange using a Deep Q Learning Network. 
The goal is to train a Reinforcement Learning (RL) agent to decide when to buy or sell USD/ZAR to maximize profit with a limited starting capital (e.g., $10,000).
The agent will learn from tick-level bid/ask price data and account for transaction costs such as spreads, commissions, and slippage.
Unlike triangular arbitrage, this focuses on single-pair trading, making it more realistic for individuals or small-scale automated strategies.

---

## Stakeholder & User
**Primary Stakeholder:** Individual traders, trading algorithm developers, and financial AI researchers. 
**End Users:**  
Algorithmic traders looking to simulate small-scale FX trading.

Students studying reinforcement learning in finance.

Researchers analyzing single-currency decision-making.
Timing & Workflow Context:

For simulation and backtesting only, not real-time trading.  
**Timing & Workflow Context:**  
The model is for **backtesting and educational simulation**, not live market execution.

---

## Useful Answer & Decision

The RL agent will provide:

Buy/sell/hold actions at optimal times.

Profit and loss simulations over historical data.

Insights into market conditions (volatility, trend) that impact profitability.

---

## Assumptions & Constraints
Data: Tick-level bid/ask prices for USD/ZAR.

Budget: $10,000 starting capital.

Costs: Spread, per-trade commission, and slippage will be included in simulations.

Execution: Each trade occurs at a single tick; fractional execution or partial fills are ignored.

Limitation: Real-time market dynamics (latency, HFT competition) are not modeled.
---

## Known Unknowns / Risks

Risk of overfitting to historical price patterns.

Unrealistic assumptions about execution speed.

Market shocks or illiquidity may reduce strategy profitability.

---

## Lifecycle Mapping
| Goal                                                       | Stage                      | Deliverable                                                |
| ---------------------------------------------------------- | -------------------------- | ---------------------------------------------------------- |
| Prepare tick-level USD/ZAR dataset                         | Stage 02: Data Collection  | Cleaned and aligned price data                             |
| Apply transaction cost modeling                            | Stage 03: Data Preparation | Cost-adjusted dataset                                      |
| Train RL agent on historical simulation                    | Stage 04: Modeling         | Trained agent with performance metrics                     |
| Evaluate vs baseline (e.g., buy-and-hold, random strategy) | Stage 05: Reporting        | Research report with charts, insights, and recommendations |


---

## Repo Plan
- `/data/` → Tick-level bid/ask data from TrueFX for USD/ZAR, EUR/USD, EUR/ZAR.
- `/src/` → Data processing scripts, RL environment code, training scripts.
- `/notebooks/` → Exploratory analysis, baseline detection algorithms.
- `/docs/` → Stakeholder memo, methodology document, final report.

**Update Cadence:** Weekly commits showing progress from raw data → processed → model training → results.
