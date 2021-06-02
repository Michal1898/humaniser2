import csv
from random import choice, randrange, getrandbits
from datetime import timedelta, date

def random_person():
    person={}
    FEMALE=True
    MALE=False
    START_DATE=date(1930,1,1)
    END_DATE=date(2016,1,1)

    gender = getrandbits(1)
    person["gender"]=gender

    if gender==FEMALE:
        first_names_file="names_cr/krestni_zeny.csv"
        surnames_file="names_cr/prijmeni_zeny_1.csv"

    else:
        first_names_file = "names_cr/krestni_muzi.csv"
        surnames_file = "names_cr/prijmeni_muzi_1.csv"

    with open(first_names_file, encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        data = list(reader)
    random_first_name=choice(data[:150])
    person["firstname"] = random_first_name[1]

    with open(first_names_file, encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        data = list(reader)

    random_surname = choice(data[:250])
    person["surname"] = random_surname[1]


    time_between_dates = END_DATE - START_DATE
    days_between_dates = time_between_dates.days
    random_number_of_days = randrange(days_between_dates)
    random_date = START_DATE + timedelta(days=random_number_of_days)
    person["birthdate"] = random_date.strftime("%d-%m-%Y")

    addresses=[]
    for adr_index in range(1,8):
        address_path="addresses_cr/adr_"+str(adr_index)+".csv"
        with open(address_path, encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            data = list(reader)
            addresses.extend(data[1:])

    random_address=choice(addresses)
    random_address = random_address[0]
    random_address=random_address.split(";" , -1)

    person["city"] = random_address[0]
    person["street"] = random_address[1]
    person["house_no"] = random_address[2]
    person["plz"] = random_address[3]


    return person

for b in range (1,500):
    a=random_person()
    print(a)


