# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def iterate():
    for number in range(0,6,2):
        print(number)

def diccionarios():
    ejemplo_diccionario = {
        "str": "stringg",
        "float": 1.256,
        "int": 1,
    }

    for key, val in ejemplo_diccionario.items():
        print(f'{key}={val}')

def sets():
    set = {"a", "b", "c"}
    for s in set:
        print(s)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Calliope')
    # print('<3')
    # iterate()
    sets()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
