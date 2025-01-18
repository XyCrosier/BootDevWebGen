import unittest

from htmlnode import LeafNode, ParentNode

class TestParentNode(unittest.TestCase):

    def test_to_html(self):
        leaf_bare = LeafNode(None, "This is raw text.")
        leaf_bold = LeafNode("b", "This is BOLD text.")
        leaf_ital = LeafNode("i", "This is ital text.")
        leaf_link = LeafNode("a", "This is a link.", {"href": "https://www.example.com"})

        parent_simple = ParentNode("p", [leaf_bare])
        simple_expected = "<p>This is raw text.</p>"
        self.assertEqual(parent_simple.to_html(), simple_expected)

        parent_bold = ParentNode("p", [leaf_bold])
        bold_expected = "<p><b>This is BOLD text.</b></p>"
        self.assertEqual(parent_bold.to_html(), bold_expected)

        parent_ital = ParentNode("p", [leaf_ital])
        ital_expected = "<p><i>This is ital text.</i></p>"
        self.assertEqual(parent_ital.to_html(), ital_expected)

        parent_link = ParentNode("p", [leaf_link])
        link_expected = '<p><a href="https://www.example.com">This is a link.</a></p>'
        self.assertEqual(parent_link.to_html(), link_expected)

        parent_simple_2 = ParentNode("p", [leaf_bare, leaf_bare])
        simple_2_expected = "<p>This is raw text.This is raw text.</p>"
        self.assertEqual(parent_simple_2.to_html(), simple_2_expected)

        parent_composite = ParentNode("p", [leaf_bare, leaf_bold, leaf_ital, leaf_link])
        composite_expected = '<p>This is raw text.<b>This is BOLD text.</b><i>This is ital text.</i><a href="https://www.example.com">This is a link.</a></p>'
        self.assertEqual(parent_composite.to_html(), composite_expected)

        parent_nested = ParentNode("nest", [parent_simple])
        nested_expected = "<nest><p>This is raw text.</p></nest>"
        self.assertEqual(parent_nested.to_html(), nested_expected)

        parent_missing_children = ParentNode("invalid", None)
        with self.assertRaises(ValueError) as cm:
            parent_missing_children.to_html()
            self.assertEqual(str(cm.exception), "Parent nodes must have children.")

        parent_tagless = ParentNode(None, [parent_simple])
        with self.assertRaises(ValueError) as cm:
            parent_tagless.to_html()
            self.assertEqual(str(cm.exception), "Parent nodes must have a tag.")

if __name__ == "__main__":
    unittest.main()