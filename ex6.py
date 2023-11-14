from datetime import datetime

maintenant = datetime.now()

format_date_heure = "%Y-%m-%d %H:%M:%S"
date_heure_formattees = maintenant.strftime(format_date_heure)

print("La date et l'heure actuelles sont :", date_heure_formattees)
