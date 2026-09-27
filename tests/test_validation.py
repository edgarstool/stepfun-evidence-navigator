import unittest
from server import parse_model_output

VALID = '{"summary":"ok","facts":["a"],"unknowns":["b"],"next_action":"c","verification":"d"}'

class ValidationTests(unittest.TestCase):
    def test_valid_output(self):
        self.assertEqual(parse_model_output(VALID)["summary"], "ok")

    def test_rejects_wrong_array_item_type(self):
        with self.assertRaises(ValueError):
            parse_model_output('{"summary":"ok","facts":[1],"unknowns":[],"next_action":"c","verification":"d"}')

    def test_rejects_missing_field(self):
        with self.assertRaises(ValueError):
            parse_model_output('{"summary":"ok","facts":[],"unknowns":[],"next_action":"c"}')

    def test_accepts_fenced_json(self):
        fenced = "```json\n" + VALID + "\n```"
        self.assertEqual(parse_model_output(fenced)["verification"], "d")

if __name__ == "__main__":
    unittest.main()
