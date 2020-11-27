import csv

def read_csv():
    with open('../data/mascotas.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            print("Nombre: {0}, Especie: {1}, Color: {2}, Sexo: {3}".format(row[0], row[1], row[2], row[3]))

def leer_csv():
    path_archivo = '../data/mascotas.csv'
    with open(path_archivo, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            print(line)

def leer_csv_dicc():
    path_archivo = '../data/mascotas.csv'
    with open(path_archivo, 'r') as csv_file:
        dic_reader = csv.DictReader(csv_file)
        for map in dic_reader:
            print(map)

# web services cualquier servicio web al que puedo acudir para sacar datos
# REST, SOAP


if __name__ == '__main__':
    leer_csv_dicc()
