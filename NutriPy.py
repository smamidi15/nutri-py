"""
NutriPy: A Personalized Nutrition Calculator
By Madhav P, Ram K, Brandon P, and Sreyansh M
4/11/2021

"""

import csv
import tkinter as tk
from tkinter import *
import math
import pandas as pd
import numpy as np

def round_half_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier

def caloriecalc(age,weight,gender,height,activity,need):
  if gender == 1:
    BMR = 66 + (6.3 * weight) + (12.9 * height) - (6.8 * age)
    if activity == 1:
      if need == 1:
        calorie = BMR*1.2 - 250
      elif need == 2:
        calorie = BMR*1.2
      else:
        calorie = BMR*1.2 + 250
    elif activity == 2:
      if need == 1:
        calorie = BMR*1.375 - 250
      elif need == 2:
        calorie = BMR*1.375
      else:
        calorie = BMR*1.375 + 250
    elif activity == 3:
      if need == 1:
        calorie = BMR*1.55 - 250
      elif need == 2:
        calorie = BMR*1.55
      else:
        calorie = BMR*1.55 + 250
    elif activity == 4:
      if need == 1:
        calorie = BMR*1.725 - 250
      elif need == 2:
        calorie = BMR*1.725
      else:
        calorie = BMR*1.725 + 250
    else:
      if need == 1:
        calorie = BMR*1.9 - 250
      elif need == 2:
        calorie = BMR*1.9
      else:
        calorie = BMR*1.9 + 250
  else:
    BMR = 655 + (4.3 * weight) + (4.7 * height) - (4.7 * age)
    if activity == 1:
      if need == 1:
        calorie = BMR*1.2 - 250
      elif need == 2:
        calorie = BMR*1.2
      else:
        calorie = BMR*1.2 + 250
    elif activity == 2:
      if need == 1:
        calorie = BMR*1.375 - 250
      elif need == 2:
        calorie = BMR*1.375
      else:
        calorie = BMR*1.375 + 250
    elif activity == 3:
      if need == 1:
        calorie = BMR*1.55 - 250
      elif need == 2:
        calorie = BMR*1.55
      else:
        calorie = BMR*1.55 + 250
    elif activity == 4:
      if need == 1:
        calorie = BMR*1.725 - 250
      elif need == 2:
        calorie = BMR*1.725
      else:
        calorie = BMR*1.725 + 250
    else:
      if need == 1:
        calorie = BMR*1.9 - 250
      elif need == 2:
        calorie = BMR*1.9
      else:
        calorie = BMR*1.9 + 250
  calorie = round_half_up(calorie,0)
  return calorie

def macrocontent(n,need):
  if need == 1:
    protein = n*30/100
    carbs = n*40/100
    fats = n*30/100
  elif need == 2:
    protein = n*20/100
    carbs = n*55/100
    fats = n*25/100
  else:
    protein = n*40/100
    carbs = n*30/100
    fats = n*30/100
  return round_half_up(protein,0),round_half_up(carbs,0),round_half_up(fats,0)

# FoodCategory is a class for each group of foods
# A FoodCategory class will contain a list of Food objects
class FoodCategory:
  def __init__(self, name, foods):
    self.name = name
    self.foods = foods
  def __str__(self):
    output = "The " + self.name + "food category consists of these foods:\n" + self.foods
    return output
  def add_food(self, food):
    self.foods.append(food)

# Defines the Food class
class Food:
  def __init__(self, name, calories, fat, protein, carbohydrates, sugars, cholestrol, saturated_fats, calcium, sodium):
    self.name = name
    self.cals = calories
    self.fat = fat
    self.protein = protein
    self.carbs = carbohydrates
    self.sugars = sugars
    self.chol = cholestrol
    self.sat_fats = saturated_fats
    self.calc = calcium
    self.sod = sodium

  def __str__(self):
    output = "I'm this food: " + self.name
    return output

# Reads the CSV file
with open('MyFoodData Sorted Nutrition Facts.csv', 'r') as data_file:
  reader = csv.reader(data_file, delimiter=",")
  col_titles = next(reader)

  name_list = []
  cat_list = []
  counter = 0
  for row in reader:
    if counter == 0:
      next(reader)
    counter += 1

    cat_name = row[2]
    if cat_name not in name_list:
        name_list.append(cat_name)
        food_list = []
        c = FoodCategory(cat_name, food_list)
        cat_list.append(c)

    f = Food(row[1], float(row[3]), float(row[4]), float(row[5]), float(row[6]), float(row[7]), row[9], row[10], row[11], row[12])
    for group in cat_list:
      if group.name == cat_name:
        group.add_food(f)
        break

short_cat_list = ["Baked Foods", "Snacks", "Sweets", "Vegetables", "Beverages", "Fats/Oils", "Meats", "Dairy/Eggs", "Cereals", "Soup/Sauces", "Beans/Lentils","Fish", "Fruits", "Grains/Pasta", "Nuts/Seeds", "Spices/Herbs", "More Dairy"]


num1 = 0
num2 = 0
num3 = 0
num4 = 0
string1 = ""
string2 = ""
def create_base_gui():
  gui = Tk()
  gui.geometry("500x350")
  gui.title("Food Categories Picker")

  title = Label(gui, text="Food Categories Picker", width=20, font=("bold", 16))
  title.place(x=130,y=20)

  for i in range(5):
    Label(gui, text=f'{short_cat_list[i]}', width=10, font=("bold", 8)).place(x=10+i*100, y=80)

  n1 = 0
  for j in range(5,10):
    Label(gui, text=f'{short_cat_list[j]}', width=10, font=("bold", 8)).place(x=10+n1*100, y=140)
    n1 += 1

  n2 = 0
  for k in range(10,15):
    Label(gui, text=f'{short_cat_list[k]}', width=10, font=("bold", 8)).place(x=10+n2*100, y=200)
    n2 += 1

  n3 = 0
  for m in range(15,17):
    Label(gui, text=f'{short_cat_list[m]}', width=10, font=("bold", 8)).place(x=145+n3*125, y=260)
    n3 += 1

  gr = StringVar()
  dropdown = OptionMenu(gui, gr, *short_cat_list)
  dropdown.config(width=25)
  gr.set("Select a Food Category")
  dropdown.place(x=15, y=310)

  def submit_choice():
    gui.destroy()
    create_second_gui(gr.get())

  def click_done():
    gui.destroy()
    create_inter_gui()

  Button(gui, text="Submit", width=10, bg="green", fg="white", command=lambda: submit_choice()).place(x=250,y=310)
  Button(gui, text="Done", width=10, bg="red", fg="white", command=lambda: click_done()).place(x=350,y=310)

  gui.mainloop()

chosen_foods = []

def create_second_gui(food_group):
  g = Tk()
  g.geometry("500x250")
  g.title(food_group)

  title = Label(g, text=food_group, width=20, font=("bold", 16))
  title.place(x=130,y=20)

  Label(g, text="Type a Food to Search For:", width=25, font=("bold", 10)).place(x=15, y=60)

  search_entry = Entry(g)
  search_entry.place(x=205,y=60)

  foods = []
  foodsExist = False

  fo1 = StringVar()
  fo2 = StringVar()

  def find_food(name):
    for f in foods:
      if f.name == name:
        return f

  def go_back():
    g.destroy()
    create_base_gui()

  def submit_go_back():      
    if fo1.get() != "Food Choice 1":
      foo1 = find_food(fo1.get())
      chosen_foods.append(foo1)

    if fo2.get() != "Food Choice 2":
      foo2 = find_food(fo2.get())
      chosen_foods.append(foo2)

    g.destroy()
    create_base_gui()

  def show_dropdowns():
      names = [f.name for f in foods]

      dropd1 = OptionMenu(g, fo1, *names)
      dropd1.config(width=30)
      fo1.set("Food Choice 1")
      dropd1.place(x=20, y=125)

      dropd2 = OptionMenu(g, fo2, *names)
      dropd2.config(width=30)
      fo2.set("Food Choice 2")
      dropd2.place(x=270, y=125)

      Button(g, text="Submit", width=10, bg="green", fg="white", command=lambda: submit_go_back()).place(x=180,y=175)
      Button(g, text="Go Back", width=10, bg="red", fg="white", command=lambda: go_back()).place(x=270,y=175)
  
  def search():
    response = search_entry.get()
    for c in cat_list:
      if c.name == food_group:
        cat = c
        break
    for f in c.foods:
      if response.lower() in f.name.lower():
        foods.append(f)
    
    if len(foods) != 0:
      Label(g, text=f'There are {str(len(foods))} matches!', width=30, font="Arial 10 bold").place(x=125, y=95)
      foodsExist = True
      show_dropdowns()
    else:
      Label(g, text="Choose a different word - 0 matches!", width=30, font="Arial 10 bold").place(x=125, y=95)
        
  Button(g, text="Search", width=10, bg="green", fg="white", command=lambda: search()).place(x=340,y=60)
  g.mainloop()

serving_sizes = []

def create_inter_gui():
  it = Tk()
  it.geometry("500x300")
  it.title("Selected Foods/Amounts")

  title = Label(it, text="Chosen Foods/Amounts", width=20, font=("bold", 16))
  title.place(x=125,y=20)

  des = Label(it, text="One serving is 100 g, enter the # of servings", width=40, font=("bold", 10))
  des.place(x=90,y=50)

  food_names = [f.name for f in chosen_foods]
  fo = StringVar()
  dropd = OptionMenu(it, fo, *food_names)
  dropd.config(width=30)
  fo.set("Food Choice")
  dropd.place(x=20,y=80)

  entry = Entry(it)
  entry.place(x=275,y=85)  

  def go_to_next():
    en_input = entry.get()
    serving_sizes.append(float(en_input))
    entry.delete(0, "end")
    fo.set("Food Choice")

  def go_to_end():
    it.destroy()
    create_recommendation_gui()

  Button(it, text="Next", width=10, bg="green", fg="white", command=lambda: go_to_next()).place(x=150,y=120)
  Button(it, text="Done", width=10, bg="red", fg="white", command=lambda: go_to_end()).place(x=250,y=120)

  it.mainloop()

def create_nutrition_gui():
    calc = Tk()

    calc.geometry("500x500")

    calc.title('Nutrition Calculator')

    label_0 = Label(calc,text="Nutrition Calculator", width=20,font=("bold",20))
    label_0.place(x=90,y=30)

    label_1 = Label(calc,text="Age (years)", width=20,font=("bold",10))
    label_1.place(x=80,y=100)

    entry_1 = Entry(calc)
    entry_1.place(x=240,y=100)

    label_3 = Label(calc,text="Height (inches)", width=20,font=("bold",10))
    label_3.place(x=68,y=150)

    entry_3= Entry(calc)
    entry_3.place(x=240,y=150)

    label_5 = Label(calc,text="Weight (lbs)", width=20,font=("bold",10))
    label_5.place(x=68,y=200)

    entry_5= Entry(calc)
    entry_5.place(x=240,y=200)

    label_4 =Label(calc,text="Gender", width=20,font=("bold",10))
    label_4.place(x=70,y=250)

    var=IntVar()

    Radiobutton(calc,text="Male",padx= 5, variable = var, value=1).place(x=235,y=250)
    Radiobutton(calc,text="Female",padx= 10, variable= var, value=2).place(x=300,y=250)

    label_6=Label(calc,text="Amount of Activity",width=20,font=("bold",10))
    label_6.place(x=70,y=300)

    list_of_activity=[ 'none or little' ,'1-3 days/week' , '3-5 days/week' ,'6-7 days/week' ,'extreme']

    activ =StringVar()
    droplist=OptionMenu(calc,activ, *list_of_activity)
    droplist.config(width=20)
    activ.set('Select Activity Level')
    droplist.place(x=240,y=300)


    label_7 = Label(calc,text="Goal", width=20,font=("bold",10))
    label_7.place(x=70,y=335)

    list_of_goal=[ 'Lose Weight' ,'Maintain Weight' , 'Gain Weight']

    goa = StringVar()
    droplist=OptionMenu(calc,goa, *list_of_goal)
    droplist.config(width=20)
    goa.set('Select Goal')
    droplist.place(x=240,y=335)

    def nextstep():
        calc.destroy()
        create_base_gui()

    def submit():
        num1 = int(entry_1.get())
        num2 = int(entry_5.get())
        num3 = var.get()
        num4 = int(entry_3.get())
        string1 = activ.get()
        if string1 == "none or little":
            string1 = 1
        elif string1 == "1-3 days/week":
            string1 = 2
        elif string1 == "3-5 days/week":
            string1 = 3
        elif string1 == "6-8 days/week":
            string1 = 4
        elif string1 == "extreme":
            string1 = 5
        string2 = goa.get()
        if string2 == "Lose Weight":
            string2 = 1
        elif string2 == "Maintain Weight":
            string2 = 2
        elif string2 == "Gain Weight":
            string2 = 3
        calculations = ("Calories Needed: " + str(caloriecalc(num1,num2,num3,num4,string1,string2)) + "\n" + 
                        "Protein Calories: " + str(macrocontent(caloriecalc(num1,num2,num3,num4,string1,string2),string2)[0]) + "\n" + 
                        "Carbs Calories: " + str(macrocontent(caloriecalc(num1,num2,num3,num4,string1,string2),string2)[1]) + "\n" + 
                        "Fats Calories: " + str(macrocontent(caloriecalc(num1,num2,num3,num4,string1,string2),string2)[2]))
        
        label = Label(calc, text=calculations,width=50,font=("bold",10))
        label.place(x=50,y=410)
        submitbut.destroy()
        Button(calc, text='Next Step' , width=20,bg="white",fg='black',command = lambda: nextstep()).place(x=180,y=380)


    submitbut = Button(calc, text='Submit' , width=20,bg="white",fg='black',command = lambda: submit())
    submitbut.place(x=180,y=380)

    calc.mainloop()
    return caloriecalc(num1,num2,num3,num4,string1,string2)

nutrition = pd.read_csv(r".\MyFoodData Sorted Nutrition Facts.csv")
def tier_system():
  with open('MyFoodData Sorted Nutrition Facts.csv', 'r') as data_file:
    nutrition['Saturated Fats (g)'] = nutrition['Saturated Fats (g)'].fillna(0)
    nutrition.insert(8, "Tier", 1)

    conditions = [
(nutrition['Sodium (mg)'] > 1100),
(nutrition['Cholesterol (mg)'] > 100),
(nutrition['Saturated Fats (g)'] > 10),
(nutrition['Sugars (g)'] > 18),
(nutrition['Saturated Fats (g)'] > 5),
(nutrition['Cholesterol (mg)'] > 50),
(nutrition['Sodium (mg)'] > 550),
(nutrition['Sugars (g)'] >9),
((nutrition['Saturated Fats (g)'] > 5) & (nutrition['Sugars (g)'] >9 ) & (nutrition['Sodium (mg)'] > 550)), 
((nutrition['Saturated Fats (g)'] > 5) & (nutrition['Sugars (g)'] >9 ) & (nutrition['Cholesterol (mg)'] > 50)),
((nutrition['Sodium (mg)'] > 550) & (nutrition['Sugars (g)'] >9 ) & (nutrition['Cholesterol (mg)'] > 50)),  
((nutrition['Saturated Fats (g)'] > 5) & (nutrition['Sodium (mg)'] >550 ) & (nutrition['Cholesterol (mg)'] > 50))
]
    choices = [3,3,3,3,2,2,2,2,3,3,3,3]

    nutrition['Tier'] = np.select(conditions, choices, default=1)
    nutrition.head()

def create_recommendation_gui():
    # Label(recg, text="To fulfill your caloric needs, you can eat: ", width=25, font=("bold", 10)).place(x=15, y=60)
    # y1 = 60
    
    tier_system()
    protein = 0
    fats = 0
    carbs = 0
    for i in range(len(chosen_foods)):
        protein = protein + (chosen_foods[i].protein * serving_sizes[i])
        fats = fats + (chosen_foods[i].fat * serving_sizes[i])
        carbs = carbs + (chosen_foods[i].carbs * serving_sizes[i])
    protein_cal = protein * 4   
    carb_cal = carbs * 4
    fats_cal = fats * 9

    if (protein_cal < (macrocontent(caloriecalc(num1,num2,num3,num4,string1,string2),string2)[0])):
        temp = (macrocontent(caloriecalc(num1,num2,num3,num4,string1,string2),string2)[0]) - protein_cal
        print ("You need ",temp," calories from protein")
        print ("Here are some recommendations:\n")
        count = 0
        for i in range(1000):
            if ( (nutrition['Protein (g)'][i] > 20) & (nutrition['Tier'][i] == 1 )):
                print ("One serving of ",nutrition['Name'][i], " contains ", (nutrition['Protein (g)'][i]*4)," calories of protein")
                count += 1
                if count > 5:
                    break
    print("")
    if (carb_cal < (macrocontent(caloriecalc(num1,num2,num3,num4,string1,string2),string2)[1])):
        temp = (macrocontent(caloriecalc(num1,num2,num3,num4,string1,string2),string2)[1]) - carb_cal
        print ("You need ",temp," calories from carbohydrates")
        print ("Here are some recommendations:\n")
        count = 0
        for i in range(1000):
            if ( (nutrition['Carbohydrate (g)'][i] > 70) & (nutrition['Tier'][i] == 1 )):
                print ("One serving of ",nutrition['Name'][i], " contains ", (nutrition['Carbohydrate (g)'][i]*4)," calories of carbohydrates")
                count += 1
                if count > 5:
                    break
    print("")
    if (fats_cal < (macrocontent(caloriecalc(num1,num2,num3,num4,string1,string2),string2)[2])):
        temp = (macrocontent(caloriecalc(num1,num2,num3,num4,string1,string2),string2)[2]) - fats_cal
        print ("You need ",temp," calories from fats")
        print ("Here are some recommendations:\n")
        count = 0
        for i in range(1000):
            if ( (nutrition['Fat (g)'][i] > 20) & (nutrition['Tier'][i] == 1 )):
                print ("One serving of ",nutrition['Name'][i], " contains ", (nutrition['Fat (g)'][i]*9)," calories of fats")
                count += 1
                if count > 5:
                    break

    end = Tk()
    end.geometry("500x150")
    end.title("Thank You")

    label_0 = Label(end,text="Look at the Terminal!", width=20,font=("bold",16))
    label_0.place(x=120,y=20)

    des1 = Label(end, text="Info about fulfilling your caloric needs are there.", width=40, font=("bold", 10))
    des1.place(x=90,y=50)

    des2 = Label(end, text="Thank you for using NutriPy!", width=40, font=("bold", 10))
    des2.place(x=90,y=75)

    end.mainloop()  


create_nutrition_gui()
