# Stakeholder Memo
**Stage:** Problem Framing & Scoping (Stage 01)

## Problem Statement
Stock prices are affected by a combination of market trends, macroeconomic factors, sector performance, and company-specific events. The high volatility and complexity of the financial market make it challenging for investors and analysts to generate accurate short-term forecasts. Incorrect predictions can lead to poor investment decisions and increased risk exposure.

This project focuses on developing a predictive model that uses historical price data and key financial indicators to forecast short-term stock prices. By improving the accuracy of predictions, the model will support better decision-making, help mitigate risks, and potentially enhance portfolio returns.

## Stakeholders and Users
- **Primary Stakeholders:** Individual investors, financial analysts, portfolio managers, and asset management firms.
- **End Users:** Traders and investment teams who rely on timely forecasts to decide when to buy, hold, or sell securities.

## Useful Answer & Decision
- **Answer Type:** Predictive
- **Decision Supported:** Whether to buy, hold, or sell a given stock in the short term.
- **Metric for Success:** Forecast accuracy, evaluated using RMSE and MAPE.

## Assumptions
1. Historical price data and financial indicators contain patterns useful for short-term forecasting.
2. Data quality is sufficient and regularly updated.
3. External shocks (e.g., unexpected geopolitical events) are rare or can be managed by model retraining.

## Risks
- Sudden market disruptions (e.g., economic crises, geopolitical events) may reduce model accuracy.
- Overfitting to historical patterns that may not hold in the future.
- Data delays or missing values affecting real-time predictions.

## Lifecycle Mapping
Goal → Deliverable  
- Define problem and stakeholders → Project description and scope document  
- Prepare and analyze data → Clean dataset and exploratory analysis report  
- Build and evaluate model → Trained predictive model with performance metrics  
- Present and document results → Final report and visualizations

## Repo Plan
/data/, /src/, /notebooks/, /docs/ ; weekly updates