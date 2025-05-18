from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import os

professions_disponibles = [
    "Masseur-kinésithérapeute", "Gynécologues / Obstétricien", "Infirmier", "Infirmier en pratique avancée",
    "Ophtalmologiste", "Chirurgiens-dentistes", "Médecin généraliste", "Acupuncteur", "Allergologue",
    "Ambulance / Véhicule sanitaire léger", "Anatomo-Cyto-Pathologiste", "Anesthésiste réanimateur",
    "Angiologue", "Cancérologues", "Cardiologue", "Chirurgien-dentiste spécialiste en orthopédie dento-faciale",
    "Chirurgien général", "Chirurgien infantile", "Chirurgien maxillo-facial", "Chirurgien maxillo-facial et stomatologiste",
    "Chirurgien oral", "Chirurgien orthopédiste et traumatologue", "Chirurgien plasticien", "Chirurgien thoracique et cardio-vasculaire",
    "Chirurgien urologue", "Chirurgien vasculaire", "Chirurgien viscéral", "Dermatologue et vénérologue", "Echographiste",
    "Endocrinologue-diabétologue", "Fournisseur de matériel médical et para-médical", "Gastro-entérologue et hépatologue",
    "Gériatre", "Hématologue", "Homéopathe", "Laboratoires", "Médecin biologiste", "Médecin généticien",
    "Médecin spécialiste en médecine nucléaire", "Médecin spécialiste en santé publique et médecine sociale",
    "Médecin thermaliste", "Médecine appliquée aux sports", "Médecine d'urgence", "Médecine des Maladies infectieuses et tropicales",
    "Médecine légale et expertises médicales", "Médecine vasculaire", "Néphrologue", "Neurochirurgien", "Neurologue",
    "Neuropsychiatre", "Orthophoniste", "Orthoptiste", "Oto-Rhino-Laryngologue (ORL) et chirurgien cervico-facial",
    "Pédiatre", "Pédicure-podologue", "Pharmacien", "Phoniatre", "Pneumologue", "Psychiatres", "Radiologue",
    "Radiothérapeute", "Réanimateur médical", "Rhumatologue", "Sage-femme", "Spécialiste en allergologie",
    "Spécialiste en médecine interne", "Spécialiste en médecine physique et de réadaptation", "Stomatologistes"
]

departements_disponibles = [
    "Dans le département 01 (Ain)", "Dans le département 02 (Aisne)", "Dans le département 2A (Corse Du Sud)",
    "Dans le département 2B (Haute Corse)", "Dans le département 03 (Allier)", "Dans le département 04 (Alpes De Haute Provence)",
    "Dans le département 05 (Hautes Alpes)", "Dans le département 06 (Alpes Maritimes)", "Dans le département 07 (Ardeche)",
    "Dans le département 08 (Ardennes)", "Dans le département 09 (Ariege)", "Dans le département 10 (Aube)",
    "Dans le département 11 (Aude)", "Dans le département 12 (Aveyron)", "Dans le département 13 (Bouches Du Rhone)",
    "Dans le département 14 (Calvados)", "Dans le département 15 (Cantal)", "Dans le département 16 (Charente)",
    "Dans le département 17 (Charente Maritime)", "Dans le département 18 (Cher)", "Dans le département 19 (Correze)",
    "Dans le département 21 (Cote D'or)", "Dans le département 22 (Cotes D'armor)", "Dans le département 23 (Creuse)",
    "Dans le département 24 (Dordogne)", "Dans le département 25 (Doubs)", "Dans le département 26 (Drome)",
    "Dans le département 27 (Eure)", "Dans le département 28 (Eure Et Loir)", "Dans le département 29 (Finistere)",
    "Dans le département 30 (Gard)", "Dans le département 31 (Haute Garonne)", "Dans le département 32 (Gers)",
    "Dans le département 33 (Gironde)", "Dans le département 34 (Herault)", "Dans le département 35 (Ille Et Vilaine)",
    "Dans le département 36 (Indre)", "Dans le département 37 (Indre Et Loire)", "Dans le département 38 (Isere)",
    "Dans le département 39 (Jura)", "Dans le département 40 (Landes)", "Dans le département 41 (Loir Et Cher)",
    "Dans le département 42 (Loire)", "Dans le département 43 (Haute Loire)", "Dans le département 44 (Loire Atlantique)",
    "Dans le département 45 (Loiret)", "Dans le département 46 (Lot)", "Dans le département 47 (Lot Et Garonne)",
    "Dans le département 48 (Lozere)", "Dans le département 49 (Maine Et Loire)", "Dans le département 50 (Manche)",
    "Dans le département 51 (Marne)", "Dans le département 52 (Haute Marne)", "Dans le département 53 (Mayenne)",
    "Dans le département 54 (Meurthe Et Moselle)", "Dans le département 55 (Meuse)", "Dans le département 56 (Morbihan)",
    "Dans le département 57 (Moselle)", "Dans le département 58 (Nievre)", "Dans le département 59 (Nord)",
    "Dans le département 60 (Oise)", "Dans le département 61 (Orne)", "Dans le département 62 (Pas De Calais)",
    "Dans le département 63 (Puy De Dome)", "Dans le département 64 (Pyrenees Atlantiques)", "Dans le département 65 (Hautes Pyrenees)",
    "Dans le département 66 (Pyrenees Orientales)", "Dans le département 67 (Bas Rhin)", "Dans le département 68 (Haut Rhin)",
    "Dans le département 69 (Rhone)", "Dans le département 70 (Haute Saone)", "Dans le département 71 (Saone Et Loire)",
    "Dans le département 72 (Sarthe)", "Dans le département 73 (Savoie)", "Dans le département 74 (Haute Savoie)",
    "Dans le département 75 (Paris)", "Dans le département 76 (Seine Maritime)", "Dans le département 77 (Seine Et Marne)",
    "Dans le département 78 (Yvelines)", "Dans le département 79 (Deux Sevres)", "Dans le département 80 (Somme)",
    "Dans le département 81 (Tarn)", "Dans le département 82 (Tarn Et Garonne)", "Dans le département 83 (Var)",
    "Dans le département 84 (Vaucluse)", "Dans le département 85 (Vendee)", "Dans le département 86 (Vienne)",
    "Dans le département 87 (Haute Vienne)", "Dans le département 88 (Vosges)", "Dans le département 89 (Yonne)",
    "Dans le département 90 (Territoire De Belfort)", "Dans le département 91 (Essonne)", "Dans le département 92 (Hauts De Seine)",
    "Dans le département 93 (Seine Saint Denis)", "Dans le département 94 (Val De Marne)", "Dans le département 95 (Val D'oise)",
    "Dans le département 971 (Guadeloupe)", "Dans le département 972 (Martinique)", "Dans le département 973 (Guyane)",
    "Dans le département 974 (La Reunion)", "Dans le département 976 (Mayotte)"
]

def lancer_extraction(profession, departements_input, option):
    departements_selectionnes = [departements_disponibles[int(d.strip()) - 1] for d in departements_input]
    departements_codes = [d.split(" ")[3].strip("()") for d in departements_selectionnes]
    departements_str = "-".join(departements_codes)

    if option == 1:
        nom_fichier = f"{profession}_dp{departements_str}_all.xlsx"
    elif option == 2:
        nom_fichier = f"{profession}_dp{departements_str}_filter.xlsx"

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    document_dir = os.path.join(base_dir, "document")
    os.makedirs(document_dir, exist_ok=True)
    chemin_complet = os.path.join(document_dir, nom_fichier)

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    url = "https://annuairesante.ameli.fr/recherche.html"
    driver.get(url)
    time.sleep(3)

    noms = []
    professions = []
    telephones = []
    adresses = []

    driver.find_element(By.LINK_TEXT, "Liste des professionnels de santé").click()
    time.sleep(3)

    professions_links = driver.find_elements(By.LINK_TEXT, profession)
    profession_urls = [link.get_attribute("href") for link in professions_links]

    for profession_url in profession_urls:
        driver.get(profession_url)
        time.sleep(3)

        for departement in departements_selectionnes:
            departement_links = driver.find_elements(By.LINK_TEXT, departement)
            departement_urls = [link.get_attribute("href") for link in departement_links]

            for departement_url in departement_urls:
                driver.get(departement_url)
                time.sleep(3)

                ville_links = driver.find_elements(By.CSS_SELECTOR, "div.seo-liste ul li a")
                ville_urls = [link.get_attribute("href") for link in ville_links]

                for ville_url in ville_urls:
                    try:
                        driver.get(ville_url)
                        time.sleep(3)

                        try:
                            WebDriverWait(driver, 10).until(
                                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.item-professionnel-inner"))
                            )
                        except:
                            continue

                        while True:
                            professionnels = driver.find_elements(By.CSS_SELECTOR, "div.item-professionnel-inner")
                            for professionnel in professionnels:
                                try:
                                    try:
                                        nom = professionnel.find_element(By.CSS_SELECTOR, ".ignore-css a").text
                                    except:
                                        nom = "Non renseigné"

                                    try:
                                        profession = professionnel.find_element(By.CSS_SELECTOR, ".specialite").text
                                    except:
                                        profession = "Non renseigné"

                                    try:
                                        adresse = professionnel.find_element(By.CSS_SELECTOR, ".adresse").text
                                    except:
                                        adresse = "Non renseigné"

                                    try:
                                        telephone_element = professionnel.find_element(By.CSS_SELECTOR, ".tel")
                                        telephone = telephone_element.get_attribute('innerHTML').replace("&nbsp;", " ")
                                    except:
                                        telephone = "Non renseigné"

                                    if telephone != "Non renseigné":
                                        if option == 1:
                                            noms.append(nom)
                                            professions.append(profession)
                                            telephones.append(telephone)
                                            adresses.append(adresse)
                                        elif option == 2 and (telephone.startswith("06") or telephone.startswith("07")):
                                            noms.append(nom)
                                            professions.append(profession)
                                            telephones.append(telephone)
                                            adresses.append(adresse)

                                        data = {
                                            "Nom": [nom],
                                            "Profession": [profession],
                                            "Téléphone": [telephone],
                                            "Adresse": [adresse]
                                        }
                                        df = pd.DataFrame(data)
                                        if not os.path.isfile(chemin_complet):
                                            df.to_excel(chemin_complet, index=False)
                                        else:
                                            with pd.ExcelWriter(chemin_complet, mode="a", engine="openpyxl", if_sheet_exists="overlay") as writer:
                                                df.to_excel(writer, index=False, header=False, startrow=writer.sheets["Sheet1"].max_row)

                                except Exception as e:
                                    continue

                            try:
                                next_button = driver.find_element(By.LINK_TEXT, "Page suivante")
                                next_button.click()
                                time.sleep(3)
                            except:
                                break

                    except Exception as e:
                        continue

    driver.quit()

    return chemin_complet
