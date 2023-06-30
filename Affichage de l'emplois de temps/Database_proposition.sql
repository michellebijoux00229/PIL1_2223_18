CREATE DATABASE IF NOT EXISTS gestionEmplois; 	/* Création de la base de donnes */
USE gestionEmplois; 				/* Utilisation de la base de données */

/* Création des tables et la spécification des clés primaires et étrangères*/
 CREATE TABLE IF NOT EXISTS Administrateur(
	id_admin INT NOT NULL,
	nom_admin VARCHAR (255) NOT NULL,
	prenom_admin VARCHAR(255),
	email_admin VARCHAR(255),
	poste_admin VARCHAR(255),
	mot_de_passe varchar (255) NOT NULL,
    PRIMARY KEY(id_admin)
  )ENGINE = InnoDB;
  
 CREATE TABLE IF NOT EXISTS Etudiant(
	matricule BIGINT NOT NULL,
	nom VARCHAR(255),
	prenom VARCHAR(255),
	promotion VARCHAR(255),
	email VARCHAR(255),
	mot_de_passe VARCHAR(255) NOT NULL,
	PRIMARY KEY(matricule)
)ENGINE = InnoDB;
  
  CREATE TABLE IF NOT EXISTS Emplois(
	id_emploie INT NOT NULL AUTO_INCREMENT,
	semaine DATE NOT NULL,
    promotion VARCHAR(100) NOT NULL,
    matiere VARCHAR(255) NOT NULL,
    masse_horaire TIME NOT NULL,
    temps_restant TIME NOT NULL,
    professeur VARCHAR(255) NOT NULL,
    salle VARCHAR(100) NOT NULL,
    jour DATE NOT NULL,
    heure_debut TIME NOT NULL,
    heure_fin TIME NOT NULL,
    PRIMARY KEY(id_emploie)
)ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS Examen(
	id_exam INT NOT NULL AUTO_INCREMENT,
	matiere VARCHAR(255) NOT NULL,
	date DATE NOT NULL,
    heure_debut TIME NOT NULL,
    heure_fin TIME NOT NULL, 
	PRIMARY KEY(id_exam)
)ENGINE = InnoDB;

CREATE TABLE Evenement(
	id_event INT NOT NULL AUTO_INCREMENT,
	type_event VARCHAR(255) NOT NULL,
    jour_debut DATETIME NOT NULL,
    jour_fin DATETIME NOT NULL,
    PRIMARY KEY(id_event)
)ENGINE = InnoDB;
    