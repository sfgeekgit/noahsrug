import csv
#import itertools

filepath = '/Users/nick/py/noahs/5784-speedrun/noahs-customers.csv'


def letters_to_phone_number(letters):
    letter_to_phone_map = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }
    return ''.join(letter_to_phone_map[letter] for letter in letters.upper() if letter in letter_to_phone_map)


def main():
    i=0
    # read csv file line by line and process phone numbers
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header line
        for row in reader:
            phone_number = row[5]  # Assuming phone number is in the 6th column
            # strip phone_number to only numbers
            phone_number = ''.join(filter(str.isdigit, phone_number))

            full_name = row[1]

            name_suffixes = ['Jr.', 'Sr.', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'Jr', 'Sr', '2nd']
                
            last_name = full_name.split()[-1]
            if last_name in name_suffixes:
                last_name = full_name.split()[-2]
            len_name = len(last_name)
            #if len_name < 4:
            #    print(f'{last_name} is too short {full_name}')
            #    #quit()  

            # get last 7 digits of phone number
            #phone_number = phone_number[-7:]
            # Nope! use full 10 digits

            if len_name == 10:            
                last_name_to_phone = letters_to_phone_number(last_name)
                if last_name_to_phone == phone_number:
                    print(f'{last_name} matches phone number! {phone_number}')
                else:
                    pass
                    #print(f'{last_name} does not match phone number {last_name_to_phone} {phone_number}')


            i += 1
            #if i >= 3:
            #    break

if __name__ == "__main__":
    main()

