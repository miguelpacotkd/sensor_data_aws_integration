#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from datetime import datetime, timedelta


n_days = 7
interval_minutes = 15
n_sensors = 5
start_time = datetime(2025, 5, 1, 0, 0, 0)


intervals_per_day = 24 * 60 // interval_minutes
total_intervals = n_days * intervals_per_day
total_rows = total_intervals * n_sensors


timestamps = []
for day in range(n_days):
    for interval in range(intervals_per_day):
        ts = start_time + timedelta(days=day, minutes=interval * interval_minutes)
        timestamps.extend([ts] * n_sensors)


sensor_ids = list(range(1, n_sensors + 1)) * total_intervals


simulation_runs = []
run_counter = 1
days_into_sim = 0
for idx in range(len(timestamps)):
    if idx > 0 and timestamps[idx].day != timestamps[idx-1].day:
        days_into_sim += 1
    if days_into_sim >= 2:
        days_into_sim = 0
        run_counter += 1
    simulation_runs.append(f"run_{run_counter:03d}")


np.random.seed(42)  # reproducible, line can be commented out for different data each run


hour_of_day = np.array([ts.hour for ts in timestamps])
time_factor = 5 * np.sin(np.pi * (hour_of_day - 6) / 12) 


sensor_baseline = {1: 22.0, 2: 23.5, 3: 21.0, 4: 22.5, 5: 20.5}
base_temp = np.array([sensor_baseline[sid] for sid in sensor_ids])


temperature_c = base_temp + time_factor + np.random.normal(0, 0.5, total_rows)

humidity_pct = 60 - 0.5 * (temperature_c - 22) + np.random.normal(0, 3, total_rows)
humidity_pct = np.clip(humidity_pct, 30, 80)

pressure_hpa = 1013 + 2 * np.sin(np.pi * hour_of_day / 12) + np.cumsum(np.random.normal(0, 0.02, total_rows))
pressure_hpa = np.clip(pressure_hpa, 1005, 1025)

vibration_ms2 = 0.1 + 0.05 * np.abs(np.gradient(temperature_c)) + np.random.exponential(0.05, total_rows)
vibration_ms2 = np.clip(vibration_ms2, 0.05, 0.5)

power_kw = 1.5 + 0.15 * (temperature_c - 22) + np.random.normal(0, 0.2, total_rows)
power_kw = np.clip(power_kw, 0.8, 3.5)

df = pd.DataFrame({
    'timestamp': timestamps,
    'sensor_id': sensor_ids,
    'temperature_c': np.round(temperature_c, 1),
    'humidity_pct': np.round(humidity_pct, 1),
    'pressure_hpa': np.round(pressure_hpa, 1),
    'vibration_ms2': np.round(vibration_ms2, 3),
    'power_kw': np.round(power_kw, 2),
    'simulation_run': simulation_runs
})

# Add some anomalies (2% of rows)
anomaly_indices = np.random.choice(df.index, size=int(0.02 * len(df)), replace=False)
df.loc[anomaly_indices, 'temperature_c'] = df.loc[anomaly_indices, 'temperature_c'] + np.random.uniform(8, 15, len(anomaly_indices))
df.loc[anomaly_indices, 'vibration_ms2'] = df.loc[anomaly_indices, 'vibration_ms2'] + np.random.uniform(0.3, 0.8, len(anomaly_indices))

df = df.sort_values(['timestamp', 'sensor_id'])

df.to_csv('hvac_sensor_data.csv', index=False)
print(f"Saved {len(df):,} rows to hvac_sensor_data.csv")
print("\nSample data:")
print(df.head(10))
print("\nColumn stats:")
print(df.describe())


# In[ ]:




