SELECT 
    timestamp_col,
    sensor_id,
    CAST(temperature_c AS DOUBLE) as temp_c,
    CAST(power_kw AS DOUBLE) as power_kw
FROM hvac_final
WHERE CAST(temperature_c AS DOUBLE) > 35
ORDER BY CAST(temperature_c AS DOUBLE) DESC
LIMIT 20;
