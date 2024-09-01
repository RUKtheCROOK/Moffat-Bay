-- Begin transaction
START TRANSACTION;

DROP TABLE IF EXISTS ReservationAmenity;
DROP TABLE IF EXISTS Reservation;
DROP TABLE IF EXISTS Amenity;
DROP TABLE IF EXISTS RoomType;
DROP TABLE IF EXISTS PasswordResetRequest;
DROP TABLE IF EXISTS Session;
DROP TABLE IF EXISTS User;

-- Commit the transaction to finalize the rollback
COMMIT;
