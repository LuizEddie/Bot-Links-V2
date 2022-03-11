import os
import json
from datetime import date
import time
from google_play_scraper import app

class MainClass:

    appData = []
    log_path = "log/"

    def __init__(self):
        pass

    def read_json_data(self):
        json_path = open('Links.json', 'r', encoding="utf8")
        data = json.load(json_path)

        print("Dados Carregados")
        links = data['links']

        self.check_app_status(links)

    def check_app_status(self, apps):

        count = 0
        for appl in apps:
            try:
                app(
                    appl['url'],
                    lang='pt',  # defaults to 'en'
                    country='br',  # defaults to 'us'
                )

                self.appData.append({"Nome": appl['name'],
                                     "Status": "Online"})

            except Exception as e:
                print(e)
                self.appData.append({"Nome": appl['name'],
                                     "Status": "Offline"})

            count = count + 1

            print("Lendo... " + str((count / len(apps)) * 100) + "%")
            os.system("cls||clear")

        self.write_log_file()

    def create_log_file(self):
        self.log_path += str(date.today()) + " " + str(time.time()) + ".txt"

        file = open(self.log_path, "x", encoding="utf8")

        file.close()

        self.read_json_data()

    def write_log_file(self):
        file = open(self.log_path, "w", encoding="utf8")
        file.write(str(date.today()) + str(time.time()) + "\n\n")

        for appl in self.appData:
            file.write("App: " + appl['Nome'] + "\n")
            file.write("Status: " + appl['Status'] + "\n\n")
        file.close()

        self.read_log_file()

    def read_log_file(self):
        file = open(self.log_path, "r", encoding="utf8")
        print(file.read())
        file.close()

try:
    mainClass = MainClass()

    mainClass.create_log_file()

    os.system("pause")

except Exception as e:
    print("Erro")