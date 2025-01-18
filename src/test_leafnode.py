import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):

    def test_to_html(self):
        node = LeafNode(None, "This is raw text.")
        self.assertEqual(node.to_html(), "This is raw text.")

    def test_to_html_2(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_to_html_3(self):
        node = LeafNode("a", "This is a link.", {"href": "https://www.example.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.example.com">This is a link.</a>')

    def test_repr(self):
        node = LeafNode("T","This is a Leaf Node", {"href": "https://www.example.com"})
        expected = "HTMLNode(TAG: T, VALUE: This is a Leaf Node, PROPS: {'href': 'https://www.example.com'}, CHILDREN: None)"
        self.assertEqual(str(node), expected)

if __name__ == "__main__":
    unittest.main()