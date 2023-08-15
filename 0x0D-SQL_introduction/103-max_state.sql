-- displays the max temperature of each state (ordered by State name).
SELECT state, MAX(value) from temperatures
GROUP BY state ORDER BY state;
