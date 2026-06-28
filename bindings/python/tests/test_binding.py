from unittest import TestCase

import tree_sitter
import tree_sitter_avro_avdl


class TestLanguage(TestCase):
    def test_can_load_grammar(self):
        try:
            tree_sitter.Language(tree_sitter_avro_avdl.language())
        except Exception:
            self.fail("Error loading Avro AVDL grammar")
