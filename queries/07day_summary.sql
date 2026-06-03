SELECT 
    DATE(CAST(timestamp_col AS TIMESTAMP)) as day,
    ROUND(MIN(CAST(temperature_c AS DOUBLE)), 1) as min_temp,
    ROUND(MAX(CAST(temperature_c AS DOUBLE)), 1) as max_temp,
    ROUND(AVG(CAST(temperature_c AS DOUBLE)), 1) as avg_temp
FROM hvac_final
WHERE timestamp_col IS NOT NULL
GROUP BY DATE(CAST(timestamp_col AS TIMESTAMP))
ORDER BY day;
