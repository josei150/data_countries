import re
import matplotlib.pylab as plt
import csv

def get_country(country):
    with open("./data_countries.csv") as data:
        countries = csv.reader(data, delimiter=",")
        labels = next(countries)
        population_label = re.findall("[\d]+ Population", ",".join(labels))
        population = []
        result = []
        print(labels)
        for data_country in countries:
            result.append(dict(zip(labels, data_country)))
        
        find_country = list(filter(lambda x: x["Country"].lower() == country.lower(), result))
        find_country = find_country[0] if len(find_country) else []
        
        if find_country:
            for label in population_label:
                population.append(int(find_country[label]))
        else:
            raise KeyError("Pais no encontrado")
        
        population_label = re.findall("[\d]+", ",".join(population_label))
        population_label.reverse()
        population.reverse()

        return population_label, population


def chart_population(country, labels, population):
    fig, data = plt.subplots()
    data.bar(labels, population)
    data.set_title(f"Population in {country}")
    data.set_xlabel("Year")
    data.set_ylabel("Population")
    plt.show()

def chart_percentage_population(labels, population):
    fig, data = plt.subplots()
    data.pie(population, labels = labels)
    data.set_title("Percentage world population")
    plt.show()

def get_world_poputaion_percentage():
    list_data_countries = []
    name_countries = []
    percentage_for_country = []
    with open("./data_countries.csv") as data_country:
        countries = csv.reader(data_country, delimiter=",")
        labels = next(countries)

        for data in countries:
            list_data_countries.append(dict(zip(labels, data)))
        
        for data in list_data_countries:
            name_countries.append(data["Country"])
            percentage_for_country.append(data["World Population Percentage"])
        
    return name_countries, percentage_for_country

if __name__ == "__main__":
    country = input("Dime el país: ")
    wrong_country = True

    while wrong_country:
        try:
            labels, population = get_country(country)
            chart_population(country, labels=labels, population=population)
            names_countries, percentage = get_world_poputaion_percentage()
            chart_percentage_population(names_countries, percentage)
            wrong_country = False
        except KeyError as error:
            print(error)
            country = input("Dime el país: ")
