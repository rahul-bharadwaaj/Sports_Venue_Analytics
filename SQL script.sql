-- Ranking Venues by Capacity within Each Country 
SELECT Country,City,Venue,Capacity,
DENSE_RANK() OVER(PARTITION BY Country ORDER BY Capacity DESC) AS Capacity_Rank
FROM sports_venue

-- Average Capacity by Sport and Country
SELECT Sport,Country,
AVG(Capacity) AS Average_Capacity,
COUNT(*) AS No_of_Venues
FROM sports_venue
GROUP BY Sport,Country;

--  Relationship between venue capacity and the number of venues a sport has in each country.
SELECT Sport, Country,
AVG(Capacity) AS Average_Capacity,
SUM(Capacity) AS Total_Capacity,
COUNT(*) AS No_of_Venues,
AVG(Capacity) * COUNT(*) AS Capacity_Venue_Score
FROM sports_venue
GROUP BY Sport, Country
ORDER BY Capacity_Venue_Score DESC;

-- Diversity of Sports Venue Sizes within Countries
SELECT Sport, Country,
AVG(Capacity) AS Average_Capacity,
MAX(Capacity) - MIN(Capacity) AS Capacity_Range,
STDEV(Capacity) AS Capacity_StdDev,
COUNT(*) AS No_of_Venues
FROM sports_venue
GROUP BY Sport, Country
ORDER BY Capacity_StdDev DESC;