## EDA Summary for `calls_normalized.csv`

- **rows**: 3466
- **columns**: 24

| Column | Format | Unique | Sample unique values |
| - | - | -: | - |
| call_id | string | 3466 | 00000000-01dc-04c7-d629-df1700001aa5, 00000000-01dc-04fc-50e9-939400001aa6, 00000000-01dc-04fe-cac3-009300001aa7, 00000000-01dc-04fe-f6a4-4da000001aa8, 00000000-01dc-0501-6f1a-db8900001aa9, 00000000-01dc-0501-900f-9cb100001aaa, 00000000-01dc-0502-a26f-edd100001aab, 00000000-01dc-0503-c383-542b00001aac, 00000000-01dc-0503-d488-53f400001aad, 00000000-01dc-0504-7ff8-839200001aae |
| call_start_time | datetime-like string | 2109 | 8/4/25 0:42, 8/4/25 10:01, 8/4/25 10:02, 8/4/25 10:04, 8/4/25 10:06, 8/4/25 10:08, 8/4/25 10:09, 8/4/25 10:11, 8/4/25 10:12, 8/4/25 10:13 |
| Direction | string | 2 | Inbound, Outbound |
| outside_working_hours | int | 2 | 0, 1 |
| first_agent_answer_time | datetime-like string | 1665 | 8/4/25 10:02, 8/4/25 10:03, 8/4/25 10:04, 8/4/25 10:05, 8/4/25 10:06, 8/4/25 10:07, 8/4/25 10:08, 8/4/25 10:09, 8/4/25 10:10, 8/4/25 10:12 |
| Outbound_call_answered | int | 2 | 0, 1 |
| agent_answered_after_queue | int | 2 | 0, 1 |
| total_queue_unanswered | int | 100 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 |
| total_IVR | int | 131 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 |
| total_queue_wait | int | 388 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 10 |
| total_ring | int | 51 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 |
| total_talk | int | 913 | 0, 1, 2, 3, 4, 5, 6, 7, 9, 10 |
| total_call_duration (excl. IVR) | int | 1009 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 |
| total_call_duration (incl. IVR) | int | 1063 | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 |
| cost_sum | float | 125 | 0, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.1, 0.11 |
| sla_breach | int | 2 | 0, 1 |
| abandon | int | 2 | 0, 1 |
| abandon_within_10s | int | 2 | 0, 1 |
| environment | string | 4 | DE/AT B2B, DE/AT Broker, DE/AT Fraud and 3PM, DE/AT Wealth |
| start_day | datetime-like string | 5 | 8/4/25, 8/5/25, 8/6/25, 8/7/25, 8/8/25 |
| week | int | 1 | 32 |
| start_hour | int | 19 | 0, 5, 6, 7, 8, 9, 10, 11, 12, 13 |
| month | int | 1 | 8 |
| year | int | 1 | 2025 |
