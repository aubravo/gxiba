""" Collection of queries for SQL & Google Cloud BigQuery """

""" ========== BIG QUERY ========== """
landsat_bigquery = """
SELECT product_id, sensing_time, north_lat, south_lat, west_lon, east_lon, base_url
FROM bigquery-public-data.cloud_storage_geo_index.landsat_index
WHERE
spacecraft_id = "LANDSAT_8" AND
north_lat > 19.023463 AND
south_lat < 19.023463 AND
east_lon > -98.622686 AND
west_lon < -98.622686 AND
date_acquired >= "{}"
ORDER BY sensing_time ASC;
"""

sentinel_bigquery = """
SELECT granule_id, sensing_time, north_lat, south_lat, west_lon, east_lon, base_url
FROM bigquery-public-data.cloud_storage_geo_index.sentinel_2_index
WHERE
granule_id LIKE "L1C%" AND
north_lat > 19.023463 AND
south_lat < 19.023463 AND
east_lon > -98.622686 AND
west_lon < -98.622686 AND
sensing_time >= "{}"
ORDER BY sensing_time ASC;
"""

""" ========== SQL ========== """
initial_setup = """
CREATE SCHEMA gxiba;
CREATE TABLE IF NOT EXISTS gxiba.landsat (
    id TEXT PRIMARY KEY,
    sensing_time TIMESTAMP,
    north_lat NUMERIC,
    south_lat NUMERIC,
    west_lon NUMERIC,
    east_lon NUMERIC,
    status TEXT,
    base_url TEXT
);
CREATE TABLE IF NOT EXISTS gxiba.sentinel (
    id TEXT PRIMARY KEY,
    product TEXT,
    sensing_time TIMESTAMP,
    north_lat NUMERIC,
    south_lat NUMERIC,
    west_lon NUMERIC,
    east_lon NUMERIC,
    status TEXT,
    base_url TEXT
);
"""

platform_insert = """
INSERT INTO gxiba.%(platform)s (id, sensing_time, north_lat, south_lat, west_lon, east_lon, base_url, status)
VALUES (%(id)s, %(sensing_time)s, %(north_lat)s, %(south_lat)s, %(west_lon)s, %(east_lon)s, %(base_url)s, %(status)s);
"""

get_most_recent_date = """
SELECT sensing_time FROM gxiba.{}
ORDER BY sensing_time DESC
LIMIT 1;
"""

get_by_status = """
SELECT id, base_url
FROM gxiba.{}
WHERE
status LIKE '{}'
"""

get_one_by_status = """
SELECT id, base_url
FROM gxiba.{}
WHERE
status LIKE '{}'
ORDER BY RANDOM()
LIMIT 1;
"""

get_count_by_status = """
SELECT COUNT(*)
FROM gxiba.{}
WHERE
status LIKE '{}'
"""

change_status_by_id = """
UPDATE gxiba.{}
SET status = '{}'
WHERE id = '{}'
"""