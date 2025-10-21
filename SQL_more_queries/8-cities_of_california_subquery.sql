-- Write a script that lists all the cities of California that can be found
-- in the database hbtn_0d_usa.
SELECT cities_id, cities_name
FROM cities, statesWHERE cities.states_id= states.id AND states.name = 'California'
ORDER BY cities_id ASC;
