from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 16", +79991234567),
    Smartphone("Samsung", "Galaxy A56", +79999999999),
    Smartphone("Xiaomi", "15", +79997894563),
    Smartphone("Poco", "X7", +791234567890),
    Smartphone("Huawei", "Pura 70", +79991234569)
]

for i in catalog:
    print(i.str())
