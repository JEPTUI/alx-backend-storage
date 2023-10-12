-- ranks country origins of bands
-- ordered by the number of (non-unique) fans
SELECT origin, SUM(nb_fans) AS nb_fans
FROM bands
GROUP BY origin
ORDER BY nb_fans DESC;
