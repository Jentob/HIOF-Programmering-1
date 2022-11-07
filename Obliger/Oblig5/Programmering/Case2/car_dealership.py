from datetime import date

car_register = {
    "toyotaBZ4X": {
        "brand": "Toyota",
        "model": "Corolla",
        "price": 96_000,
        "year": 2012,
        "month": 8,
        "new": False,
        "km": 163_000
    },
    "pugeot408": {
        "brand": "Pugeot",
        "model": "408",
        "price": 330_000,
        "year": 2019,
        "month": 1,
        "new": False,
        "km": 40_000
    },
    "audiRS3": {
        "brand": "Audi",
        "model": "RS3",
        "price": 473_000,
        "year": 2022,
        "month": 2,
        "new": True,
        "km": 0
    },
}

NEW_CAR_REGISTRATION_FEE = 10783
RENT_CAR_PERCENTAGE = 0.4
RENT_NEW_CAR_FEE = 1000

CAR_FEE_0_3 = 6681
CAR_FEE_4_11 = 4034
CAR_FEE_12_29 = 1729
CAR_FEE_30 = 0


def print_car_information(car):
    # Oppgave 3.1
    print(f"Brand: {car['brand']}")
    print(f"Model: {car['model']}")
    print(f"Price: {car['price']},-")
    print(f"Manufactured: {car['year']}")
    print(f"Condition: {'New' if car['new'] else 'Used'}")
    print()

def create_car(car_register, key, brand, model, price, year, month, new, km):
    # Oppgave 3.2
    new_car = {
        key : {
            "brand": brand,
            "model": model,
            "price": price,
            "year": year,
            "month": month,
            "new": new,
            "km": km
        }
    }
    car_register.update(new_car)
    return new_car

def get_car_age(car):
    # Oppgave 3.3
    age = date.today().year - car["year"]
    return age

def next_eu_control(car):
    # Oppgave 3.4
    return date(car["year"] + 2, car["month"], 1)

def rent_car_monthly_price(car):
    # Oppgave 3.5
    price = car["price"] * RENT_CAR_PERCENTAGE / 12 + (RENT_NEW_CAR_FEE if car["new"] else 0)
    round(price, 2)
    return price

def calculate_total_price(car):
    # Oppgave 3.6
    price = car["price"]
    if car["new"]:
        price += NEW_CAR_REGISTRATION_FEE
        return price
    car_age = get_car_age(car)
    if car_age <= 3:
        price += CAR_FEE_0_3
        return price
    if car_age <= 11:
        price += CAR_FEE_4_11
        return price
    if car_age <= 29:
        price += CAR_FEE_12_29
        return price
    return price


def is_new(car):
    return car['new']

if __name__ == '__main__':
    create_car(car_register, "volvoV90", "Volvo", "V90", 850_000, 2021, 12, True, 0)


    toyota = car_register['toyotaBZ4X']

    print_car_information(toyota)

    print(f"\nThe total price for this {toyota['brand']} {toyota['model']} is {calculate_total_price(toyota)}kr.")
    print(f"Next EU-control for the {toyota['brand']} {toyota['model']} is {next_eu_control(toyota)}")
    print(f"If you want to rent the {toyota['brand']} {toyota['model']} the monthly fee will be {rent_car_monthly_price(toyota)}.")


    audi = car_register['audiRS3']

    print_car_information(audi)

    print(f"\nThe total price for this {audi['brand']} {audi['model']} is {calculate_total_price(audi)}kr.")
    print(f"Next EU-control for the {audi['brand']} {audi['model']} is {next_eu_control(audi)}")
    print(f"If you want to rent the {audi['brand']} {audi['model']} the monthly fee will be {rent_car_monthly_price(audi)}kr.")

class Car:
    def __init__(self, brand, model, price, year, month, new, km):
        self.brand = brand
        self.model = model
        self.price = price
        self.year = year
        self.month = month
        self.new = new
        self.km = km

    def print_car_information(self):
        pass

    def get_car_age(self):
        pass 

    def next_eu_control(self):
        pass

    def rent_car_monthly_price(self):
        pass 

    def calculate_total_price(self):
        pass
    # Jeg mener at alle disse metodene passer inn i klassen fordi de alle tar en car-dictionary som argument
