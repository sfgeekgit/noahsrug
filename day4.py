import csv
#import itertools

cust_filepath = './5784-speedrun/noahs-customers.csv'

# need to find a libra born in the year of the goat
# so, I need to find a customer with a birthday in 1979 or 1991 or 2003 or 2015 or earlier in 67 55 43
# Unless Libra is like Jan or somehow close to the chinese new year
#   Libra dates are September 23 to October 22,  whew.


def main():
    c_uids = {}
    
    goat_years = ['1967', '1955', '1943', '1931', '1919', '1907', '1979', '1991', '2003', '2015']
    # read customers csv file line by line 
    with open(cust_filepath, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header line
        for cust_row in reader:
            birthdate = cust_row[4]
            b_year, b_month, b_day = birthdate.split('-')
            if b_year in goat_years:
                if (int(b_month) == 9 and int(b_day) >= 23) or (
                    int(b_month) == 10 and int(b_day) <= 22):

                    #print(f"{cust_row=}")
                    # print(f"{birthdate=}  {b_year=} {b_month=} {b_day=}")
                    # UM. OK, these are all libras born in the year of the goat.
                    # 64 of them. There must be another clue.

                    # OK, looking for :
                    # guy who lived in my neighborhood
                    # this guy's neighbor:
                    # 5745,"David Swanson Jr.","86-84 214th St","Queens Village, NY 11427","1958-10-29","838-351-0370","America/New_York",40.73007,-73.74856
                    # so look for "Queens Village, NY" I guess...
                    cust_neighborhood = cust_row[3]
 
                    # if cust_neighborhood contains "Queens"
                    if "Queens Village" in cust_neighborhood:
                        print(f"!!! \n\n {cust_neighborhood=}")
                        print(f"{cust_row=} \n\n")

                    # two rows match, one matchs the exact zip code, I'll try that...





if __name__ == "__main__":
    main()
