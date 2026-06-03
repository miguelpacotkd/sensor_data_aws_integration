SELECT 
    simulation_run,
    ROUND(AVG(CAST(temperature_c AS DOUBLE)), 1) as avg_temp,
    ROUND(AVG(CAST(power_kw AS DOUBLE)), 2) as avg_power,
    COUNT(*) as total_readings,
    SUM(CASE WHEN CAST(temperature_c AS DOUBLE) > 35 THEN 1 ELSE 0 END) as anomaly_count
FROM hvac_final
GROUP BY simulation_run
ORDER BY simulation_run;
