CREATE TABLE Patient (
    Patient VARCHAR(255) PRIMARY KEY,
    HouseNumber INT,
    PostalCode VARCHAR(6),
    City VARCHAR(255)
);

CREATE TABLE Physician (
    Physician VARCHAR(255) PRIMARY KEY,
    Specialization VARCHAR(255),
)

CREATE TABLE Appointment (
    AppointmentID INT PRIMARY KEY,
    Patient VARCHAR(255) FOREIGN KEY REFERENCES Patient(Patient),
    Physician VARCHAR(255) FOREIGN KEY REFERENCES Physician(Physician),
    AppointmentDate DATE,
    AppointmentLocation VARCHAR(255),
    Price DECIMAL(10, 2),
    CauseDecription VARCHAR(255)
)