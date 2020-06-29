def my_func():
    return 10

def test_mything(snapshot):

    return_value = my_func()

    snapshot.assert_match(return_value, 'gpg_response')
