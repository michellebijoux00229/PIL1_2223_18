/*Creaction de la base de donnes*/

/*CREATE DATABASE GE_TDP;*/

/*utilisation de la base de donnes*/

USE GE_TDP;

/*Créaction des tables et la spécification des cles primaires et etrangères*/

DROP TABLE IF EXISTS Administrateur;

  CREATE TABLE Administrateur(
  id_Admin INT NOT NULL PRIMARY KEY,
  Nom_admin varchar (100) NOT NULL,
  Mot_de_passe varchar (255) NOT NULL)
  ENGINE =InnoDB;
  
   DROP TABLE IF EXISTS Salle;
   
  CREATE TABLE Salle(
  id_Salle INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Nom_Salle CHAR(100),
  Localisation_Salle VARCHAR(255))
  ENGINE=InnoDB;
  
  DROP TABLE IF EXISTS Filiére;
  
  CREATE TABLE Filiére(
  id_Filiére INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    Code_Mat BIGINT,
    Libellé_Mat CHAR (100))
    ENGINE=InnoDB;
  
   DROP TABLE IF EXISTS Etudiant;
   
  CREATE TABLE Etudiant(
  Numéro_matricule_Etu BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Nom_Etu VARCHAR(200),
  Prénom_Etu VARCHAR(200),
  Promotion_Etu VARCHAR(100),
  Email_Etu VARCHAR(100),
  id_Filiére INT NOT NULL,
  CONSTRAINT fk_id_Filiére_Numéro_matricule_Etu FOREIGN KEY (id_Filiére ) REFERENCES Filiére ( id_Filiére ))
  ENGINE=InnoDB;
  
  DROP TABLE IF EXISTS Matière ;
  
   CREATE TABLE  Matière (
  id_Mat INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  Code_Mat BIGINT,
  Libellé_Mat CHAR (100),
  Masse_horaire INT(20),
  id_Salle INT NOT NULL,
  id_Filiére INT NOT NULL,
	CONSTRAINT fk_id_Salle_id_Mat FOREIGN KEY (
  id_Salle ) REFERENCES 	Salle (id_Salle ),
  CONSTRAINT fk_id_Filiére_id_Mat FOREIGN KEY (
  id_Filiére ) REFERENCES Filiére (id_Filiére ))
  ENGINE=InnoDB;
  
   DROP TABLE IF EXISTS Horaire;
   
  CREATE TABLE Horaire(
  Date_heure DATETIME NOT NULL PRIMARY KEY,id_Mat INT NOT NULL,
  CONSTRAINT fk_id_Mat_Date_heure FOREIGN KEY (id_Mat ) REFERENCES Matière (id_Mat))
  ENGINE=InnoDB;
  
  DROP TABLE IF EXISTS Professeur;

 CREATE TABLE  Professeur(
 id_Professeur INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
 Nom_Professeur VARCHAR(200),
 Prénom_Professeur VARCHAR(200),
 Adresse_Email_Professeur VARCHAR(255))
 ENGINE=InnoDB;
 
 DROP TABLE IF EXISTS Enseignements ;
 
 CREATE TABLE Enseignements(
 id_Mat  INT NOT NULL,
 id_Professeur INT NOT NULL,
 PRIMARY KEY (id_Mat, id_Professeur),
  CONSTRAINT fk_id_Mat_id_Mat_id_Professeur FOREIGN KEY (id_Mat) REFERENCES Matière (id_Mat ),
  CONSTRAINT fk_id_Professeur_id_Mat_id_Professeur FOREIGN KEY (id_Professeur) REFERENCES Professeur  (id_Professeur))
  ENGINE=InnoDB;
   
   
  
