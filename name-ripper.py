import sys


def first_initial(first_letter, last_name):
    results = []

    # First letter lowercase
    results.append(first_letter + last_name.lower())
    results.append(first_letter + last_name.capitalize())
    results.append(first_letter + last_name.upper())

    # First letter uppercase
    results.append(first_letter.upper() + last_name.lower())
    results.append(first_letter.upper() + last_name.capitalize())
    results.append(first_letter.upper() + last_name.upper())

    tmp = []

    for result in results:
        tmp.append(result[0] + '.' + result[1:len(result)])
        tmp.append(result[0] + '-' + result[1:len(result)])
        tmp.append(result[0] + '_' + result[1:len(result)])

    results.extend(tmp)
    return results


def last_initial(first_name, last_letter):
    results = []

    # Last letter lowercase
    results.append(first_name.lower() + last_letter)
    results.append(first_name.capitalize() + last_letter)
    results.append(first_name.upper() + last_letter)

    # Last letter uppercase
    results.append(first_name.lower() + last_letter.upper())
    results.append(first_name.capitalize() + last_letter.upper())
    results.append(first_name.upper() + last_letter.upper())

    tmp = []

    for result in results:
        tmp.append(result[0:-1] + '.' + result[len(result) - 1])
        tmp.append(result[0:-1] + '-' + result[len(result) - 1])
        tmp.append(result[0:-1] + '_' + result[len(result) - 1])

    results.extend(tmp)
    return results


def full_names(first_name, last_name):
    results = []

    results.append(first_name.lower() + last_name.lower())
    results.append(first_name.capitalize() + last_name.capitalize())
    results.append(first_name.upper() + last_name.upper())

    results.append(first_name.lower() + last_name.capitalize())
    results.append(first_name.upper() + last_name.capitalize())

    results.append(first_name.capitalize() + last_name.lower())
    results.append(first_name.capitalize() + last_name.upper())

    tmp = []

    for result in results:
        tmp.append(result[0:len(first_name)] + '.' + result[len(first_name):len(result)])
        tmp.append(result[0:len(first_name)] + '-' + result[len(first_name):len(result)])
        tmp.append(result[0:len(first_name)] + '_' + result[len(first_name):len(result)])

    results.extend(tmp)

    results.append(last_name.lower() + first_name.lower())
    results.append(last_name.capitalize() + first_name.capitalize())
    results.append(last_name.upper() + first_name.upper())

    results.append(last_name.lower() + first_name.capitalize())
    results.append(last_name.upper() + first_name.capitalize())

    results.append(last_name.capitalize() + first_name.lower())
    results.append(last_name.capitalize() + first_name.upper())

    tmp = []

    for result in results:
        if not result.isalpha():
            continue
        tmp.append(result[0:len(last_name)] + '.' + result[len(last_name):len(result)])
        tmp.append(result[0:len(last_name)] + '-' + result[len(last_name):len(result)])
        tmp.append(result[0:len(last_name)] + '_' + result[len(last_name):len(result)])

    results.extend(tmp)

    return results


def main():
    names = [name.strip() for name in sys.argv[1].split(',')]
    variations = []

    for name in names:
        splitname = name.split(' ')
        first_name = splitname[0]
        last_name = splitname[1]

        variations.extend(first_initial(first_name[0].lower(), last_name))
        variations.extend(last_initial(first_name, last_name[0].lower()))
        variations.extend(full_names(first_name, last_name))

    with open('users.txt', 'w') as user_file:
        for variation in variations:
            user_file.write(variation + '\n')
    print("Number of variations: " + str(len(variations)))


if __name__ == '__main__':
    main()
