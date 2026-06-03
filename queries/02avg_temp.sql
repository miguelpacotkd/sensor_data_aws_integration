SELECT 
    sensor_id,
    AVG(CAST(temperature_c AS DOUBLE)) as avg_temp_c,
    COUNT(*) as readings
FROM hvac_final
WHERE temperature_c IS NOT NULL
GROUP BY sensor_id
ORDER BY sensor_id;
