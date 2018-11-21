from faker import Faker
from datetime import timedelta
from random import *
import csv

fake = Faker()

customers_list = []
reservation_list = []
payment_list = []
card_list = []
address_list = []
postalCode_list = []
guest_list = []

'''
Customer
'''
for i in range(5000):
    # Create name first and last
    name = fake.name()
    tempList = name.split()

    firstName = tempList[0]
    lastName = tempList[1]

    # Create email
    emailA = firstName + lastName + str(randint(0,100)) + "@gmail.com"

    # Create phone number
    phoneNumber = randint(1000000000,9999999999)

    # Make customer object
    class Customers:
        def __init__(self, fName, lName, phoneNum, email):
            self.fName = firstName
            self.lName = lastName
            self.phoneNum = phoneNumber
            self.email = emailA


    customers_list.append(Customers(firstName, lastName, phoneNumber, emailA))

    '''
    Reservations
    '''
    # Check in
    In = fake.date_this_decade(before_today=True, after_today=False)

    # Check out
    stayDurationRand = randint(1, 5)
    Out = In + timedelta(days=stayDurationRand)

    # Has Paid
    paidRand = randint(0, 1)
    hasPaidList = [True, False]
    paid = hasPaidList[paidRand]

    # Special Request
    sr = fake.sentence()


    class Reservations:
        def __init__(self, checkIn, checkOut, hasPaid, specialRequest):
            self.checkIn = In
            self.checkOut = Out
            self.hasPaid = paid
            self.specialRequest = sr

    reservation_list.append(Reservations(In, Out, paid, sr))

    '''
    Payment
    '''
    # Amount paid
    stay = Out - In
    tempStay = str(stay)
    stay = int(tempStay[0])

    amountA = 80 * stay * 1.13  # Base price multiplied by the duration of the stay and the tax rate

    # Date paid
    dateP = In
    randDateSelector = randint(0, 1)
    if randDateSelector == 1:
        dateP = Out

    class Payments:
        def __init__(self, amount, datePaid):
            self.amount = amountA
            self.datePaid = dateP

    payment_list.append(Payments(amountA, dateP))

    '''
    Card Details
    '''
    # Card Number
    cardTypeList = ['visa', 'mastercard', 'amex']
    cardRandSelector = randint(0, 2)
    cardN = fake.credit_card_number(card_type=cardTypeList[cardRandSelector])

    # CCV
    securityCode = fake.credit_card_security_code(card_type=cardTypeList[cardRandSelector])

    # holderFName = same as fName
    # holderLName = same as lName

    # Card Type
    ct = cardTypeList[cardRandSelector]


    class Cards:
        def __init__(self, cardNum, CCV, holderFName, holderLName, cardType):
            self.cardNum = cardN
            self.CCV = securityCode
            self.holderFName = firstName
            self.holderLName = lastName
            self.cardType = ct


    card_list.append(Cards(cardN, securityCode, firstName, lastName, ct))

    '''
    Address
    '''
    # Create address
    streetNum = fake.building_number()
    streetA = fake.street_name()
    cityA = fake.city()
    stateA = fake.state()
    postalCodeA = fake.postalcode()

    class Address:
        def __init__(self, unitNum, street):
            self.unitNum = streetNum
            self.street = streetA
    address_list.append(Address(streetNum, streetA))

    '''
    Postal Code
    '''
    class PostalCodes:
        def __init__(self, city, state, postalCode):
            self.city = city
            self.state = state
            self.postalCode = postalCode


    postalCode_list.append(PostalCodes(cityA, stateA, postalCodeA))

    '''
    Guests
    '''
    class Guests:
        def __init__(self, fName, lName, age):
            self.fName = f
            self.lName = l
            self.age = a

    numOfGuestRand = randint(0, 3)
    for i in range(numOfGuestRand):
        name = fake.name()
        tempList = name.split()
        f = tempList[0]
        l = tempList[1]
        a = randint(1, 100)

        guest_list.append(Guests(f, l, a))


# Export to CSV
with open('customer_list.csv', 'w', newline='') as csvfile:
    csv_faker = csv.writer(csvfile)
    for i in customers_list:
        csv_faker.writerow([i.fName, i.lName, i.phoneNum, i.email])

with open('reservation_list.csv', 'w', newline='') as csvfile:
    csv_faker = csv.writer(csvfile)
    for i in reservation_list:
        csv_faker.writerow([i.checkIn, i.checkOut, i.hasPaid, i.specialRequest])

with open('payment_list.csv', 'w', newline='') as csvfile:
    csv_faker = csv.writer(csvfile)
    for i in payment_list:
        csv_faker.writerow([i.amount, i.datePaid])

with open('card_list.csv', 'w', newline='') as csvfile:
    csv_faker = csv.writer(csvfile)
    for i in card_list:
        csv_faker.writerow([i.cardNum, i.CCV, i.holderFName, i.holderLName, i.cardType])

with open('address_list.csv', 'w', newline='') as csvfile:
    csv_faker = csv.writer(csvfile)
    for i in address_list:
        csv_faker.writerow([i.unitNum, i.street])

with open('postalCode_list.csv', 'w', newline='') as csvfile:
    csv_faker = csv.writer(csvfile)
    for i in postalCode_list:
        csv_faker.writerow([i.city, i.state, i.postalCode])

with open('guest_list.csv', 'w', newline='') as csvfile:
    csv_faker = csv.writer(csvfile)
    for i in guest_list:
        csv_faker.writerow([i.fName, i.lName, i.age])







