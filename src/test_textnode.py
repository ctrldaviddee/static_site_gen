import unittest

from textnode import (TextNode, TextType)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)

        self.assertEqual(node, node2)


    def test_different_text(self):
        node = TextNode("This is a text node", TextType.NORMAL_TEXT)
        node2 = TextNode("This is a different node", TextType.NORMAL_TEXT)

        self.assertNotEqual(node, node2)


    def test_different_text_types(self):
        node = TextNode("This is a text node", TextType.ITALIC_TEXT)
        node2 = TextNode("This is a different node", TextType.NORMAL_TEXT)

        self.assertNotEqual(node, node2)


    def test_nodes_with_different_url(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT, "http://0.0.0.0:8888/")

        self.assertNotEqual(node, node2)


    def test_url_provided(self):
        url = "http://0.0.0.0:8888/"
        node = TextNode("This is a url text", TextType.LINKS, url)
        self.assertIsNotNone(node.url)
        self.assertEqual(node.url, url)


    def test_repr(self):
            node = TextNode("This is a text node", TextType.NORMAL_TEXT, "https://www.boot.dev")
            self.assertEqual(
                "TextNode(This is a text node, n_text, https://www.boot.dev)", repr(node)
            )


if __name__=="__main__":
    unittest.main()
