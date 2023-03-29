.sqlite3 GULLOSO.db
CREATE TABLE Aprendiz(
idestudiante CHAR (10) PRIMARY KEY NOT NULL,
primer_nom VARCHAR (20),
primer_ape VARCHAR (20),
seg_nom VARCHAR (20),
seg_ape VARCHAR (20));

CREATE TABLE Colegio(
idcolegio CHAR (10) PRIMARY KEY,
estudiante_idestudiante CHAR (10) NOT NULL,
privado VARCHAR(20),
distrital VARCHAR(20),
);#CONSTRAINT FK_Aprendiz FOREIGN KEY (estudiante_idestudiante) REFERENCES Aprendiz (idestudiante)

INSERT INTO Aprendiz VALUES (1,'ANGELO','RIZO','JOSE','GULLOSO');
INSERT INTO Aprendiz VALUES (2,'DARIO','RIZO','JOSE','OSPINO');
INSERT INTO Aprendiz VALUES (3,'ANTHONY','RIZO','STIVEN','GULLOSO');
INSERT INTO Aprendiz VALUES (4,'LEINER','OSPINO','PEPE','MEJIA');

INSERT INTO Colegio VALUES (1,1,'PRIVADO','VIDA NUEVA');
INSERT INTO Colegio VALUES (2,2,'PUBLICO','INTEGARDO');
INSERT INTO Colegio VALUES (3,3,'PRIVADO','ALFONZO LOPEZ');
INSERT INTO Colegio VALUES (4,4,'PUBLICO','ISEDE');

ALTER TABLE Colegio
ADD FOREIGN KEY (estudiante_idestudiante) REFERENCES Aprendiz (idestudiante)

SELECT * FROM Aprendiz,Colegio
SELECT * FROM Colegio
SELECT * FROM Aprendiz
SELECT idestudiante FROM Aprendiz








