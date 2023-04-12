from test_1 import is_log_line


def test_log_line():
    test_string_true = "03/11/21 08:51:01 INFO    :...locate_configFile: Specified configuration file: /u/user10/rsvpd1.conf"
    test_string_false = "not a line"

    assert is_log_line(test_string_true) == True
    assert is_log_line(test_string_false) == False

