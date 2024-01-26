CREATE TABLE OSOBA (
    id INT PRIMARY KEY,
    imie VARCHAR(50),
    nazwisko VARCHAR(50),
    plec CHAR(1)
);

CREATE SEQUENCE osoba_id_seq START WITH 1 INCREMENT BY 1;

INSERT INTO OSOBA (id, imie, nazwisko, plec)
VALUES (NEXTVAL('osoba_id_seq'), 'Anna', 'Kowalska', 'K'),
       (NEXTVAL('osoba_id_seq'), 'Jan', 'Nowak', 'M'),
       (NEXTVAL('osoba_id_seq'), 'Maria', 'Wiśniewska', 'K');

SELECT * FROM OSOBA;