SELECT
  COUNT(DISTINCT company_id)
FROM (
  SELECT
    company_id, -- Added comma
    ROW_NUMBER() OVER ( -- Corrected function name
      PARTITION BY
        title,
        description
      ORDER BY
        post_date
    ) AS post_num
  FROM
    job_listing
) t -- Added subquery alias
WHERE
  post_num = 2;
