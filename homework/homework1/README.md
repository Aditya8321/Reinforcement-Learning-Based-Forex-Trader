# Project Title 

Comparative Analysis of Global Bond Markets: India and US (2019–2024)

**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement

The bond markets prove to be quite an efficient investment tools for financial institutions and helps in providing economic stability and investment stratergy. At a global scale, different markets exhibit varying risks, yields and correlations over time. This project will comprise of a comprehensive study of past 5 year data (2019-2024) of the bond markets in India and the United States, focusing primarily on the short term (3 months) and long term (5 years) bonds. By comparing these bonds through market volatility, yield trends and cross market correlations, we aim to conclude which market proved to be a better investment relative to the risk demanded, any possibilites for currency arbitrage, and correlation between these markets. 

## Stakeholder & User

Primary Stakeholder: Institutional investors, sovereign wealth funds, and global macro hedge funds seeking yield optimization and risk-adjusted returns.
End Users: Financial analysts, economists, and policy advisors interested in yield curve analysis and cross-market capital flow dynamics.
Timing & Workflow Context: Insights will be most valuable during portfolio rebalancing cycles, monetary policy shifts, and in response to macroeconomic shocks.

## Useful Answer & Decision

The project will produce descriptive yield comparisons, correlation analysis, and theoretical arbitrage evaluations based on interest rate parity. Outputs will include:

Yield performance metrics for short- and long-term bonds in each market.

Correlation coefficients between India and US bonds.

Identification of periods where covered interest arbitrage may have been feasible.

Visualizations of yield curves, spreads, and deviations from parity conditions.

## Assumptions & Constraints

Data Availability: Daily or monthly historical yields for 3M and 5Y bonds from RBI and FRED; spot and forward FX rates for USD/INR.

Time Horizon: Jan 2019 – Aug 2024.

Constraints: Possible short-term missing data; differences in bond market liquidity; FX forward rate accessibility.

Compliance: Data sources must be publicly licensed or accessible through institutional data subscriptions.

## Known Unknowns / Risks

FX forward market data availability for historical periods.

India’s partial capital controls limiting arbitrage execution in practice.

Yield distortions due to COVID-19 and policy interventions (e.g., US QE, India rate cuts).

## Lifecycle Mapping
Goal → Stage → Deliverable

Compare short- and long-term yields → Stage 02: Data Collection → Dataset & Data Dictionary.

Assess market correlation → Stage 03: Data Analysis → Correlation tables & charts.

Evaluate parity-based arbitrage → Stage 03: Data Analysis → Arbitrage feasibility report.

Present findings → Stage 04: Reporting → Final report & visual dashboards.

## Repo Plan

/data/ → Raw and processed yield and FX data.

/src/ → Scripts for data cleaning, correlation, and arbitrage calculations.

/notebooks/ → Exploratory Data Analysis (EDA), yield curve analysis, and arbitrage testing.

/docs/ → Stakeholder memo, final report, and visualizations.
Update Cadence: Weekly commits with incremental analysis and visual outputs.