#########################################
# groupe 6
# Gaudiniere Nathan
# Lawson Late Patrick
# Said Hassani Samia
# https://github.com/uvsq22103955/Projet_tas_de_sable
#########################################


from tkinter import * 


fenetre = Tk()

# label
label = Label(fenetre, text="Bot tas de sable", bg="green")
label.pack()
# canvas
canvas = Canvas(fenetre, width=900, height=900, background='white')
ligne1 = canvas.create_line(700, 700, 700, 200)
ligne2 = canvas.create_line(600, 700, 600, 200)
ligne3 = canvas.create_line(500, 700, 500, 200)
ligne4 = canvas.create_line(400, 700, 400, 200)
ligne5 = canvas.create_line(300, 700, 300, 200)
ligne6 = canvas.create_line(200, 700, 200, 200)

ligne7 = canvas.create_line(200, 700, 700, 700)
ligne8 = canvas.create_line(200, 600, 700, 600)
ligne9 = canvas.create_line(200, 500, 700, 500)
ligne10 = canvas.create_line(200, 400, 700, 400)
ligne11= canvas.create_line(200, 300, 700, 300)
ligne12= canvas.create_line(200, 200, 700, 200)
canvas.pack()
fenetre.mainloop()
