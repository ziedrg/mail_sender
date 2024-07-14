import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Vos informations
sender_email = "ziedrg@hotmail.fr"
password = "rlbjhsalqclrklqm"
subject = "Candidature Spontanée - Admin Système et Réseau / Ingénieur Système d'Information Décisionnel"
body_admin = """\
Bonjour,

Je me permets de vous adresser ma candidature spontanée pour un poste d'administrateur système et réseau. Avec plus de 10 ans d'expérience dans le domaine de l'administration des systèmes et des réseaux, j'ai acquis des compétences solides en gestion des infrastructures informatiques et en résolution des problèmes techniques.

Je serais ravi de discuter de la manière dont je pourrais contribuer à votre équipe.

Cordialement,
RGUEZ ZIED
"""
body_engineer = """\
Bonjour,

Je souhaite vous proposer ma candidature spontanée pour un poste d'ingénieur en systèmes d'information décisionnels. Avec une maîtrise en ingénierie des systèmes d'information et une expérience approfondie en développement avec Angular, Python, BI, et IA, je suis convaincu de pouvoir apporter une valeur ajoutée significative à votre entreprise.

Je suis à votre disposition pour toute information complémentaire.

Cordialement,
RGUEZ ZIED
"""

# Chemin vers le CV
cv_path = r"E:\project\candidature_sender\CV_ZIED_RGUEZ_2024__FR_.pdf"

# Liste des destinataires
recipients = [
 
    "contact-it@aymax.fr",
    "info@beprimetech.com",
    "recrutement@be-softilys.tn",
    "info@biforyou.com",
    "contact@chifco.com",
    "stage@coachess.tn",
    "mohamedali.zaier@outlook.com",
    "contact.codactsolutions@gmail.com",
    "business@consultim-it.com",
    "hellotunis@creado.agency",
    "contact@cynoia.com",
    "contact@industryx0.pro",
    "recrutement-tn@autobiz.com",
    "contact@comar.tn",
    "contact@tech-expert.io",
    "contact@connect.network",
    "contact@smarttouchtunisie.com",
    "contact.team@dracoss.tn",
    "hello@pepolls.com",
    "contact@diginov.tech",
    "discovery.inf@discovery.com.tn",
    "contact@digibrainagency.com",
    "contact@farkito.tn",
    "recruitment-tn@newaccess.ch",
    "recrutement@actia-engineering.tn"
  
]

# Préparer les emails
def prepare_email(to_email, body, cv_path):
    print(f"Préparation de l'email pour {to_email}")
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Joindre le CV
        with open(cv_path, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(cv_path)}")
            msg.attach(part)

        print(f"Email préparé pour {to_email} avec sujet '{subject}' et corps:\n{body}\n")
        print(f"CV joint: {cv_path}")
        return msg
    except Exception as e:
        print(f"Erreur en préparant l'email pour {to_email}: {e}")
        return None

# Envoyer les emails
def send_email(msg):
    try:
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, msg['To'], msg.as_string())
        server.quit()
        print(f"Email envoyé à {msg['To']}")
    except Exception as e:
        print(f"Erreur en envoyant l'email à {msg['To']}: {e}")

# Préparer et envoyer les candidatures pour les deux profils
for recipient in recipients:
    msg_admin = prepare_email(recipient, body_admin, cv_path)
    if msg_admin:
        send_email(msg_admin)
    
    msg_engineer = prepare_email(recipient, body_engineer, cv_path)
    if msg_engineer:
        send_email(msg_engineer)
