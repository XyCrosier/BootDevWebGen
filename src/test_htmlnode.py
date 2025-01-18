import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_0(self):
        node_empty = HTMLNode()
        self.assertEqual(node_empty.props_to_html(), "")

    def test_props_to_html_1(self):
        prop_1 = {"href": "https://www.example.com"}
        prop_1H = ' href="https://www.example.com"'
        node_one_prop = HTMLNode(None, None, None, prop_1)
        self.assertEqual(node_one_prop.props_to_html(), prop_1H)

    def test_props_to_html_2(self):
        prop_2 = {"href": "https://www.example.com",
                       "target": "_blank"}
        prop_2H = ' href="https://www.example.com" target="_blank"'
        node_two_prop = HTMLNode(None, None, None, prop_2)
        self.assertEqual(node_two_prop.props_to_html(), prop_2H)

    def test_repr(self):
        node = HTMLNode("T","This is an HTML Node", None, {"href": "https://www.example.com"})
        expected = "HTMLNode(TAG: T, VALUE: This is an HTML Node, PROPS: {'href': 'https://www.example.com'}, CHILDREN: None)"
        self.assertEqual(str(node), expected)

if __name__ == "__main__":
    unittest.main()