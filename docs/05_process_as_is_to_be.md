# Process Map: As-Is vs To-Be

## As-Is (manual reporting)
```mermaid
flowchart LR
    A[Export data from system] --> B[Clean data manually in Excel]
    B --> C[Build pivot tables]
    C --> D[Create charts]
    D --> E[Email report to managers]
    E --> F[Manager asks a new question]
    F --> B
```

**Pain points**
- Every new question restarts the cycle (loop F to B).
- Cleaning rules differ between people, so numbers do not match.
- Cancellations are not separated, so revenue is overstated.
- No customer segments and no forecast.
- Effort is roughly 2-3 days per report (scenario assumption).

## To-Be (automated, self-service)
```mermaid
flowchart LR
    A[Raw transaction data] --> B[Python cleaning with documented rules]
    B --> C[KPI, RFM and forecast outputs]
    C --> D[Power BI dashboard]
    D --> E[Managers filter and explore themselves]
    E --> F[Decisions and actions]
    F --> G[Monthly data refresh]
    G --> A
```

**Improvements**

| Area | As-Is | To-Be |
|---|---|---|
| Cleaning | Manual, inconsistent | Scripted, rules documented (CR-01 to CR-06) |
| Reporting effort | Days | Minutes after refresh |
| Questions from managers | New request each time | Slicers answer them |
| Cancellations | Hidden in totals | Separate KPI |
| Customers | Treated alike | RFM segments with playbook |
| Planning | Guesswork | 6-month forecast with error shown |

*As-Is effort figures are scenario assumptions, not measured data.*
