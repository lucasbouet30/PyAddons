import os
import zipfile
import shutil

class App():
    def __init__(self):

        choix = input("Do you want to add another mod ? (y/n) ")
        if choix == "y":
            shutil.rmtree('mod')
            os.makedirs('mod')

            jar_file = input("Please type the filename (modname).jar : ")

            zip_file = jar_file.replace(".jar", ".zip")
            os.rename(jar_file, zip_file)

            os.makedirs("mod", exist_ok=True)
            with zipfile.ZipFile(zip_file, 'r') as zip_ref:
                zip_ref.extractall("mod")
            print("did it !")
            zip_file.replace(".zip", ".jar")
            App.getname(self)
        elif choix == "n":
            App.getname(self)

    def getname(self):
        dossiers = os.listdir("mod/assets")
        nom_dossier = None
        for dossier in dossiers:
            if dossier != "minecraft":
                nom_dossier = dossier
                break
        self.nom = nom_dossier
        print(self.nom)
        App.getfoldersofrecipes(self)

    def getfoldersofrecipes(self):
        recipe_path = os.path.join("mod", "data", self.nom, "recipes")
        self.foldernames = [name for name in os.listdir(recipe_path) if os.path.isdir(os.path.join(recipe_path, name))]
        print(self.foldernames)
        App.saveallinfiles(self)

    def saveallinfiles(self):
        with open("list.txt", "w") as file:
            for folder_name in self.foldernames:
                file.write(folder_name + "\n")
        with open("name.txt", "w") as file:
            file.write(self.nom)

        App.startui(self)

    def startui(self):
        from visualgi import MyApp
        MyApp()

if __name__ == "__main__":
    App()