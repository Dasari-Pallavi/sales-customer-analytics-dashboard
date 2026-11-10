cat << 'EOF' > docs/01_problem_statement.md
# 1. Business Problem Statement

## Background
A UK-based online giftware retailer processes over 1,000,000 transactions across 2009–2011 in the UK and 35+ international markets. Currently, leadership relies on manual spreadsheet exports to review monthly revenue.

## Core Operational Pain Points
1. **Delayed Reporting:** Consolidating raw invoice logs into monthly summaries takes 3+ business days, delaying pricing and inventory decisions.
2. **Unquantified Return Leakage:** Cancelled orders (invoices starting with "C") are mixed into raw exports, distorting gross revenue and hiding high-return items.
3. **Untargeted Marketing:** Over 4,300 unique customers are treated identically because management lacks visibility into recency, frequency, and monetary spend.
4. **Reactive Inventory Planning:** Without a statistical revenue forecast, Q4 holiday demand spikes cause stockouts on top-selling SKUs.

## Objective
Design and validate an **AI-Powered Sales & Customer Analytics Dashboard** that automates KPI tracking, isolates return rates, segments customers using RFM + K-Means clustering, and forecasts revenue 6 months ahead.
EOF
