-- Begin transaction to allow rollback if needed
START TRANSACTION;

DROP TABLE IF EXISTS ReservationAmenity;
DROP TABLE IF EXISTS Reservation;
DROP TABLE IF EXISTS Amenity;
DROP TABLE IF EXISTS RoomType;
DROP TABLE IF EXISTS PasswordResetRequest;
DROP TABLE IF EXISTS Session;
DROP TABLE IF EXISTS RegisteredUser;

CREATE TABLE RegisteredUser (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(255) NOT NULL,
    LastName VARCHAR(255) NOT NULL,
    Email VARCHAR(255) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(20),
    PasswordHash VARCHAR(255) NOT NULL,
    Salt VARCHAR(255) NOT NULL,
    GuestFlag BOOLEAN DEFAULT FALSE,
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
    FOREIGN KEY (UserID) REFERENCES RegisteredUser(UserID) ON DELETE SET NULL
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

CREATE TABLE Session (
    SessionID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    SessionToken VARCHAR(255) UNIQUE NOT NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    ExpiresAt DATETIME,
    FOREIGN KEY (UserID) REFERENCES RegisteredUser(UserID) ON DELETE CASCADE
);

CREATE TABLE PasswordResetRequest (
    ResetRequestID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    ResetToken VARCHAR(255) UNIQUE NOT NULL,
    CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    ExpiresAt DATETIME,
    Used BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (UserID) REFERENCES RegisteredUser(UserID) ON DELETE CASCADE
);

INSERT INTO RegisteredUser (FirstName, LastName, Email, PhoneNumber, PasswordHash, Salt, GuestFlag)
VALUES 
('John', 'Doe', 'test1@email.com', '1234567890', 'password1', 'salt1', FALSE),
('Jane', 'Smith', 'test2@email.com', '0987654321', 'password2', 'salt2', FALSE),
('Alice', 'Johnson', 'test3@email.com', '1122334455', 'password3', 'salt3', TRUE); --guest!!

INSERT INTO RoomType (RoomTypeName, BasePrice, MaxGuests)
VALUES 
('Double Full Beds', 115.00, 2),
('Queen', 115.00, 2),
('King', 150.00, 5);

INSERT INTO Reservation (UserID, Email, RoomType, NumberOfGuests, CheckInDate, CheckOutDate, TotalPrice, ReservationStatus)
VALUES 
(1, 'john.doe@example.com', 'Queen', 2, '2024-09-01', '2024-09-07', 805.00, 'Confirmed'),
(NULL, 'guest@example.com', 'King', 3, '2024-09-10', '2024-09-14', 600.00, 'Confirmed'),
(3, 'alice.johnson@example.com', 'Double Full Beds', 1, '2024-09-15', '2024-09-18', 345.00, 'Canceled');

INSERT INTO Amenity (AmenityName, Description, Price)
VALUES 
('Kayaking', 'Enjoy a scenic kayak ride', 50.00),
('Whale Watching', 'Observe the magnificent whales', 75.00),
('Scuba Diving', 'Explore the underwater world', 100.00);

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

-- Commit transaction assuming there were no errors up to this point
COMMIT;
