import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, TextNode, TextType, text_node_to_html_node

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        schema = {
            "href": "https://www.google.com",
            "target": "_blank",
        }

        expected = ' href="https://www.google.com" target="_blank"'

        node = HTMLNode(tag="a", value="Click me", children=None, props={"href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(type(node.props), type(schema))

        self.assertEqual(node.props_to_html(), expected)

    def test_data_member_optional_feature(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})


    def test_default_empty_collections(self):
        node = HTMLNode(tag="div", value="content")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {})


    def test_to_html_raises_error(self):
        node = HTMLNode()
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_repr_method(self):
        node = HTMLNode(tag="p", value="paragraph")
        # Call repr() on the node, which internally calls node.__repr__()
        repr_str = repr(node)
        self.assertIn("tag=p", repr_str)
        self.assertIn("value=paragraph", repr_str)
        

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")
        
    def test_value_required(self):
        with self.assertRaises(ValueError):
            LeafNode(tag="p", value="")
            
    def test_render_raw_text(self):
        node = LeafNode(tag=None, value="This is a leaf node")
        self.assertEqual(node.to_html(), "This is a leaf node")
        
    def test_render_with_props(self):
        node = LeafNode(tag="a", value="Click me", props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com" target="_blank">Click me</a>')
        
        
class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
        
class TestTextNodeToHtmlNode(unittest.TestCase):
    def test_text(self):
            node = TextNode("This is a text node", TextType.NORMAL_TEXT)
            html_node = text_node_to_html_node(node)
            self.assertEqual(html_node.tag, None)
            self.assertEqual(html_node.value, "This is a text node")
        
        

if __name__ == '__main__':
    unittest.main()
