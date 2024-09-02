-- Begin transaction to allow rollback if needed
START TRANSACTION;

SET foreign_key_checks = 0;
DROP TABLE IF EXISTS ReservationAmenity;
DROP TABLE IF EXISTS Reservation;
DROP TABLE IF EXISTS Amenity;
DROP TABLE IF EXISTS RoomType;
DROP TABLE IF EXISTS PasswordResetRequest;
DROP TABLE IF EXISTS Session;
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Attractions;
DROP TABLE IF EXISTS ReservationAttraction;
DROP PROCEDURE IF EXISTS spLogin;

-- ====================================================================================================================
-- 													Setup Tables
-- ====================================================================================================================
CREATE TABLE User (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(20),
    PasswordHash VARCHAR(255) NOT NULL,
    Salt VARCHAR(255) NOT NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE RoomType (
    RoomTypeID INT AUTO_INCREMENT PRIMARY KEY,
    RoomTypeName ENUM('Double Full Beds', 'Queen', 'Double Queen Beds', 'King') NOT NULL,
    BasePrice DECIMAL(10, 2) NOT NULL,
    MaxGuests TINYINT NOT NULL
);

CREATE TABLE Reservation (
    ReservationID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT,
    Email VARCHAR(255) NOT NULL,
    RoomType ENUM('Double Full Beds', 'Queen', 'Double Queen Beds', 'King') NOT NULL,
    NumberOfGuests TINYINT NOT NULL,
    CheckInDate DATE NOT NULL,
    CheckOutDate DATE NOT NULL,
    TotalPrice DECIMAL(10, 2) NOT NULL,
    ReservationStatus ENUM('Confirmed', 'Canceled') DEFAULT 'Confirmed',
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (UserID) REFERENCES User(UserID) ON DELETE SET NULL
);

CREATE TABLE Amenity (
    AmenityID INT AUTO_INCREMENT PRIMARY KEY,
    AmenityName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE ReservationAmenity (
    ReservationAmenityID INT AUTO_INCREMENT PRIMARY KEY,
    ReservationID INT NOT NULL,
    AmenityID INT NOT NULL,
    Quantity TINYINT NOT NULL,
    TotalPrice DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (ReservationID) REFERENCES Reservation(ReservationID) ON DELETE CASCADE,
    FOREIGN KEY (AmenityID) REFERENCES Amenity(AmenityID) ON DELETE CASCADE
);

CREATE TABLE Attractions (
    AttractionID INT AUTO_INCREMENT PRIMARY KEY,
    AttractionName VARCHAR(255) NOT NULL,
    Description TEXT,
    Price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE ReservationAttraction (
    ReservationAttractionID INT AUTO_INCREMENT PRIMARY KEY,
    ReservationID INT NOT NULL,
    AttractionID INT NOT NULL,
    Quantity TINYINT NOT NULL,
    TotalPrice DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (ReservationID) REFERENCES Reservation(ReservationID) ON DELETE CASCADE,
    FOREIGN KEY (AttractionID) REFERENCES Attractions(AttractionID) ON DELETE CASCADE
);

CREATE TABLE Session (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    SessionToken VARCHAR(255) UNIQUE NOT NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    ExpiresAt DATETIME,
    FOREIGN KEY (UserID) REFERENCES User(UserID) ON DELETE CASCADE
);

CREATE TABLE PasswordResetRequest (
    ResetRequestID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    ResetToken VARCHAR(255) UNIQUE NOT NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    ExpiresAt DATETIME,
    Used BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (UserID) REFERENCES User(UserID) ON DELETE CASCADE
);

-- Create some salts for the test users
SET @var_salt1 = LEFT(REPLACE(UUID(), '-', ''), 16);
SET @var_salt2 = LEFT(REPLACE(UUID(), '-', ''), 16);
SET @var_salt3 = LEFT(REPLACE(UUID(), '-', ''), 16);

INSERT INTO User (FirstName, LastName, Email, PhoneNumber, PasswordHash, Salt)
VALUES 
('John', 'Doe', 'test1@email.com', '1234567890', SHA2(CONCAT('password1', @var_salt1), 256), @var_salt1),
('Jane', 'Smith', 'test2@email.com', '0987654321', SHA2(CONCAT('password2', @var_salt1), 256), @var_salt2),
('Alice', 'Johnson', 'test3@email.com', '1122334455', SHA2(CONCAT('password3', @var_salt1), 256), @var_salt3); 

INSERT INTO RoomType (RoomTypeName, BasePrice, MaxGuests)
VALUES 
('Double Full Beds', 115.00, 2),
('Queen', 115.00, 2),
('King', 150.00, 5);

INSERT INTO Reservation (UserID, Email, RoomType, NumberOfGuests, CheckInDate, CheckOutDate, TotalPrice, ReservationStatus)
VALUES 
(1, 'test1@email.com', 'Queen', 2, '2024-09-01', '2024-09-07', 805.00, 'Confirmed'),
(2, 'test2@email.com', 'King', 3, '2024-09-10', '2024-09-14', 600.00, 'Confirmed'),
(3, 'test3@email.com', 'Double Full Beds', 1, '2024-09-15', '2024-09-18', 345.00, 'Canceled');

INSERT INTO Attractions (AttractionName, Description, Price)
VALUES 
('Kayaking', 'Enjoy a scenic kayak ride', 50.00),
('Whale Watching', 'Observe the magnificent whales', 75.00),
('Scuba Diving', 'Explore the underwater world', 100.00);

INSERT INTO ReservationAttraction (ReservationID, AttractionID, Quantity, TotalPrice)
VALUES 
(1, 1, 2, 100.00),
(2, 2, 1, 75.00),
(3, 3, 1, 100.00);

INSERT INTO Amenity (AmenityName, Description, Price)
VALUES 
('Breakfast', 'Delicious breakfast options', 50.00),
('Pool Access', 'Access to use the private pool', 75.00),
('Room Service', 'Convenient room service options', 100.00);

INSERT INTO ReservationAmenity (ReservationID, AmenityID, Quantity, TotalPrice)
VALUES 
(1, 1, 1, 50.00),
(2, 2, 2, 150.00),
(3, 3, 1, 100.00);

INSERT INTO Session (UserID, SessionToken, ExpiresAt)
VALUES 
(1, 'session_token_1', '2024-09-01 23:59:59'),
(2, 'session_token_2', '2024-09-02 23:59:59'),
(3, 'session_token_3', '2024-09-03 23:59:59');

INSERT INTO PasswordResetRequest (UserID, ResetToken, ExpiresAt)
VALUES 
(1, 'reset_token_1', '2024-09-01 23:59:59'),
(2, 'reset_token_2', '2024-09-02 23:59:59'),
(3, 'reset_token_3', '2024-09-03 23:59:59');

SET foreign_key_checks = 1;



-- ====================================================================================================================
--												Setup Stored Procedures
-- ====================================================================================================================
DELIMITER $$

CREATE PROCEDURE spLogin(
-- =============================================
-- Author:      Drew Bach
-- Create Date: 09/02/2024
-- Description: Verify the users email and password match what we have in the database and return a session token.
--				Else Return null.
-- =============================================
--	Parameters
    IN param_email VARCHAR(255),
    IN param_password VARCHAR(255),
    OUT out_sessionToken VARCHAR(255)
)
BEGIN
	DECLARE var_userID INT;
    DECLARE var_passHash BINARY(64);
    DECLARE var_salt BINARY(16);
    DECLARE var_sessionToken VARCHAR(255);
    
    -- Grab the user from the database if they exist
    SELECT UserID, PasswordHash, Salt INTO var_userID, var_passHash, var_salt
    FROM user
    WHERE email = param_email
    LIMIT 1;
    
    IF var_userID IS NOT NULL THEN
        -- We need to hash the password the user entered with the users salt so we can compare it
        SET @calculated_hash = SHA2(CONCAT(param_password, var_salt), 256);
        
        IF @calculated_hash = var_passHash THEN
			-- Clear out sessions for the user before we create a new session
            DELETE FROM Session
			WHERE UserID = var_userID;
        
            -- We then create a new UUID() to store as out session token
            SET var_sessionToken = UUID();
            
            INSERT INTO Session (
				UserID,
                SessionToken,
                CreatedAt,
                ExpiresAt
			)
            VALUES (
				var_userID,
                var_sessionToken,
                NOW(),
                DATE_ADD(NOW(), INTERVAL 48 HOUR)
			);
            
            -- Return the session token
            SET out_sessionToken = var_sessionToken;
        ELSE
            -- If the password comparison failed, return null and then we will have to handle it on the backend
            SET out_sessionToken = NULL;
        END IF;
    ELSE
        -- Same for email, if a user doesn't exist we will return null and handle the status we want to return on the backend
        SET out_sessionToken = NULL;
    END IF;
END$$

DELIMITER ;

-- Commit transaction assuming there were no errors up to this point
COMMIT;
