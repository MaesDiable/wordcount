import unittest

import app
text_test_case_1 = "tres tristres tigres, tragaban trigo en un trigal, en tres tristes trasto, tragaban trigo tres tristes tigres."
test_result_1 = "tres tristres tigres tragaban trigo en un trigal en tres tristes trasto tragaban trigo tres tristes tigres"

text_test_case_2 = "Tres trIstres tiGres, Tragaban trigo en uN trigal, en tRes tristes TRASTO, tragaban trigo TREs tristes tigres."
test_result_2 = "tres tristres tigres tragaban trigo en un trigal en tres tristes trasto tragaban trigo tres tristes tigres"

text_test_case_3 = "Trés trIstres tiGres, Tragaban trigo en uN trigal, en trés tristes TRÁSTO, tragaban trigo TREs tristes tigres."
test_result_3 = "trés tristres tigres tragaban trigo en un trigal en trés tristes trásto tragaban trigo tres tristes tigres"

text_test_case_4 = "tres tristres    tigres, tragaban  trigo en un trigal, en tres     tristes trasto,   tragaban trigo tres tristes tigres."
test_result_4 = "tres tristres tigres tragaban trigo en un trigal en tres tristes trasto tragaban trigo tres tristes tigres"

text_test_case_5 = "tres tristres   " \
                   " tigres, tragaban  trigo en un trigal, en tres" \
                   "     tristes trasto,   tragaban trigo tres " \
                   "tristes tigres."
test_result_5 = "tres tristres tigres tragaban trigo en un trigal en tres tristes trasto tragaban trigo tres tristes tigres"

test_response = {"Tres": 3, "tristres": 1, "tristes": 2, "tragaban": 2, "trigo": 2, "en": 2, "un": 1, "trigal": 1,
                 "trasto": 1}



class AddTest(unittest.TestCase):
    def normal_text_with_punctuation(self):
        c = app.normalize_text(text_test_case_1)
        self.assertEqual(test_result_1, c)

    def text_lowercase_uppercase_mix(self):
        c = app.normalize_text(text_test_case_2)
        self.assertEqual(test_result_2, c)

    def text_lowercase_uppercase_and_accents(self):
        c = app.normalize_text(text_test_case_3)
        self.assertEqual(test_result_3, c)

    def text_with_multiple_spaces(self):
        c = app.normalize_text(text_test_case_4)
        self.assertEqual(test_result_4, c)

    def text_with_multiple_lines(self):
        c = app.normalize_text(text_test_case_5)
        self.assertEqual(test_result_5, c)

if __name__ == '__main__':
    AddTest.main()
