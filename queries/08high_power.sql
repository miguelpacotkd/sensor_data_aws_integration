SELECT 
    timestamp_col,
    sensor_id,
    CAST(power_kw AS DOUBLE) as power_kw,
    CAST(temperature_c AS DOUBLE) as temp_c
FROM hvac_final
WHERE CAST(power_kw AS DOUBLE) > 2.5
ORDER BY CAST(power_kw AS DOUBLE) DESC
LIMIT 15;
