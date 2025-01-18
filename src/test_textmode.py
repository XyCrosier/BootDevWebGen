import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node_urlnonelit = TextNode("This is a text node", TextType.BOLD, None)
        
        self.assertEqual(node, node2)
        self.assertEqual(node, node_urlnonelit)

    def test_eq2(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node_com = TextNode("This is a text node", TextType.BOLD, "www.example.com")
        node_net = TextNode("This is a text node", TextType.BOLD, "www.example.net")
        node_ital = TextNode("This is a text node", TextType.ITALIC)
        node_text = TextNode("This is a DIFFERENT text node", TextType.BOLD)
        node_lowercase = TextNode("this is a text node", TextType.BOLD)
        node_urlnone_lit = TextNode("This is a text node", TextType.BOLD, None)
        node_urlnone_str = TextNode("This is a text node", TextType.BOLD, "None")
        node_textnone_lit = TextNode(None, TextType.BOLD, "None")
        node_textnone_str = TextNode("", TextType.BOLD, "None")
        
        self.assertNotEqual(node, node_com)
        self.assertNotEqual(node_com, node_net)
        self.assertNotEqual(node, node_ital)
        self.assertNotEqual(node, node_text)
        self.assertNotEqual(node, node_lowercase)
        self.assertNotEqual(node_urlnone_lit, node_urlnone_str)
        self.assertNotEqual(node, node_urlnone_str)
        self.assertNotEqual(node_textnone_str, node_textnone_lit)

class TestTextNodeToHTMLNode(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(
            html_node.props,
            {"src": "https://www.boot.dev", "alt": "This is an image"},
        )

    def test_bold(self):
        node = TextNode("This is bold", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is bold")

if __name__ == "__main__":
    unittest.main()