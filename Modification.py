import mysql.connector
# Connexion à la base de donnéesconn = mysql.connector.connect(    host="localhost",    user="Emploi_du_temps",    password="..",    database="emploi_du_temps") 
# Récupération des données de l'emploi du tempsdef get_emploi_du_temps():    
cursor = conn.cursor()   
cursor.execute("SELECT * FROM emploi_du_temps")    
emploi_du_temps = cursor.fetchall()   
cursor.close()  
return emploi_du_temps
# Modification de l'emploi du tempsdef modifier_emploi_du_temps(nouvelles_valeurs):   
cursor = conn.cursor()  
cursor.execute("UPDATE emploi_du_temps SET matiere = ?, heure = ?, jour = ?,masse horaire=?,charger du cours=?, Promotion=?,date=?,heure=?,Nom et prénom=?, Batiment et salle=?,Heure de début=?,heure de fin=?,dat=?,début=?,fn=? WHERE id = ? ",         
(nouvelles_donnees['matiere'], 
nouvelles_donnees['Masse horaire'], 
nouvelles_donnees['Charger du cours'],
nouvelles_donnees['Promotion'],
nouvelles_donnees['Date'],
nouvelles_donnees['heure'],
nouvelles_donnees['Non et prénom'],
nouvelles_donnees['Batiment et salle'],
nouvelles_donnees['Heure de début'],
nouvelles_donnees['heure de fin'],
nouvelles_donnees['Dat'],
nouvelles_donnees['Debut'],
nouvelles_donnees['Fn'], 
id_emploi_du_temps))
conn.commit()   
cursor.close()
