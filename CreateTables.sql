use moffatbaylodge_dev;

CREATE TABLE Customers (
	CustomerID int NOT NULL,
    EmailID int,
    First_Name varchar(255),
    Last_Name varchar(255),
    address varchar(255),
    Telephone_number varchar(20)
);

CREATE TABLE ImageStore (
	ImageID int NOT NULL,
    ImageData MEDIUMBLOB,
    ImageType varchar(50),
    EntityID INT,
    EntityType varchar(50)
);

CREATE TABLE RoomType (
	RoomTypeID int NOT NULL,
    PrimaryImageID INT,
    RoomView varchar(255),
    Bedding varchar(255),
    base_price Decimal
);

CREATE TABLE Room(
	RoomID int NOT NULL,
    RoomTypeID INT,
    RoomCapacity INT
);

CREATE TABLE Reservation (
	ReservationID int NOT NULL,
    CustomerID INT,
    RoomID INT,
    NumberOfGuests INT,
    PaymentID INT
);

CREATE TABLE User (
	UserID int NOT NULL,
    CustomerID INT,
    EmailID INT
);

CREATE TABLE Payment (
	PaymentID int NOT NULL,
    ReservationID INT,
    EmailAddress varchar(255),
    PaymentAmount decimal,
    PaymentDate DATE,
    PaymentMethod varchar(255)

);

CREATE TABLE Email (
	EmailID int NOT NULL,
    EmailAddress Varchar(255)
);


CREATE TABLE PasswordReset (
	PasswordResetID int NOT NULL,
    CustomerID INT,
    GUID char(36),
    ExpirationDate DATETIME
);

CREATE TABLE Session (
	SessionID int NOT NULL,
    CustomerID INT,
    Token Varchar(64),
    ExpirationDate DATETIME
);

CREATE TABLE Confirmation (
	ConfirmationID int NOT NULL,
    CustomerID INT,
    GUID Char(36)
);