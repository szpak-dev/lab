SELECT
    tablename,
    indexname,
    indexdef
FROM
    pg_indexes
WHERE
    schemaname = 'rentals'
ORDER BY
    tablename,
    indexname;