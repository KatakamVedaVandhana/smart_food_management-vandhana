def add_two_numbers(first, second):

    return first + second


def test_add_two_numbers_with_integer_values_as_input(snapshot):

    #Arrange
    first = 1
    second = 2

    #Act
    return_value = add_two_numbers(first, second)

    #Assert
    snapshot.assert_match(return_value, 'sum_of_two_integers')

def test_add_two_numbers_with_float_values_as_input(snapshot):

    #Arrange
    first = 1.2
    second = 3.5

    #Act
    return_value = add_two_numbers(first, second)

    #Assert
    snapshot.assert_match(return_value, 'sum_of_two_float_numbers')

def test_add_two_numbers_with_negative_values_as_input(snapshot):

    #Arrange
    first = -1
    second = -3

    #Act
    return_value = add_two_numbers(first, second)

    #Assert
    snapshot.assert_match(return_value, 'sum_of_two_negative_numbers')
