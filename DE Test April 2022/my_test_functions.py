from test_1 import INVALID, is_log_line, get_valid_log_level, get_valid_message, get_valid_timestamp, get_dict

def test_find_log_level():
    """ Tests basic log_level functionality """
    assert get_valid_log_level("INFO") != INVALID
    assert get_valid_log_level("---") == INVALID

def test_validate_message():
    """ Tests message is format ': some message ' """
    assert get_valid_message("INFO :", "INFO") == INVALID
    assert get_valid_message("INFO : a message", "INFO") != INVALID

def test_validate_timestamp():
    """ Tests only single normal timestamps allowed """
    assert get_valid_timestamp("03/11/21 08:51:01") == "03/11/21 08:51:01"
    assert get_valid_timestamp("03/11/21 08:51:01 INFO") == "03/11/21 08:51:01"
    assert get_valid_timestamp("03/11/21-08:51:01") == INVALID
    assert get_valid_timestamp("not even close") == INVALID
    assert get_valid_timestamp("03/11/21 08:51:0103/11/21 08:51:01") == INVALID


def test_log_line():
    test_string_true = "03/11/21 08:51:01 INFO    :...locate_configFile: Specified configuration file: /u/user10/rsvpd1.conf"
    test_string_false = "not a line"

    assert is_log_line(test_string_true) == True
    assert is_log_line(test_string_false) == False

