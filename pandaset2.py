import pandas as pd

df = pd.read_csv('länder.csv')
pd.set_option('display.max_columns', None)

country = df[['Country', 'Total Area']]
population = df[['Country', 'Pop']]
government = df[['Country', 'Government']]
multiLang = df[['Country', 'Multilingual']]
euMember = df[['Country', 'EU Member']]
demIndex = df[['Country', 'Democracy Index']]
totArea = df[['Country', 'Total Area']]
hdi = df[['Country', 'HDI']]
medianAge = df[['Country', 'Median Age']]
gdpCapita = df[['Country', 'GDP/Capita']]

# Kontrollerar om användaren vill att listan visas nedåt- eller uppåtgående. 0 = odefinierat, 1 = nedåt, 2 = uppåt
listDesAsc = 0






# Fråga om användaren vill se listan stigande eller fallande
def askDesOrAsc():
    global listDesAsc
    desOrAsc = input("Do you wish to see the list in descending or ascending order? (Des/Asc): ")
    if desOrAsc == "Des":
        listDesAsc = 1
    elif desOrAsc == "Asc":
        listDesAsc = 2
    else:
        print("Invalid input. Try again.")
        askDesOrAsc()


print(df[0:18])

constMonarchy = df[(df['Government'] == 'Constitutional Monarchy')]
unitaryConstMon = df[(df['Government'] == 'Unitary Constitutional Monarchy')]
Republic = df[(df['Government'] == 'Republic')]
federalRepublic = df[(df['Government'] == 'Federal Republic')]
semiPresRepublic = df[(df['Government'] == 'Semi-Presidential Republic')]
parliamentaryRepublic = df[(df['Government'] == 'Parliamentary Republic')]

# Fallande values
valuesByName_Asc = country.sort_values('Country')
valuesByHDI_Asc = hdi.sort_values('HDI')
valuesByGDP_Asc = gdpCapita.sort_values('GDP/Capita')
valuesByPop_Asc = population.sort_values('Pop')
valuesByMedianAge_Asc = medianAge.sort_values('Median Age')
valuesByDemIndex_Asc = demIndex.sort_values('Democracy Index')
valuesByEuMember_Asc = euMember.sort_values('EU Member')
valuesByMultiLang_Asc = multiLang.sort_values('Multilingual')
valuesByArea_Asc = totArea.sort_values('Total Area')

# Stigande values
valuesByName_Des = country.sort_values('Country', ascending=False)
valuesByHDI_Des = hdi.sort_values('HDI', ascending=False)
valuesByGDP_Des = gdpCapita.sort_values('GDP/Capita', ascending=False)
valuesByPop_Des = population.sort_values('Pop', ascending=False)
valuesByMedianAge_Des = medianAge.sort_values('Median Age', ascending=False)
valuesByDemIndex_Des = demIndex.sort_values('Democracy Index', ascending=False)
valuesByEuMember_Des = euMember.sort_values('EU Member', ascending=False)
valuesByMultiLang_Des = multiLang.sort_values('Multilingual', ascending=False)
valuesByArea_Des = totArea.sort_values('Total Area', ascending=False)

print(len(constMonarchy))
print(len(unitaryConstMon))
print(len(Republic))
print(len(federalRepublic))
print(len(semiPresRepublic))
print(len(parliamentaryRepublic))


def valuesByName():
    askDesOrAsc()
    if listDesAsc == 1:
        print(valuesByName_Des)
    elif listDesAsc == 2:
        print(valuesByName_Asc)



def valuesByHdi():
    print(valuesByHDI_Des)


def valuesByGdp():
    print(valuesByGDP_Des)


def valuesByPop():
    print(valuesByPop_Des)


def valuesByMedianAge():
    print(valuesByMedianAge_Des)
    print(valuesByDemIndex_Des)
    print(valuesByEuMember_Des)
    print(valuesByMultiLang_Des)
    print(valuesByArea_Des)

valuesByName()

