SELECT 
    sensor_id,
    ROUND(AVG(CAST(temperature_c AS DOUBLE)), 1) as avg_temp,
    ROUND(AVG(CAST(vibration_ms2 AS DOUBLE)), 3) as avg_vibration,
    ROUND(AVG(CAST(power_kw AS DOUBLE)), 2) as avg_power
FROM hvac_final
GROUP BY sensor_id
ORDER BY sensor_id;
