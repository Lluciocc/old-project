import customtkinter as ctk
from tkinter import filedialog, messagebox
import pandas as pd
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
from PIL import Image
from PIL import Image, ImageTk
import tkinter as tk  
from colorama import *

# pyinstaller --clean --onefile --windowed main.py
init()


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx;*.xls")])
    if file_path:
        convert_excel_to_json(file_path)

import pandas as pd
import json
import tkinter.messagebox as messagebox

import pandas as pd
import json
import tkinter.messagebox as messagebox
from colorama import Fore, Style

def convert_excel_to_json(file_path):
    try:
        # Charger le fichier Excel
        df = pd.read_excel(file_path)
        print(Fore.YELLOW + Style.BRIGHT + str(df))  # Afficher le DataFrame initial
        
        # Renommer les colonnes pour correspondre à ce qui est attendu
        df.columns = ['NOM APPORTEUR', 'CIVILITE', 'NOM', 'PRENOM', 'DATE NAISSANCE', 'AGE', 'RUE', 'CP', 'VILLE', 'EMAIL']
        
        # Vérifier que les colonnes 'EMAIL' et 'DATE NAISSANCE' existent
        if "EMAIL" not in df.columns or "DATE NAISSANCE" not in df.columns:
            messagebox.showerror("Erreur", "Le fichier doit contenir 'EMAIL' et 'DATE NAISSANCE' (format YYYY-MM-DD)")
            return
        
        # Supprimer les lignes où 'EMAIL' ou 'DATE NAISSANCE' sont vides
        df = df.dropna(subset=["EMAIL", "DATE NAISSANCE"])

        # Convertir 'DATE NAISSANCE' en datetime si nécessaire, et gérer les erreurs
        df['DATE NAISSANCE'] = pd.to_datetime(df['DATE NAISSANCE'], errors='coerce')  # Erreurs converties en NaT
        
        # Gérer les valeurs NaT en les convertissant en chaîne vide ou une valeur par défaut
        df['DATE NAISSANCE'] = df['DATE NAISSANCE'].apply(lambda x: x.strftime('%Y-%m-%d') if pd.notna(x) else 'Inconnu')

        # Convertir le DataFrame en dictionnaire pour JSON
        data = df.to_dict(orient="records")
        print(data)
        # Enregistrer le dictionnaire dans un fichier JSON
        with open("emails.json", "w") as json_file:
            json.dump(data, json_file, indent=4)
        
        messagebox.showinfo("Succès", "Fichier importé avec succès ! Vérification des anniversaires...")
        print(data)
        check_and_send_emails(data)
        
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la conversion : {e}")
        
        
        
        
def check_and_send_emails(data):
    today = datetime.today().strftime("%Y-%m-%d")
    count = 0
    for person in data:
        if person["EMAIL"] != "":
            if person["DATE NAISSANCE"] == today:
                send_email(person["EMAIL"])
                count += 1
        else:
            print(Fore.RED, Style.BRIGHT, "Attention ")
            send_email("lluciocc.000@gmail.com")

    if count > 0:
        messagebox.showinfo("Succès", f"{count} e-mails envoyés !")
    else:
        messagebox.showinfo("Info", "Aucun anniversaire aujourd'hui.")

def send_email(email_receiver):
    with open("config.json", "r") as file:
        z = json.load(file)

    try:
        SMTP_SERVER = z["SMTP_SERVER"]
        SMTP_PORT = z["SMTP_PORT"]
        EMAIL_SENDER = z["SMTP_EMAIL_SENDER"]
        EMAIL_PASSWORD = z["SMTP_EMAIL_PASSWORD"]
        response = messagebox.askyesno(
            "Vérification des informations",
            f"Tout est prêt, veuillez vérifier que les informations sont correctes:\n"
            f"Server: {SMTP_SERVER}\n"
            f"Port: {SMTP_PORT}\n"
            f"Email: {EMAIL_SENDER}\n"
            f"Mot de passe: {EMAIL_PASSWORD}"
        )
        if response:
            print("Envoi du mail...")
        else:
            print(Fore.RED,"Annulation de l'envoi de l'email.")
            return
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la configuration interne de l'envoie du mail : {e}")

    msg = MIMEMultipart()
    msg["From"] = EMAIL_SENDER
    msg["To"] = email_receiver
    msg["Subject"] = "🎉 Joyeux Anniversaire ! 🎂"

    html_content = """
    <html>
        <body style="font-family: Arial, sans-serif; text-align: center;">
            <style>
                body { font-family: Arial, sans-serif; margin: 0; padding: 0; background-color: #f4f4f4; }
                .container { width: 100%; max-width: 600px; margin: auto; background: #ffffff; padding: 20px; }
                .header { text-align: center; padding: 10px 0; }
                .content { font-size: 16px; line-height: 1.5; color: #333333; }
                .footer { text-align: center; font-size: 12px; color: #777777; padding: 10px 0; }
            </style>
            <div class="container">
                <div class="header">
                    <img src="https://wpm.ccmp.eu/wpm/879/2025/01/08012025_voeux/logo.png" alt="SwissLife" width="300">
                </div>
                <div class="content">
                    <h2 style="color: #4CAF50; text-align: center;">Joyeux Anniversaire ! 🎉</h2>
                    <p>Nous vous souhaitons une excellente journée pleine de bonheur et de surprises !</p>
                    <p style="text-align: center;">🎂🥳🎁</p>
                </div>
                <div class="footer">
                    <strong>MICHEL CIALDELLA</strong><br>
                    Tél : <strong>0355188288</strong><br>
                    E-mail : <strong>thionville@agence-swisslife.fr</strong>
                    <br>
                    <p>&copy; 2025 SwissLife. Tous droits réservés.</p>
                </div>
            </div>
        </body>
    </html>
    """
    
    msg.attach(MIMEText(html_content, "html"))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        print(Fore.GREEN, "Connexion réussie au serveur SMTP")
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        print(Fore.GREEN,"Login réussie au serveur SMTP")
        server.sendmail(EMAIL_SENDER, email_receiver, msg.as_string())
        server.quit()
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible d'envoyer l'email à {email_receiver} : {e}")

def load_config():
    try:
        with open("config.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {
            "SMTP_SERVER": "smtp.gmail.com",
            "SMTP_PORT": "587",
            "SMTP_EMAIL_SENDER": "",
            "SMTP_EMAIL_PASSWORD": ""
        }

def save_config():
    data = {
        "SMTP_SERVER": entry_fields["server"].get(),
        "SMTP_PORT": entry_fields["port"].get(),
        "SMTP_EMAIL_SENDER": entry_fields["email_sender"].get(),
        "SMTP_EMAIL_PASSWORD": entry_fields["email_password"].get(),
        "isConfig" : True
    }
    with open("config.json", "w") as file:
        json.dump(data, file, indent=4)
    label_status.configure(text="Configuration enregistrée ✅", text_color="green")

# Créer les champs de configuration
def set_config_box():
    config_data = load_config()

    labels = ["Serveur SMTP:", "Port SMTP:", "Email Expéditeur:", "Mot de Passe:"]
    keys = ["server", "port", "email_sender", "email_password"]

    for i in range(4):
        ctk.CTkLabel(master=config_frame, text=labels[i]).pack()
        entry = ctk.CTkEntry(master=config_frame, width=300, show="•" if keys[i] == "password" else "")
        entry.insert(0, config_data.get("SMTP_" + keys[i].upper(), ""))
        entry.pack(pady=5)
        entry_fields[keys[i]] = entry 
        print("SMTP_" + keys[i].upper(), config_data.get("SMTP_" + keys[i].upper(), ""))

    btn_save = ctk.CTkButton(master=config_frame, text="Enregistrer", command=save_config)
    btn_save.pack(pady=10)

def add_config_true():
    with open("config.json", "r") as file:
        z = json.load(file)

    data = {"isConfig": True}
    z.update(data)

    with open("config.json", "w") as file:
        json.dump(z, file, indent=4)

def add_config_false():
    with open("config.json", "r") as file:
        z = json.load(file)

    data = {"isConfig": False}
    z.update(data)

    with open("config.json", "w") as file:
        json.dump(data, file, indent=4)

def check_if_file_is_good():
    with open("config.json", "r") as file:
        data = json.load(file)
        if (data.get("SMTP_SERVER") != "" and 
            data.get("SMTP_PORT") != "" and 
            data.get("SMTP_EMAIL_SENDER") != "" and 
            data.get("SMTP_EMAIL_PASSWORD") != ""):
            return True
        else:
            add_config_false()
            return False

def config():
    try:
        with open("config.json", "r") as file:
            data = json.load(file)
            conf = data.get("isConfig")
            if conf and check_if_file_is_good():
                message = ctk.CTkLabel(master=config_frame, text="Tout bon ! ✅",text_color="green", font=("Arial", 18))
                message.pack(pady=10)
                add_config_true()
            else:
                message = ctk.CTkLabel(master=config_frame, text="Veuillez configurer ! ❌", text_color="red", font=("Arial", 18))
                message.pack(pady=1)
                set_config_box()
            
    except (FileNotFoundError, json.JSONDecodeError):
        data = {"isConfig": False}

    with open("config.json", "w") as file:
        json.dump(data, file, indent=4)


ctk.set_default_color_theme("blue")  
ctk.set_appearance_mode("dark")  

app = ctk.CTk()
app.title("Envoi d'Emails d'Anniversaire")
app.geometry("800x600")

import_frame = ctk.CTkFrame(master=app, fg_color='#8D6F3A', border_color='#FFCC70', border_width=2)
import_frame.pack(expand=True, fill="both", padx=20, pady=20)

label = ctk.CTkLabel(master=import_frame, text="Importer un fichier Excel", font=("Arial", 18))
label.pack(pady=10)

btn_select = ctk.CTkButton(master=import_frame, text="Choisir un fichier", command=select_file)
btn_select.pack(pady=10)

config_frame = ctk.CTkScrollableFrame(master=app, fg_color='#4a275e', border_color='#6F3A8D', border_width=2)
config_frame.pack(expand=True, fill="both", padx=20, pady=20)

label = ctk.CTkLabel(master=config_frame, text="Configurer", font=("Arial", 18))
label.pack(pady=10)

label_status = ctk.CTkLabel(master=config_frame, text="")
label_status.pack()

# ico

image_path = "./fav32.png" 

try:
    image = Image.open(image_path)
    photo_image = ImageTk.PhotoImage(image)
    app.iconphoto(False, photo_image)
except Exception as e:
    print(f"Erreur lors de la définition de l'icône: {e}")



entry_fields = {} 
config()
app.mainloop()
