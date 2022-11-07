#------------------------------------------
#Oppgaver
#------------------------------------------
def print_ware_information(ware):
    '''Funksjonsbeskrivelse: Printer ut informasjon om en spesifisert vare.'''
    print(f"Name: {ware['name']}")
    print(f"Price: {ware['price']}")
    print(f"Number in stock: {ware['number_in_stock']}")
    print(f"Description: {ware['description']}")
    print()

def calculate_average_ware_rating(ware):
    ''''Returnerer den gjennomsnittlige ratingen for en spesifisert vare.'''
    try:
        avg = sum(ware["ratings"]) / len(ware["ratings"])
    except ZeroDivisionError:
        avg = 0
    return avg
def get_all_wares_in_stock(all_wares):
    '''Returnerer en dictionary med alle varer som er på lager.'''
    wares_in_stock = {}
    for ware in all_wares:
        if all_wares[ware]["number_in_stock"]:
            wares_in_stock[ware] = all_wares[ware]
    return wares_in_stock

def is_number_of_ware_in_stock(ware, number_of_ware):
    '''Returnerer en Boolean-verdi som representerer om et spesifisert antall av en gitt vare finnes på lager.'''
    if ware["number_in_stock"] >= number_of_ware:
        return True
    return False

def add_number_of_ware_to_shopping_cart(ware_key, ware, shopping_cart, number_of_ware=1):
    '''Legger til et spesifisert antall av en gitt vare i en spesifisert handlevogn.'''
    if not is_ware_in_stock(ware):
        return print(f"{ware['name']} is not in stock and could not be added to the shopping cart.")
    if not is_number_of_ware_in_stock(ware, number_of_ware):
        shopping_cart.update({ware_key : ware["number_in_stock"]})
        return print(f"Only {ware['number_in_stock']} instance(s) of {ware['name']} were in stock. These were added to the shopping cart.")
    shopping_cart.update({ware_key : number_of_ware})
    print(f"{number_of_ware} instance(s) of {ware['name']} were added to the shopping cart. ")


def calculate_shopping_cart_price(shopping_cart, all_wares, tax):
    '''Returnerer prisen av en handlevogn basert på varene i den.'''
    price = 0
    for ware in shopping_cart:
        price += all_wares[ware]["price"] * shopping_cart[ware] * tax
    return price

def can_afford_shopping_cart(shopping_cart_price, wallet):
    '''Returnerer en Boolean-verdi basert på om det er nok penger i en gitt lommebok for å kjøpe en handlevogn.'''
    if wallet >= shopping_cart_price:
        return True
    return False

def buy_shopping_cart():
    '''Kjøper varene i en handlevogn. Parameterene defineres i oppgaven.'''

#------------------------------------------
# Predefinerte funksjoner
#------------------------------------------
def is_ware_in_stock(ware):
    '''Returnerer en Boolean-verdi som representerer om en vare er på lager.'''
    if ware["number_in_stock"] >= 1:
        return True
    else:
        return False

def clear_shopping_cart(shopping_cart):
    '''Tømmer en handlevogn.'''
    shopping_cart.clear()