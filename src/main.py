from textnode import TextNode, TextType
from htmlnode import HTMLNode

text_node = TextNode("This is some anchor text", TextType.LINKS, "https://www.boot.dev")
html_node = HTMLNode(tag="a", value="Click me", children=None, props={"href": "https://www.google.com", "target": "_blank"})


print(text_node)
print(html_node)
print(html_node.props_to_html())
