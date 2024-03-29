from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.geometry('400x200')

def graph():
    # Create fake data   
    house_prices = np.random.normal(200000, 25000, 5000) # First parameter is the center
    plt.hist(house_prices, 100) # How many bins          # Second is the deviation(αποκλιση)
                                                         # Thirds is the size, changew 

    plt.show()

Button(root, text='Chart', command=graph).pack()

root.mainloop()


