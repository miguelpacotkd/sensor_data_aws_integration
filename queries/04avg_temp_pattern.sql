SELECT 
    HOUR(CAST(timestamp_col AS TIMESTAMP)) as hour_of_day,
    ROUND(AVG(CAST(temperature_c AS DOUBLE)), 1) as avg_temp,
    ROUND(AVG(CAST(power_kw AS DOUBLE)), 2) as avg_power
FROM hvac_final
WHERE timestamp_col IS NOT NULL
GROUP BY HOUR(CAST(timestamp_col AS TIMESTAMP))
ORDER BY hour_of_day;
