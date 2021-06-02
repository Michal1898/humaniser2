import csv
from random import choice, randrange, getrandbits
from datetime import timedelta, date

FEMALE = True
MALE = False

def random_person(sex=FEMALE, age_min = 1, age_max = 99, count=1):
    person={}
    start_date=date.today()-timedelta(365*age_max)
    end_date=date.today()-timedelta(365*age_min)
    #print( end_date, start_date)

    gender = sex

    print(gender, start_date, end_date, count)
    if gender==FEMALE:
        first_names_file="names_cr/krestni_zeny.csv"
        surnames_file="names_cr/prijmeni_zeny_1.csv"

    else:
        first_names_file = "names_cr/krestni_muzi.csv"
        surnames_file = "names_cr/prijmeni_muzi_1.csv"

    with open(first_names_file, encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        data = list(reader)

    first_names_list=data[:150]

    with open(surnames_file, encoding="utf-8", newline="") as f:
        reader = csv.reader(f)
        data = list(reader)

    surnames_list=data[:150]

    addresses=[]
    for adr_index in range(1,8):
        address_path="addresses_cr/adr_"+str(adr_index)+".csv"
        with open(address_path, encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            data = list(reader)
            addresses.extend(data[1:])

    human_list=[]
    for c in range(0,count):
        person= {}
        person["gender"] = gender

        random_first_name=choice(first_names_list)
        person["firstname"] = random_first_name[1]

        random_surname = choice(surnames_list)
        person["surname"] = random_surname[1]

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = randrange(days_between_dates)
        random_date = start_date + timedelta(days=random_number_of_days)
        person["birthdate"] = random_date.strftime("%d-%m-%Y")

        random_address=choice(addresses)
        random_address = random_address[0]
        random_address=random_address.split(";" , -1)

        person["city"] = random_address[0]
        person["street"] = random_address[1]
        person["house_no"] = random_address[2]
        person["plz"] = random_address[3]

        #print (person)
        human_list.append(person)

    #print(human_list)
    return human_list


a=random_person(MALE,18,30,300)
print(a)

a=random_person(FEMALE,18,30,300)
print(a)

