import csv


def main():
    customer_country = open('customer_country.csv', 'w')
    with open('customers.csv', 'rt') as data1:
        data2 = csv.DictReader(data1, delimiter=',', quotechar='"')
        customer_country.write('FirstName,LastName,Country\n')
        for row in data2:
            customer_country.write(
                row['FirstName'] + ',' + row['LastName'] + ',' + row['Country'] + '\n')
    customer_country.close()


main()