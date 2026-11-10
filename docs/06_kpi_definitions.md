## RFM Scoring Rules
- Snapshot date = last invoice date in the data + 1 day.
- Recency = days between the customer's last order and the snapshot date.
- Frequency = number of distinct invoices.
- Monetary = total revenue from valid sales (excluding cancellations).
- Each metric is scored 1-5 using quintiles (5 = best; for Recency, fewer days = 5).

| Segment | Rule |
|---|---|
| Champions | R >= 4 and F >= 4 |
| Loyal Customers | R >= 3 and F >= 3 (not Champions) |
| New / Promising | R >= 4 and F <= 2 |
| At Risk | R <= 2 and F >= 3 |
| Lost | R <= 2 and F <= 2 |
| Need Attention | All others |

## K-Means Method
- Inputs: log-transformed Recency, Frequency, Monetary, then standardised.
- k = 4, chosen using the elbow method and silhouette score (see chart 05).
- random_state = 42 so results can be repeated.
