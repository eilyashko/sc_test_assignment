# Cases CSV Summary

Dataset shape: 6,192 rows x 10 columns

## Columns

### Case ID

- dtype: `object`
- non-null: 6,192
- missing: 0 (0.00%)
- unique values: 6,192
- top 20 values:
  - 500dV00000Dt3ApQAJ: 1
  - 500dV00000E5hHBQAZ: 1
  - 500dV00000E5domQAB: 1
  - 500dV00000E5dn4QAB: 1
  - 500dV00000E5diIQAR: 1
  - 500dV00000E5df1QAB: 1
  - 500dV00000E5dX0QAJ: 1
  - 500dV00000E5dVUQAZ: 1
  - 500dV00000E5dNFQAZ: 1
  - 500dV00000E5dK9QAJ: 1
  - 500dV00000E5cxUQAR: 1
  - 500dV00000E5cvqQAB: 1
  - 500dV00000E5cpYQAR: 1
  - 500dV00000E5cnpQAB: 1
  - 500dV00000E5cStQAJ: 1
  - 500dV00000E5cKrQAJ: 1
  - 500dV00000E5cCgQAJ: 1
  - 500dV00000E5c9RQAR: 1
  - 500dV00000E5c7pQAB: 1
  - 500dV00000E5bjdQAB: 1

### Created Date

- dtype: `object`
- non-null: 6,192
- missing: 0 (0.00%)
- datetime range:
  - min: 2025-08-04 00:15:24
  - max: 2025-08-10 23:58:27

### Closed Date

- dtype: `object`
- non-null: 3,880
- missing: 2,312 (37.34%)
- datetime range:
  - min: 2025-08-04 08:14:47
  - max: 2025-08-13 10:06:21

### Case Origin

- dtype: `object`
- non-null: 6,192
- missing: 0 (0.00%)
- unique values: 9
- values: Backoffice, Email, Form_Mobile, Form_Web, OSKAR Email, Order Email, Outbound, Phone, Post

### Number of Emails Received

- dtype: `float64`
- non-null: 4,637
- missing: 1,555 (25.11%)
- numeric stats:
  - mean: 1.16929
  - median: 1
  - std: 0.524653
  - min: 1.0
  - max: 8.0

### Number of Emails Sent

- dtype: `float64`
- non-null: 4,438
- missing: 1,754 (28.33%)
- numeric stats:
  - mean: 1.35872
  - median: 1
  - std: 0.690402
  - min: 1.0
  - max: 8.0

### Contact Reason

- dtype: `object`
- non-null: 6,192
- missing: 0 (0.00%)
- unique values: 7
- values: New Scalable, No Reply, Null, Out of Scope, Product Question, System Issue, Systemic in Nature

### Bucket

- dtype: `object`
- non-null: 6,192
- missing: 0 (0.00%)
- unique values: 10
- values: Account Management, Account Opening, Broker Portfolio Management, Broker Trading, Corporate Actions, Goodwill, Null, Other, Payments, Taxes

### Topic

- dtype: `object`
- non-null: 6,192
- missing: 0 (0.00%)
- unique values: 52
- top 20 values:
  - Account Management - MISC: 498
  - Corporate Actions - Stock Split: 350
  - Broker Trading - Savings Plans: 346
  - Account Management - Client Documents: 340
  - Account Management - Data Change: 332
  - Broker Portfolio Management - Transfer OUT: 318
  - Broker Trading - MISC: 298
  - Broker Portfolio Management - Transfer IN: 291
  - Payments - Deposits: 249
  - Account Opening - Opening Process: 220
  - Account Management - Cancellation: 218
  - Payments - Withdrawals: 199
  - Account Opening - MISC: 196
  - Account Management - 2FA: 182
  - Account Opening - Account Reactivation: 176
  - Broker Trading - Trade Issues: 174
  - Taxes - MISC: 174
  - Account Management - IT Issues: 167
  - Account Opening - KYC: 166
  - Broker Portfolio Management - MISC: 135

### Sub-Topic

- dtype: `object`
- non-null: 677
- missing: 5,515 (89.07%)
- unique values: 21
- values: Account Statement, Address, App, Blocked Account, Cancelled Account, Compliance Copy, Duplicate User, ELTIF, Email, Identification, Joint Account, Junior Account, Login, Missing Document, Name, Phone, Portfolio Report, Reference Account, Securities Statement, Spread Fee, Web
