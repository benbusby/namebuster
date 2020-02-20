import itertools
import sys

def name_with_symbol(name_list):
    results = []

    for name in name_list:
        results.append(name + '.')
        results.append(name + '_')
        results.append(name + '-')
        results.append(name + '+')

    return results


def combine(left, right):
    left.extend(name_with_symbol(left))
    return map(''.join, itertools.product(left, right))


def main():
    names = [name.strip() for name in sys.argv[1].split(',')]
    variations = []

    for name in names:
        split_name = name.split(' ')
        if len(split_name) != 2:
            print('Invalid name provided, must match "FirstName LastName" format')
            continue

        first_name = split_name[0]
        last_name = split_name[1]

        first_name_vars = [first_name.lower(), first_name.capitalize(), first_name.upper()]
        last_name_vars = [last_name.lower(), last_name.capitalize(), last_name.upper()]

        variations.extend(combine(first_name_vars[:] + [first_name[0].lower(), first_name[0].upper()], last_name_vars[:]))
        variations.extend(combine(last_name_vars[:] + [last_name[0].lower(), last_name[0].upper()], first_name_vars[:]))
        variations.extend(combine(first_name_vars[:], [last_name[0].lower(), last_name[0].upper()]))
        variations.extend(combine(last_name_vars[:], [first_name[0].lower(), first_name[0].upper()]))

        variations.extend(first_name_vars)
        variations.extend(last_name_vars)

    with open('users.txt', 'w') as user_file:
        for variation in variations:
            user_file.write(variation + '\n')

    print(str(len(names)) + ' user(s), ' + str(len(variations)) + ' variations')


if __name__ == '__main__':
    main()
