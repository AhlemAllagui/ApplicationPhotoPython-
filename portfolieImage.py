import tkinter as tk


from PIL import Image, ImageTk
#Image, ImageTk => 2 modules utiliser pour manipuler les images dans python ,notament tkinder
# from PIL import Image, ImageTk => de la bibliotheque Pillow nous allons importer 2 module
#-> module Image
#-> module ImageTK

class CarrouselApp:
    #	class CarouselApp: => nous permet de regrouper les données ( attribut) et la fonctionnalité associé ( les methodes )dans une seul entité .Cela nous permet de mieux organisée notre code et de rendre les intéraction entre les different élément plus clair et plus simple à géres .

    def __init__(self, master, images ):
        # master => la fenetre principale des tkinder
        #images => listes des chemins d'acces aux images à afficher dans le carousel
        self.master=master
        self.images=images
        self.current_image_index=0
        #  Nous allons initialiser l'image a 0
        self.canvas=tk.Canvas(master, width=400, height=600)
        self.canvas.pack()

        self.load_image(self.current_image_index)
#Nous crée nos 2 bouton ⇒ bouton  suivant , bouton précédent
        prev_button=tk.Button(master , text="Précédent ", command=self.show_prev_image)
        prev_button.pack(side=tk.LEFT)

        next_button=tk.Button(master , text="Suivant", command=self.show_next_image)
        next_button.pack(side=tk.RIGHT)
#Nous allons crée une méthode def load_image
    def load_image(self, index):
        image_path = self.images[index]
        image = Image.open(image_path)
        self.tk_image = ImageTk.PhotoImage(image.resize((400, 600)))
        self.canvas.create_image(0, 0, anchor=tk.NW , image=self.tk_image)

    def show_prev_image(self):
        self.current_image_index =-1
        if self.current_image_index <0:
            self.current_image_index=len(self.images)-1
        self.load_image(self.current_image_index)
    def show_next_image(self):
        self.current_image_index +=1
        if self.current_image_index >= len(self.images):
            self.current_image_index=0
        self.load_image(self.current_image_index)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Application Image")
    images = ["image-01.jpeg", "image-02.jpeg", "image-03.jpeg", "image-04.jpeg"]
    app = CarrouselApp(root, images)
    root.mainloop()