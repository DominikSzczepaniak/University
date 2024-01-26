CREATE TABLE OSOBA (
    id SERIAL PRIMARY KEY,
    imie VARCHAR(50),
    nazwisko VARCHAR(50),
    plec CHAR(1)
);

INSERT INTO OSOBA (imie, nazwisko, plec)
VALUES ('Anna', 'Kowalska', 'K'),
       ('Jan', 'Nowak', 'M'),
       ('Maria', 'Wiśniewska', 'K');

SELECT * FROM OSOBA;
