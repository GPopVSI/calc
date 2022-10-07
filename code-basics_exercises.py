# Ex 43
text = 'Never forget what you are, for surely the world will not'
# BEGIN (write your solution here)
print(f'Index Of N: {text.find("N")}\nIndex Of ,: {text.find(",")}')

# Ex 44
print(len(text[5:15].strip()))


# Ex 45
def print_motto():
    n = 'Winter is coming'
    print(n)


# Ex 46
def say_hurray_three_times():
    return 'hurray! hurray! hurray!'


# Ex 47
def truncate(text, length):
    return f'{text[0:length]}...'


# Ex 48
def get_hidden_card(credit_number, length=4):
    visible_line = credit_number[-4:]
    return f"{'*' * length}{visible_line}"


# Ex 49
def trim_and_repeat(string, offset=0, repetitions=1):
    result = string[offset:] * repetitions
    return result


# Ex 50
def is_pensioner(age):
    return age >= 60


# Ex 51
def is_mister(sex):
    return sex == 'Mister'


# Ex 52
def is_international_phone(phone_number):
    return phone_number[0] == '+'


# Ex 53
def is_leap_year(year_type):
    return year_type % 400 == 0 or (year_type % 4 == 0 and year_type % 100 != 0)


# Ex 54
def is_palindrome(word):
    lower_word = word.lower()
    return lower_word == lower_word[::-1]


def is_not_palindrome(word):
    return not is_palindrome(word)


# Ex 55
def string_or_not(parametr):
    return isinstance(parametr, str) and 'yes' or 'no'


# Ex 56
def guess_number(number):
    if number == 42:
        return 'You win!'
    return 'Try again!'


# Ex 57
def normalize_url(url):
    prefix = 'https://'
    if url[:8] == prefix:
        return url
    else:
        if url[:7] == 'http://':
            return prefix + url[7:]
        else:
            return prefix + url


# Ex 58
def who_is_this_house_to_starks(second_name):
    if second_name == 'Karstark' or second_name == 'Tully':
        return 'friend'
    elif second_name == 'Lannister' or second_name == 'Frey':
        return 'enemy'
    return 'neutral'


# Ex 59
def flip_flop(string):
    return 'flop' if string == 'flip' else 'flip'


# Ex 60
def print_numbers(last_number):
    i = last_number
    while i > 0:
        print(i)
        i = i - 1
    print('finished!')


# Ex 61
def multiply_numbers_from_range(start, finish):
    i = start
    multyply = 1
    while i <= finish:
        multyply = multyply * i
        i = i + 1
    return multyply


# Ex 62
def join_numbers_from_range(start, finish):
    i = start
    concatination = ''
    while i <= finish:
        concatination = concatination + str(i)
        i = i + 1
    return concatination


# Ex 63
def print_reversed_word_by_symbol(word):
    i = len(word) - 1
    while i >= 0:
        print(word[i])
        i -= 1


# Ex 64
def count_chars(string, char):
    index = 0
    count = 0
    while index < len(string):
        if string.lower()[index] == char.lower():
            count += 1
        index += 1
    return count


# Ex 65
def my_substr(string, length):
    i = 0
    new_string = ''
    while i < length:
        new_string = new_string + string[i]
        i = i + 1
    return new_string


# Ex 66
def is_arguments_for_substr_correct(string, i, length_string):
    if i < 0:
        return False
    elif length_string < 0:
        return False
    elif i > len(string) - 1:
        return False
    elif i + length_string > len(string):
        return False
    return True
