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

if __name__ == "__main__":
    country = input("Dime el país: ")
    wrong_country = True

    while wrong_country:
        try:
            labels, population = get_country(country)
            chart_population(country, labels=labels, population=population)
            wrong_country = False
        except KeyError as error:
            print(error)
            country = input("Dime el país: ")
