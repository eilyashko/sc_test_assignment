# Calls_Data.csv EDA Summary

- Rows: 13329
- Columns: 25

## Categorical Columns


```
- Column: Call Time
  - unique values: 3080
  - missing values: 0
  - top 20 by count: 8/4/25 11:56 (27), 8/7/25 16:12 (23), 8/4/25 17:17 (20), 8/7/25 16:13 (19), 8/4/25 9:36 (19), 8/4/25 10:52 (17), 8/4/25 10:14 (16), 8/4/25 10:13 (16), 8/6/25 14:08 (16), 8/4/25 9:32 (16), 8/7/25 9:58 (16), 8/7/25 12:19 (16), 8/7/25 12:46 (15), 8/4/25 17:16 (15), 8/7/25 16:06 (15), 8/4/25 15:13 (15), 8/7/25 16:01 (15), 8/4/25 13:02 (15), 8/5/25 11:16 (15), 8/7/25 15:53 (15) (showing 20 of 3080)
- Column: Call ID
  - unique values: 3466
  - missing values: 0
  - top 20 by count: 00000000-01dc-050f-6bfc-186200001b17 (15), 00000000-01dc-0858-b798-59ae0000280d (13), 00000000-01dc-0857-662b-bec800002802 (12), 00000000-01dc-055d-5c76-119300001e60 (12), 00000000-01dc-052b-6c48-fd8f00001c63 (11), 00000000-01dc-06df-c91e-1d640000234e (11), 00000000-01dc-051a-9916-84ce00001b97 (11), 00000000-01dc-078c-2845-dbf600002567 (11), 00000000-01dc-0511-d15a-362100001b32 (11), 00000000-01dc-06ab-e437-7394000021d7 (11), 00000000-01dc-0869-14c6-203400002878 (11), 00000000-01dc-0784-4436-dc3900002500 (10), 00000000-01dc-06df-3f03-427200002347 (10), 00000000-01dc-07bb-6e20-c4a7000026b5 (10), 00000000-01dc-06ab-1cb9-a9f1000021d5 (10), 00000000-01dc-0517-2219-8ab700001b73 (10), 00000000-01dc-06b0-02de-336c000021fb (10), 00000000-01dc-054d-1161-e36900001dcf (10), 00000000-01dc-05e6-0054-15fc00001f50 (10), 00000000-01dc-07af-ecc3-63ef0000268f (10) (showing 20 of 3466)
- Column: Direction
  - unique values: 4
  - missing values: 0
  - values: Inbound, Inbound Queue, Internal, Outbound
- Column: Status
  - unique values: 3
  - missing values: 0
  - values: Answered, Unanswered, Waiting
- Column: Ringing
  - unique values: 49
  - missing values: 0
  - values: 0:00:00, 0:00:01, 0:00:02, 0:00:03, 0:00:04, 0:00:05, 0:00:06, 0:00:07, 0:00:08, 0:00:09, 0:00:10, 0:00:11, 0:00:12, 0:00:13, 0:00:14, 0:00:15, 0:00:16, 0:00:17, 0:00:18, 0:00:19, 0:00:20, 0:00:21, 0:00:22, 0:00:23, 0:00:24, 0:00:25, 0:00:26, 0:00:27, 0:00:28, 0:00:31, 0:00:32, 0:00:33, 0:00:34, 0:00:37, 0:00:38, 0:00:39, 0:00:41, 0:00:42, 0:00:46, 0:00:47, 0:00:49, 0:00:50, 0:00:51, 0:00:54, 0:00:56, 0:00:59, 0:01:01, 0:01:18, 0:03:00
- Column: Talking
  - unique values: 984
  - missing values: 0
  - top 20 by count: 0:00:12 (418), 0:00:13 (413), 0:00:16 (408), 0:00:17 (365), 0:00:15 (357), 0:00:23 (354), 0:00:11 (348), 0:00:18 (340), 0:00:24 (316), 0:00:14 (314), 0:00:30 (308), 0:00:25 (300), 0:00:29 (297), 0:00:31 (297), 0:00:22 (275), 0:00:19 (260), 0:00:33 (253), 0:00:21 (250), 0:00:32 (246), 0:00:20 (221) (showing 20 of 984)
- Column: Cost
  - unique values: 126
  - missing values: 0
  - top 20 by count: 0.0 (13178), 0.06 (8), 0.05 (4), 0.03 (4), 0.04 (3), 0.07 (3), 0.77 (2), 0.02 (2), 2.55 (2), 0.12 (2), 1.55 (2), 0.55 (2), 0.16 (2), 1.31 (2), 0.38 (2), 5.71 (1), 2.14 (1), 6.93 (1), 3.82 (1), 15.27 (1) (showing 20 of 126)
- Column: day
  - unique values: 5
  - missing values: 0
  - values: 4/8/25, 5/8/25, 6/8/25, 7/8/25, 8/8/25
- Column: week
  - unique values: 1
  - missing values: 0
  - values: 32
- Column: Hour
  - unique values: 19
  - missing values: 0
  - values: 0, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22
- Column: Ring time
  - unique values: 49
  - missing values: 0
  - values: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 31, 32, 33, 34, 37, 38, 39, 41, 42, 46, 47, 49, 50, 51, 54, 56, 59, 61, 78, 180
- Column: IVR Time
  - unique values: 0
  - missing values: 13329
  - values: 
- Column: Wait Time in Queue
  - unique values: 371
  - missing values: 10849
  - top 20 by count: 29.0 (149), 30.0 (142), 31.0 (132), 32.0 (101), 33.0 (90), 28.0 (90), 34.0 (81), 35.0 (75), 27.0 (68), 36.0 (56), 49.0 (52), 26.0 (51), 39.0 (51), 37.0 (48), 50.0 (48), 25.0 (44), 51.0 (42), 48.0 (41), 38.0 (40), 46.0 (37) (showing 20 of 371)
- Column: Total Waiting Time (queue+ring)
  - unique values: 371
  - missing values: 10849
  - top 20 by count: 29.0 (149), 30.0 (142), 31.0 (132), 32.0 (101), 33.0 (90), 28.0 (90), 34.0 (81), 35.0 (75), 27.0 (68), 36.0 (56), 49.0 (52), 26.0 (51), 39.0 (51), 37.0 (48), 50.0 (48), 25.0 (44), 51.0 (42), 48.0 (41), 38.0 (40), 46.0 (37) (showing 20 of 371)
- Column: Environment (from Extension)
  - unique values: 4
  - missing values: 12948
  - values: DE/AT B2B, DE/AT Broker, DE/AT Fraud and 3PM, DE/AT Wealth
- Column: SLA breach
  - unique values: 2
  - missing values: 0
  - values: 0, 1
- Column: Volume
  - unique values: 2
  - missing values: 0
  - values: 0, 1
- Column: Abandon
  - unique values: 2
  - missing values: 0
  - values: 0, 1
- Column: Abandon (within 10s)
  - unique values: 2
  - missing values: 0
  - values: 0, 1
- Column: Year
  - unique values: 1
  - missing values: 0
  - values: 2025
- Column: Month
  - unique values: 1
  - missing values: 0
  - values: 8
- Column: Day
  - unique values: 5
  - missing values: 0
  - values: 4, 5, 6, 7, 8
- Column: Transfer
  - unique values: 1
  - missing values: 0
  - values: 0
```

## Numeric Columns

|                                |   count |     mean |     std |   min |    1% |   5% |   25% |   50% |   75% |   95% |     99% |   max |   missing |   zeros |   negatives |   unique_pct |
|:-------------------------------|--------:|---------:|--------:|------:|------:|-----:|------:|------:|------:|------:|--------:|------:|----------:|--------:|------------:|-------------:|
| Talk Time                      |    2465 | 349.945  | 311.153 |     0 | 14.64 |   32 |   121 |   286 |   470 | 935   | 1446.76 |  2947 |     10864 |       1 |           0 |      6.48211 |
| Total Call Duration (excl IVR) |   13329 |  80.9025 | 224.924 |     0 |  0    |    0 |     0 |     0 |     0 | 548.6 | 1056.6  |  3044 |         0 |   10849 |           0 |      7.11981 |


## Duration Columns

| column                          |   count |   missing |   mean_sec |   median_sec |   p95_sec |   max_sec |          sum_sec |   zeros | mean_hms   | median_hms   | p95_hms   | max_hms   | sum_hms   |
|:--------------------------------|--------:|----------:|-----------:|-------------:|----------:|----------:|-----------------:|--------:|:-----------|:-------------|:----------|:----------|:----------|
| Ringing                         |   13329 |         0 |    1.91402 |            0 |      11   |       180 |  25512           |   10260 | 0:00:02    | 0:00:00      | 0:00:11   | 0:03:00   | 7:05:12   |
| Talking                         |   13329 |         0 |  118.337   |           30 |     552   |      2947 |      1.57731e+06 |     177 | 0:01:58    | 0:00:30      | 0:09:12   | 0:49:07   | 438:08:29 |
| Ring time                       |   13329 |         0 |    1.91402 |            0 |      11   |       180 |  25512           |   10260 | 0:00:02    | 0:00:00      | 0:00:11   | 0:03:00   | 7:05:12   |
| Wait Time in Queue              |    2480 |     10849 |   86.9903  |           38 |     317.3 |      1805 | 215736           |       0 | 0:01:27    | 0:00:38      | 0:05:17   | 0:30:05   | 59:55:36  |
| Total Waiting Time (queue+ring) |    2480 |     10849 |   86.9903  |           38 |     317.3 |      1805 | 215736           |       0 | 0:01:27    | 0:00:38      | 0:05:17   | 0:30:05   | 59:55:36  |
| Talk Time                       |    2465 |     10864 |  349.945   |          286 |     935   |      2947 | 862614           |       1 | 0:05:50    | 0:04:46      | 0:15:35   | 0:49:07   | 239:36:54 |
| Total Call Duration (excl IVR)  |   13329 |         0 |   80.9025  |            0 |     548.6 |      3044 |      1.07835e+06 |   10849 | 0:01:21    | 0:00:00      | 0:09:09   | 0:50:44   | 299:32:30 |


## Datetime Columns

| column    |   count |   missing | min                 | max                 |   span_seconds |
|:----------|--------:|----------:|:--------------------|:--------------------|---------------:|
| Call Time |   13329 |         0 | 2025-08-04 00:42:00 | 2025-08-08 22:56:00 |         425640 |


## Date Columns

| column   |   count |   missing | min        | max        |   span_days |
|:---------|--------:|----------:|:-----------|:-----------|------------:|
| day      |   13329 |         0 | 2025-04-08 | 2025-08-08 |         122 |


## Binary Columns

| column               |   count |   missing |   zeros |   ones |   share_one |
|:---------------------|--------:|----------:|--------:|-------:|------------:|
| SLA breach           |   13329 |         0 |   12483 |    846 |    6.34706  |
| Volume               |   13329 |         0 |   10849 |   2480 |   18.606    |
| Abandon              |   13329 |         0 |   13197 |    132 |    0.990322 |
| Abandon (within 10s) |   13329 |         0 |   13234 |     95 |    0.712732 |


## Identifier Columns

| column   |   missing |   nunique |   unique_ratio |   duplicates |
|:---------|----------:|----------:|---------------:|-------------:|
| Call ID  |         0 |      3466 |        26.0035 |         9863 |


## Monetary Columns

|      |   count |      mean |      std |   min |   1% |   5% |   25% |   50% |   75% |   95% |   99% |   max |   missing |   zeros |   negatives |    sum |
|:-----|--------:|----------:|---------:|------:|-----:|-----:|------:|------:|------:|------:|------:|------:|----------:|--------:|------------:|-------:|
| Cost |   13329 | 0.0477313 | 0.776223 |     0 |    0 |    0 |     0 |     0 |     0 |     0 |  0.06 | 33.79 |         0 |   13178 |           0 | 636.21 |


## Schema JSON

```json
{
  "schema": {
    "columns": [
      {
        "name": "Call Time",
        "semantic_type": "datetime",
        "dtype": "object"
      },
      {
        "name": "Call ID",
        "semantic_type": "identifier",
        "dtype": "object"
      },
      {
        "name": "Direction",
        "semantic_type": "categorical",
        "dtype": "object"
      },
      {
        "name": "Status",
        "semantic_type": "categorical",
        "dtype": "object"
      },
      {
        "name": "Ringing",
        "semantic_type": "duration",
        "dtype": "object"
      },
      {
        "name": "Talking",
        "semantic_type": "duration",
        "dtype": "object"
      },
      {
        "name": "Cost",
        "semantic_type": "monetary",
        "dtype": "float64"
      },
      {
        "name": "day",
        "semantic_type": "date",
        "dtype": "object"
      },
      {
        "name": "week",
        "semantic_type": "constant",
        "dtype": "int64"
      },
      {
        "name": "Hour",
        "semantic_type": "integer",
        "dtype": "int64"
      },
      {
        "name": "Ring time",
        "semantic_type": "duration",
        "dtype": "int64"
      },
      {
        "name": "IVR Time",
        "semantic_type": "constant",
        "dtype": "float64"
      },
      {
        "name": "Wait Time in Queue",
        "semantic_type": "duration",
        "dtype": "float64"
      },
      {
        "name": "Total Waiting Time (queue+ring)",
        "semantic_type": "duration",
        "dtype": "float64"
      },
      {
        "name": "Talk Time",
        "semantic_type": "duration",
        "dtype": "float64"
      },
      {
        "name": "Total Call Duration (excl IVR)",
        "semantic_type": "duration",
        "dtype": "int64"
      },
      {
        "name": "Environment (from Extension)",
        "semantic_type": "categorical",
        "dtype": "object"
      },
      {
        "name": "SLA breach",
        "semantic_type": "binary",
        "dtype": "int64"
      },
      {
        "name": "Volume",
        "semantic_type": "binary",
        "dtype": "int64"
      },
      {
        "name": "Abandon",
        "semantic_type": "binary",
        "dtype": "int64"
      },
      {
        "name": "Abandon (within 10s)",
        "semantic_type": "binary",
        "dtype": "int64"
      },
      {
        "name": "Year",
        "semantic_type": "constant",
        "dtype": "int64"
      },
      {
        "name": "Month",
        "semantic_type": "constant",
        "dtype": "int64"
      },
      {
        "name": "Day",
        "semantic_type": "integer",
        "dtype": "int64"
      },
      {
        "name": "Transfer",
        "semantic_type": "constant",
        "dtype": "int64"
      }
    ]
  },
  "summaries": {
    "numeric": [
      {
        "column": "Talk Time",
        "count": 2465.0,
        "mean": 349.9448275862069,
        "std": 311.1534015962211,
        "min": 0.0,
        "1%": 14.64,
        "5%": 32.0,
        "25%": 121.0,
        "50%": 286.0,
        "75%": 470.0,
        "95%": 935.0,
        "99%": 1446.760000000002,
        "max": 2947.0,
        "missing": 10864,
        "zeros": 1,
        "negatives": 0,
        "unique_pct": 6.482106684672519
      },
      {
        "column": "Total Call Duration (excl IVR)",
        "count": 13329.0,
        "mean": 80.90254332658114,
        "std": 224.9242727045355,
        "min": 0.0,
        "1%": 0.0,
        "5%": 0.0,
        "25%": 0.0,
        "50%": 0.0,
        "75%": 0.0,
        "95%": 548.5999999999985,
        "99%": 1056.5999999999967,
        "max": 3044.0,
        "missing": 0,
        "zeros": 10849,
        "negatives": 0,
        "unique_pct": 7.1198139395303475
      }
    ],
    "duration": [
      {
        "column": "Ringing",
        "count": 13329,
        "missing": 0,
        "mean_sec": 1.9140220571685798,
        "median_sec": 0.0,
        "p95_sec": 11.0,
        "max_sec": 180.0,
        "sum_sec": 25512.0,
        "zeros": 10260,
        "mean_hms": "0:00:02",
        "median_hms": "0:00:00",
        "p95_hms": "0:00:11",
        "max_hms": "0:03:00",
        "sum_hms": "7:05:12"
      },
      {
        "column": "Talking",
        "count": 13329,
        "missing": 0,
        "mean_sec": 118.33663440618201,
        "median_sec": 30.0,
        "p95_sec": 552.0,
        "max_sec": 2947.0,
        "sum_sec": 1577309.0,
        "zeros": 177,
        "mean_hms": "0:01:58",
        "median_hms": "0:00:30",
        "p95_hms": "0:09:12",
        "max_hms": "0:49:07",
        "sum_hms": "438:08:29"
      },
      {
        "column": "Ring time",
        "count": 13329,
        "missing": 0,
        "mean_sec": 1.9140220571685798,
        "median_sec": 0.0,
        "p95_sec": 11.0,
        "max_sec": 180.0,
        "sum_sec": 25512.0,
        "zeros": 10260,
        "mean_hms": "0:00:02",
        "median_hms": "0:00:00",
        "p95_hms": "0:00:11",
        "max_hms": "0:03:00",
        "sum_hms": "7:05:12"
      },
      {
        "column": "Wait Time in Queue",
        "count": 2480,
        "missing": 10849,
        "mean_sec": 86.99032258064516,
        "median_sec": 38.0,
        "p95_sec": 317.29999999999836,
        "max_sec": 1805.0,
        "sum_sec": 215736.0,
        "zeros": 0,
        "mean_hms": "0:01:27",
        "median_hms": "0:00:38",
        "p95_hms": "0:05:17",
        "max_hms": "0:30:05",
        "sum_hms": "59:55:36"
      },
      {
        "column": "Total Waiting Time (queue+ring)",
        "count": 2480,
        "missing": 10849,
        "mean_sec": 86.99032258064516,
        "median_sec": 38.0,
        "p95_sec": 317.29999999999836,
        "max_sec": 1805.0,
        "sum_sec": 215736.0,
        "zeros": 0,
        "mean_hms": "0:01:27",
        "median_hms": "0:00:38",
        "p95_hms": "0:05:17",
        "max_hms": "0:30:05",
        "sum_hms": "59:55:36"
      },
      {
        "column": "Talk Time",
        "count": 2465,
        "missing": 10864,
        "mean_sec": 349.9448275862069,
        "median_sec": 286.0,
        "p95_sec": 935.0,
        "max_sec": 2947.0,
        "sum_sec": 862614.0,
        "zeros": 1,
        "mean_hms": "0:05:50",
        "median_hms": "0:04:46",
        "p95_hms": "0:15:35",
        "max_hms": "0:49:07",
        "sum_hms": "239:36:54"
      },
      {
        "column": "Total Call Duration (excl IVR)",
        "count": 13329,
        "missing": 0,
        "mean_sec": 80.90254332658114,
        "median_sec": 0.0,
        "p95_sec": 548.5999999999985,
        "max_sec": 3044.0,
        "sum_sec": 1078350.0,
        "zeros": 10849,
        "mean_hms": "0:01:21",
        "median_hms": "0:00:00",
        "p95_hms": "0:09:09",
        "max_hms": "0:50:44",
        "sum_hms": "299:32:30"
      }
    ],
    "datetime": [
      {
        "column": "Call Time",
        "count": 13329,
        "missing": 0,
        "min": "2025-08-04 00:42:00",
        "max": "2025-08-08 22:56:00",
        "span_seconds": 425640.0
      }
    ],
    "date": [
      {
        "column": "day",
        "count": 13329,
        "missing": 0,
        "min": "2025-04-08",
        "max": "2025-08-08",
        "span_days": 122
      }
    ],
    "binary": [
      {
        "column": "SLA breach",
        "count": 13329,
        "missing": 0,
        "zeros": 12483,
        "ones": 846,
        "share_one": 6.347062795408507
      },
      {
        "column": "Volume",
        "count": 13329,
        "missing": 0,
        "zeros": 10849,
        "ones": 2480,
        "share_one": 18.60604696526371
      },
      {
        "column": "Abandon",
        "count": 13329,
        "missing": 0,
        "zeros": 13197,
        "ones": 132,
        "share_one": 0.9903218546027459
      },
      {
        "column": "Abandon (within 10s)",
        "count": 13329,
        "missing": 0,
        "zeros": 13234,
        "ones": 95,
        "share_one": 0.7127316377822792
      }
    ],
    "identifier": [
      {
        "column": "Call ID",
        "missing": 0,
        "nunique": 3466,
        "unique_ratio": 26.003451121614525,
        "duplicates": 9863
      }
    ],
    "monetary": [
      {
        "column": "Cost",
        "count": 13329.0,
        "mean": 0.04773126266036462,
        "std": 0.7762227020494729,
        "min": 0.0,
        "1%": 0.0,
        "5%": 0.0,
        "25%": 0.0,
        "50%": 0.0,
        "75%": 0.0,
        "95%": 0.0,
        "99%": 0.06,
        "max": 33.79,
        "missing": 0,
        "zeros": 13178,
        "negatives": 0,
        "sum": 636.21
      }
    ]
  }
}
```

## Machine-readable JSON

```json
{
  "dataset": {
    "path": "/Users/evgeniiliashko/repos/scalable_capital/Calls_Data.csv",
    "rows": 13329,
    "columns": 25
  },
  "column_roles": {
    "categorical": [
      "Call Time",
      "Call ID",
      "Direction",
      "Status",
      "Ringing",
      "Talking",
      "Cost",
      "day",
      "week",
      "Hour",
      "Ring time",
      "IVR Time",
      "Wait Time in Queue",
      "Total Waiting Time (queue+ring)",
      "Environment (from Extension)",
      "SLA breach",
      "Volume",
      "Abandon",
      "Abandon (within 10s)",
      "Year",
      "Month",
      "Day",
      "Transfer"
    ],
    "numeric": [
      "Talk Time",
      "Total Call Duration (excl IVR)"
    ]
  },
  "categorical": [
    {
      "name": "Call Time",
      "nunique": 3080,
      "missing": 0,
      "top_counts": [
        {
          "value": "8/4/25 11:56",
          "count": 27
        },
        {
          "value": "8/7/25 16:12",
          "count": 23
        },
        {
          "value": "8/4/25 17:17",
          "count": 20
        },
        {
          "value": "8/7/25 16:13",
          "count": 19
        },
        {
          "value": "8/4/25 9:36",
          "count": 19
        },
        {
          "value": "8/4/25 10:52",
          "count": 17
        },
        {
          "value": "8/4/25 10:14",
          "count": 16
        },
        {
          "value": "8/4/25 10:13",
          "count": 16
        },
        {
          "value": "8/6/25 14:08",
          "count": 16
        },
        {
          "value": "8/4/25 9:32",
          "count": 16
        },
        {
          "value": "8/7/25 9:58",
          "count": 16
        },
        {
          "value": "8/7/25 12:19",
          "count": 16
        },
        {
          "value": "8/7/25 12:46",
          "count": 15
        },
        {
          "value": "8/4/25 17:16",
          "count": 15
        },
        {
          "value": "8/7/25 16:06",
          "count": 15
        },
        {
          "value": "8/4/25 15:13",
          "count": 15
        },
        {
          "value": "8/7/25 16:01",
          "count": 15
        },
        {
          "value": "8/4/25 13:02",
          "count": 15
        },
        {
          "value": "8/5/25 11:16",
          "count": 15
        },
        {
          "value": "8/7/25 15:53",
          "count": 15
        }
      ],
      "values_truncated": true,
      "top_counts_shown": 20
    },
    {
      "name": "Call ID",
      "nunique": 3466,
      "missing": 0,
      "top_counts": [
        {
          "value": "00000000-01dc-050f-6bfc-186200001b17",
          "count": 15
        },
        {
          "value": "00000000-01dc-0858-b798-59ae0000280d",
          "count": 13
        },
        {
          "value": "00000000-01dc-0857-662b-bec800002802",
          "count": 12
        },
        {
          "value": "00000000-01dc-055d-5c76-119300001e60",
          "count": 12
        },
        {
          "value": "00000000-01dc-052b-6c48-fd8f00001c63",
          "count": 11
        },
        {
          "value": "00000000-01dc-06df-c91e-1d640000234e",
          "count": 11
        },
        {
          "value": "00000000-01dc-051a-9916-84ce00001b97",
          "count": 11
        },
        {
          "value": "00000000-01dc-078c-2845-dbf600002567",
          "count": 11
        },
        {
          "value": "00000000-01dc-0511-d15a-362100001b32",
          "count": 11
        },
        {
          "value": "00000000-01dc-06ab-e437-7394000021d7",
          "count": 11
        },
        {
          "value": "00000000-01dc-0869-14c6-203400002878",
          "count": 11
        },
        {
          "value": "00000000-01dc-0784-4436-dc3900002500",
          "count": 10
        },
        {
          "value": "00000000-01dc-06df-3f03-427200002347",
          "count": 10
        },
        {
          "value": "00000000-01dc-07bb-6e20-c4a7000026b5",
          "count": 10
        },
        {
          "value": "00000000-01dc-06ab-1cb9-a9f1000021d5",
          "count": 10
        },
        {
          "value": "00000000-01dc-0517-2219-8ab700001b73",
          "count": 10
        },
        {
          "value": "00000000-01dc-06b0-02de-336c000021fb",
          "count": 10
        },
        {
          "value": "00000000-01dc-054d-1161-e36900001dcf",
          "count": 10
        },
        {
          "value": "00000000-01dc-05e6-0054-15fc00001f50",
          "count": 10
        },
        {
          "value": "00000000-01dc-07af-ecc3-63ef0000268f",
          "count": 10
        }
      ],
      "values_truncated": true,
      "top_counts_shown": 20
    },
    {
      "name": "Direction",
      "nunique": 4,
      "missing": 0,
      "values": [
        "Inbound",
        "Inbound Queue",
        "Internal",
        "Outbound"
      ],
      "values_truncated": false
    },
    {
      "name": "Status",
      "nunique": 3,
      "missing": 0,
      "values": [
        "Answered",
        "Unanswered",
        "Waiting"
      ],
      "values_truncated": false
    },
    {
      "name": "Ringing",
      "nunique": 49,
      "missing": 0,
      "values": [
        "0:00:00",
        "0:00:01",
        "0:00:02",
        "0:00:03",
        "0:00:04",
        "0:00:05",
        "0:00:06",
        "0:00:07",
        "0:00:08",
        "0:00:09",
        "0:00:10",
        "0:00:11",
        "0:00:12",
        "0:00:13",
        "0:00:14",
        "0:00:15",
        "0:00:16",
        "0:00:17",
        "0:00:18",
        "0:00:19",
        "0:00:20",
        "0:00:21",
        "0:00:22",
        "0:00:23",
        "0:00:24",
        "0:00:25",
        "0:00:26",
        "0:00:27",
        "0:00:28",
        "0:00:31",
        "0:00:32",
        "0:00:33",
        "0:00:34",
        "0:00:37",
        "0:00:38",
        "0:00:39",
        "0:00:41",
        "0:00:42",
        "0:00:46",
        "0:00:47",
        "0:00:49",
        "0:00:50",
        "0:00:51",
        "0:00:54",
        "0:00:56",
        "0:00:59",
        "0:01:01",
        "0:01:18",
        "0:03:00"
      ],
      "values_truncated": false
    },
    {
      "name": "Talking",
      "nunique": 984,
      "missing": 0,
      "top_counts": [
        {
          "value": "0:00:12",
          "count": 418
        },
        {
          "value": "0:00:13",
          "count": 413
        },
        {
          "value": "0:00:16",
          "count": 408
        },
        {
          "value": "0:00:17",
          "count": 365
        },
        {
          "value": "0:00:15",
          "count": 357
        },
        {
          "value": "0:00:23",
          "count": 354
        },
        {
          "value": "0:00:11",
          "count": 348
        },
        {
          "value": "0:00:18",
          "count": 340
        },
        {
          "value": "0:00:24",
          "count": 316
        },
        {
          "value": "0:00:14",
          "count": 314
        },
        {
          "value": "0:00:30",
          "count": 308
        },
        {
          "value": "0:00:25",
          "count": 300
        },
        {
          "value": "0:00:29",
          "count": 297
        },
        {
          "value": "0:00:31",
          "count": 297
        },
        {
          "value": "0:00:22",
          "count": 275
        },
        {
          "value": "0:00:19",
          "count": 260
        },
        {
          "value": "0:00:33",
          "count": 253
        },
        {
          "value": "0:00:21",
          "count": 250
        },
        {
          "value": "0:00:32",
          "count": 246
        },
        {
          "value": "0:00:20",
          "count": 221
        }
      ],
      "values_truncated": true,
      "top_counts_shown": 20
    },
    {
      "name": "Cost",
      "nunique": 126,
      "missing": 0,
      "top_counts": [
        {
          "value": 0.0,
          "count": 13178
        },
        {
          "value": 0.06,
          "count": 8
        },
        {
          "value": 0.05,
          "count": 4
        },
        {
          "value": 0.03,
          "count": 4
        },
        {
          "value": 0.04,
          "count": 3
        },
        {
          "value": 0.07,
          "count": 3
        },
        {
          "value": 0.77,
          "count": 2
        },
        {
          "value": 0.02,
          "count": 2
        },
        {
          "value": 2.55,
          "count": 2
        },
        {
          "value": 0.12,
          "count": 2
        },
        {
          "value": 1.55,
          "count": 2
        },
        {
          "value": 0.55,
          "count": 2
        },
        {
          "value": 0.16,
          "count": 2
        },
        {
          "value": 1.31,
          "count": 2
        },
        {
          "value": 0.38,
          "count": 2
        },
        {
          "value": 5.71,
          "count": 1
        },
        {
          "value": 2.14,
          "count": 1
        },
        {
          "value": 6.93,
          "count": 1
        },
        {
          "value": 3.82,
          "count": 1
        },
        {
          "value": 15.27,
          "count": 1
        }
      ],
      "values_truncated": true,
      "top_counts_shown": 20
    },
    {
      "name": "day",
      "nunique": 5,
      "missing": 0,
      "values": [
        "4/8/25",
        "5/8/25",
        "6/8/25",
        "7/8/25",
        "8/8/25"
      ],
      "values_truncated": false
    },
    {
      "name": "week",
      "nunique": 1,
      "missing": 0,
      "values": [
        32
      ],
      "values_truncated": false
    },
    {
      "name": "Hour",
      "nunique": 19,
      "missing": 0,
      "values": [
        0,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22
      ],
      "values_truncated": false
    },
    {
      "name": "Ring time",
      "nunique": 49,
      "missing": 0,
      "values": [
        0,
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
        26,
        27,
        28,
        31,
        32,
        33,
        34,
        37,
        38,
        39,
        41,
        42,
        46,
        47,
        49,
        50,
        51,
        54,
        56,
        59,
        61,
        78,
        180
      ],
      "values_truncated": false
    },
    {
      "name": "IVR Time",
      "nunique": 0,
      "missing": 13329,
      "values": [],
      "values_truncated": false
    },
    {
      "name": "Wait Time in Queue",
      "nunique": 371,
      "missing": 10849,
      "top_counts": [
        {
          "value": 29.0,
          "count": 149
        },
        {
          "value": 30.0,
          "count": 142
        },
        {
          "value": 31.0,
          "count": 132
        },
        {
          "value": 32.0,
          "count": 101
        },
        {
          "value": 33.0,
          "count": 90
        },
        {
          "value": 28.0,
          "count": 90
        },
        {
          "value": 34.0,
          "count": 81
        },
        {
          "value": 35.0,
          "count": 75
        },
        {
          "value": 27.0,
          "count": 68
        },
        {
          "value": 36.0,
          "count": 56
        },
        {
          "value": 49.0,
          "count": 52
        },
        {
          "value": 26.0,
          "count": 51
        },
        {
          "value": 39.0,
          "count": 51
        },
        {
          "value": 37.0,
          "count": 48
        },
        {
          "value": 50.0,
          "count": 48
        },
        {
          "value": 25.0,
          "count": 44
        },
        {
          "value": 51.0,
          "count": 42
        },
        {
          "value": 48.0,
          "count": 41
        },
        {
          "value": 38.0,
          "count": 40
        },
        {
          "value": 46.0,
          "count": 37
        }
      ],
      "values_truncated": true,
      "top_counts_shown": 20
    },
    {
      "name": "Total Waiting Time (queue+ring)",
      "nunique": 371,
      "missing": 10849,
      "top_counts": [
        {
          "value": 29.0,
          "count": 149
        },
        {
          "value": 30.0,
          "count": 142
        },
        {
          "value": 31.0,
          "count": 132
        },
        {
          "value": 32.0,
          "count": 101
        },
        {
          "value": 33.0,
          "count": 90
        },
        {
          "value": 28.0,
          "count": 90
        },
        {
          "value": 34.0,
          "count": 81
        },
        {
          "value": 35.0,
          "count": 75
        },
        {
          "value": 27.0,
          "count": 68
        },
        {
          "value": 36.0,
          "count": 56
        },
        {
          "value": 49.0,
          "count": 52
        },
        {
          "value": 26.0,
          "count": 51
        },
        {
          "value": 39.0,
          "count": 51
        },
        {
          "value": 37.0,
          "count": 48
        },
        {
          "value": 50.0,
          "count": 48
        },
        {
          "value": 25.0,
          "count": 44
        },
        {
          "value": 51.0,
          "count": 42
        },
        {
          "value": 48.0,
          "count": 41
        },
        {
          "value": 38.0,
          "count": 40
        },
        {
          "value": 46.0,
          "count": 37
        }
      ],
      "values_truncated": true,
      "top_counts_shown": 20
    },
    {
      "name": "Environment (from Extension)",
      "nunique": 4,
      "missing": 12948,
      "values": [
        "DE/AT B2B",
        "DE/AT Broker",
        "DE/AT Fraud and 3PM",
        "DE/AT Wealth"
      ],
      "values_truncated": false
    },
    {
      "name": "SLA breach",
      "nunique": 2,
      "missing": 0,
      "values": [
        0,
        1
      ],
      "values_truncated": false
    },
    {
      "name": "Volume",
      "nunique": 2,
      "missing": 0,
      "values": [
        0,
        1
      ],
      "values_truncated": false
    },
    {
      "name": "Abandon",
      "nunique": 2,
      "missing": 0,
      "values": [
        0,
        1
      ],
      "values_truncated": false
    },
    {
      "name": "Abandon (within 10s)",
      "nunique": 2,
      "missing": 0,
      "values": [
        0,
        1
      ],
      "values_truncated": false
    },
    {
      "name": "Year",
      "nunique": 1,
      "missing": 0,
      "values": [
        2025
      ],
      "values_truncated": false
    },
    {
      "name": "Month",
      "nunique": 1,
      "missing": 0,
      "values": [
        8
      ],
      "values_truncated": false
    },
    {
      "name": "Day",
      "nunique": 5,
      "missing": 0,
      "values": [
        4,
        5,
        6,
        7,
        8
      ],
      "values_truncated": false
    },
    {
      "name": "Transfer",
      "nunique": 1,
      "missing": 0,
      "values": [
        0
      ],
      "values_truncated": false
    }
  ],
  "numeric": [
    {
      "name": "Talk Time",
      "stats": {
        "count": 2465.0,
        "mean": 349.9448275862069,
        "std": 311.1534015962211,
        "min": 0.0,
        "1%": 14.64,
        "5%": 32.0,
        "25%": 121.0,
        "50%": 286.0,
        "75%": 470.0,
        "95%": 935.0,
        "99%": 1446.760000000002,
        "max": 2947.0,
        "missing": 10864.0,
        "zeros": 1.0,
        "negatives": 0.0,
        "unique_pct": 6.482106684672519
      }
    },
    {
      "name": "Total Call Duration (excl IVR)",
      "stats": {
        "count": 13329.0,
        "mean": 80.90254332658114,
        "std": 224.9242727045355,
        "min": 0.0,
        "1%": 0.0,
        "5%": 0.0,
        "25%": 0.0,
        "50%": 0.0,
        "75%": 0.0,
        "95%": 548.5999999999985,
        "99%": 1056.5999999999967,
        "max": 3044.0,
        "missing": 0.0,
        "zeros": 10849.0,
        "negatives": 0.0,
        "unique_pct": 7.1198139395303475
      }
    }
  ]
}
```
