USE call_a_cab;
-- 1. How many Mini, Premier, XL cabs?
SELECT Model, count(*) as Number FROM call_a_cab.cab group by Model;

-- 2. List the top rated drivers ?
SELECT Driver_ID,Rating FROM driver WHERE Rating IN (4,5) AND Status='Available';

-- 3. Retrieve the details of late night rides (to verify if people consider the app safe)
SELECT Ride_ID, Dropoff_Time FROM ride WHERE Dropoff_Time BETWEEN '00:00:00' AND '06:00:00';

-- 4. Update status of cab availibility
UPDATE driver SET Status= 'Busy' WHERE Driver_ID='14306';

-- 5. Customer aborts ride request
DELETE FROM ride_request WHERE Request_ID='10693';

-- 6. Retrieve number of transactions for each payment mode
SELECT Payment_Mode, count(*) as Number FROM call_a_cab.payments group by Payment_Mode;

-- 7. How many trips were of amount > 4000 ?
SELECT Date, Ride_ID,Amount,Payment_Mode FROM payments WHERE Amount>4000;

-- 8. Viewing drivers in a locality  
SELECT SUBSTR(Location, -2) AS last_two_letters, COUNT(*) AS count FROM driver GROUP BY last_two_letters;

-- 9. Viewing passengers in a locality  
SELECT SUBSTR(Location, -2) AS last_two_letters, COUNT(*) AS count FROM passenger_account GROUP BY last_two_letters;

-- 10. Creating a new passenger account
INSERT INTO `passenger_account` (`Passenger_ID`, `Email`, `Password`, `Name`, `Location`) VALUES (4, 'lamarmclaughlin@example.net', 'b6b8b2b65426508b41c880914580d', 'Marnus Wayne', '6 Downing Street\nSouth Manhattan, NY 63297');

-- 11. Display the total number of users
SELECT COUNT(passenger_ID) FROM passenger_account;

-- 12. To access passenger details for a ride request
SELECT passenger_account.passenger_id
FROM passenger_account 
JOIN ride_request ON passenger_account.passenger_id = ride_request.passenger_id 
WHERE ride_request.request_id = 10693;

-- 13. To check request details for an ongoing ride
SELECT ride_request.request_id
FROM ride_request 
JOIN ride ON ride_request.request_id = ride.request_id 
WHERE ride.ride_id = 10124;

-- 14. Update driver rating
UPDATE driver SET Rating= '3' WHERE Driver_ID='10000';







-- what is total money received through each payment mode
-- which region has most riders
-- what was the average cost of a ride
-- what is the avg rating of a driver