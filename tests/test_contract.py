import copy
import json
from pathlib import Path
import unittest
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]


class EvidenceContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        schema = json.loads((ROOT / 'schemas/public-evidence.schema.json').read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(schema)
        cls.validator = Draft202012Validator(schema, format_checker=FormatChecker())
        cls.example = json.loads((ROOT / 'examples/public-evidence.json').read_text(encoding='utf-8'))

    def test_fictional_example_valid(self):
        self.validator.validate(self.example)

    def test_private_evidence_rejected(self):
        value = copy.deepcopy(self.example)
        value['projects'][0]['evidence'][0]['visibility'] = 'private'
        self.assertFalse(self.validator.is_valid(value))

    def test_unexpected_personal_field_rejected(self):
        value = copy.deepcopy(self.example)
        value['profile']['email'] = 'person@example.com'
        self.assertFalse(self.validator.is_valid(value))

    def test_invalid_source_uri_rejected(self):
        value = copy.deepcopy(self.example)
        value['projects'][0]['evidence'][0]['source_url'] = 'not a URI'
        self.assertFalse(self.validator.is_valid(value))

    def test_missing_project_context_rejected(self):
        value = copy.deepcopy(self.example)
        del value['projects'][0]['summary']
        self.assertFalse(self.validator.is_valid(value))

    def test_duplicate_skills_rejected(self):
        value = copy.deepcopy(self.example)
        value['projects'][0]['evidence'][0]['skills'] = ['Python', 'Python']
        self.assertFalse(self.validator.is_valid(value))


if __name__ == '__main__':
    unittest.main()
