#reading the recipes .txt files
import pathlib

#reading the recipe .txt files
recipes = pathlib.Path("recipes").glob('*.txt')
data = ""
for p in recipes:
    data = data + p.read_text()

#Each recipe starts with the word Recipe. So, split on it to separate the recipes fetched
datanew = data.split("Recipe")

#removing empty data elements
for i in datanew:
    if len(i)==0:
        datanew.remove(i)

#removing the white spaces at the beginning
for i in range(len(datanew)):
    datanew[i] = datanew[i].lstrip()

#length of datanew should be equal to the number of recipes
print(len(datanew))

#print datanew to check if results are as required
print(datanew)

mylist = [""]*len(datanew)

#The files are not read in proper order. mylist is the list which has recipes in the proper order.
#For instance, mylist[0] has the 1st recipe, mylist[1] has the 2nd recipe and so on
for i in range(len(datanew)):
    a = datanew[i].split('\n')
    # b has the recipe number
    b = int(a[0])
    # mylist[0] should have the 1st recipe, so mylist[b-1] used
    mylist[b-1] = datanew[i]

#adding the word Recipe at the beginning of each recipe
for i in range(len(mylist)):
    mylist[i] = "Recipe " + mylist[i]

print(mylist)

#finding the names of each recipes
titles = [""]*len(mylist)

for i in range(len(mylist)):
    a = mylist[i].split("\n")
    #The element at the 3rd position should have the recipe name
    titles[i] = a[2]

print(titles)

outfile = open('Recipes_names.txt','w',encoding='utf-8')

for recipename in titles:
    print(recipename,file=outfile)

outfile.close()

#finding the number of ingredients in each recipe.
lines = [0]* len(mylist)

for i in range(len(mylist)):
    #remove trailing white spaces
    recipe = mylist[i].rstrip()
    recipelines = recipe.split("\n")
    #we do not want to count empty lines
    for j in recipelines:
        if len(j)==0:
            recipelines.remove(j)
    #the first is Recipe RecipeNumber and second line is the title, so 2 needs to be subtracted
    lines[i] = len(recipelines)-2

# printing the lines (ingredients)
print(lines)

#producing the required output file with 2 columns - Recipe name and the number of ingredients
import csv

rows = []
for i in range(len(mylist)):
   row = [titles[i],lines[i]]
   rows.append(row)

outfile = open('RecipeAndIngredients.csv','w', encoding='utf-8', newline='')
csvout = csv.writer(outfile)
csvout.writerow(['Recipe name', 'Number of ingredients'])
csvout.writerows(rows)
outfile.close()

#finding the recipe with least ingredients
minrecipepos = 0
for i in range(len(lines)):
    #finding the position of the recipe with least ingredient (lines)
    if lines[i] == min(lines):
        minrecipepos = i

print(minrecipepos)

#printing the name of  the recipe with least ingredients along with thr number of ingredients
print("The recipe with least ingredients is : Recipe", minrecipepos+1, " - ",titles[minrecipepos], ", which has ", lines[minrecipepos], " ingredients")

#finding the recipes which have ingredients that are optional
blanks = []

for i in range(len(mylist)):
    #a stores the words in each recipe
    a = mylist[i].split()
    for j in a:
        #look for the work 'optional', if found append the position to 'blanks'
        if j == "optional":
            blanks.append(i)
            break

#finding the names of the recipes that have optional ingredients
optrecipe = [""] * len(blanks)
for i in range(len(blanks)):
    a = blanks[i]
    optrecipe[i] = titles[a]

print(optrecipe)

# print("The recipes which have optional ingredients are -")
# for i in blanks:
#     print(titles[i])

#producing a .txt file that stores the recipe names which have one or more optional ingredients
outfile = open('Recipes_with_Optional_Ingredients.txt','w',encoding='utf-8')

for recipename in optrecipe:
    print(recipename,file=outfile)

outfile.close()

#finding and printing the Recipe name and its optional ingredients
for i in range(len(blanks)):
    a = blanks[i]
    print("Optional ingredient(s) in Recipe ", a+1,'-',titles[a], "are :")
    #fetch the required recipes and split them to find each line
    b = mylist[a].split("\n")
    #loop through each line of the recipe
    for j in b:
        #find words in each line using split
        d = j.split()
        #loop through each word
        for e in d:
            #if the word 'optional' is found, print the entire line
            if e == "optional":
                print(j)
    print("\n")

#finding the recipes that have fruits
fruits = ["banana","apple","mango","strawberry","pineapple","orange","blueberry","grape"]

frt = []

for i in range(len(mylist)):
    #in each recipe, split each word
    a = mylist[i].split()
    #loop though each word
    for j in a:
        #if the word in a recipe is found in the fruits list, append the position
        if j in fruits:
            frt.append(i)
#print(frt)

#finding the title of the recipes which have fruits in the ingredients
fruitrecipe = [""] * len(frt)
for i in range(len(frt)):
    a = frt[i]
    fruitrecipe[i] = titles[a]

print("The recipes which have fruits are -")
print(fruitrecipe)

#finding the recipes that use potato
potato =[]

for i in range(len(mylist)):
    #split each word
    a = mylist[i].split()
    #loop through each word in a recipe
    for j in a:
        if j == "potato":
            #if word found, append to the list
            potato.append(i)
#print(potato)

#find the recipe name of the recipe which use potato
potatorecipe = [""] * len(potato)
for i in range(len(potato)):
    a = potato[i]
    #finding the recipe names
    potatorecipe[i] = titles[a]

print("The recipes that use potato are - ")
print(potatorecipe)

#finding the total quantity of salt used in all the recipes
salt =[""]

for i in range(len(mylist)):
    #find each line of a recipe
    b = mylist[i].split("\n")
    #loop through each line
    for j in b:
        d = j.split()
        #loop through each word
        for e in d:
            #find the word salt
            if e == "salt":
                #if the word salt is found, append its position
                salt.append(j)

#remove empty spaces
for i in salt:
    if len(i) == 0:
        salt.remove(i)

#print(salt)

totalsalt = 0
for i in range(len(salt)):
    a = salt[i]
    #split each word
    #each line begins with the salt quantity
    quantity = a.split()[0]
    #the quanity is converted to float and the fractional quantities are converted to decimal
    quantity = float(quantity.replace("1/4","0.25").replace("1/2","0.5").replace("3/4","0.75"))
    #the quanities are all added up to find the total quantity
    totalsalt = totalsalt + quantity

print("The total quantity of salt used in all the recipes is ", totalsalt, " table spoons")
