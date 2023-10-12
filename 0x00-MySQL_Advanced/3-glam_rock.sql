-- lists all bands with Glam rock as their main style
-- ranked by their longevity
SELECT
    band_name,
    CASE
        WHEN split = 'present' THEN (2022 - YEAR(formed))
        ELSE (YEAR(split) - YEAR(formed))
    END AS lifespan
FROM
    bands
WHERE
    style LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;
