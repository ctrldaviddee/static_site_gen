from textnode import TextNode, TextType


class HTMLNode:
    """
        An HTMLNode without a tag will just render as raw text
        An HTMLNode without a value will be assumed to have children
        An HTMLNode without children will be assumed to have a value
        An HTMLNode without props simply won't have any attributes
    """
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = [] if children is None else children
        self.props = {} if props is None else props

    def to_html(self):
        "Child classes will override this method to render themselves as HTML."
        raise NotImplementedError('to_html not impleented')

    def props_to_html(self) -> str:
        """Convert props dictionary to HTML attributes string with leading space."""
        if not self.props:
            return ""
        return " " + " ".join(f'{key}="{value}"' for key, value in self.props.items())
        

    def __repr__(self) -> str:
        """String representation of the HTMLNode for debugging."""
        return (f"HTMLNode(tag={self.tag}, value={self.value}, "
                f"children={self.children}, props={self.props})")


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if not value:
            raise ValueError("All leaf nodes must have a value")
        super().__init__(tag=tag, value=value, props=props)
    
    # def to_html(self):
    #     if self.tag:
    #         return (
    #             f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    #             if self.props
    #             else f"<{self.tag}>{self.value}</{self.tag}>"
    #         )
    #     else:
    #         return self.value
    
    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
        
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)
        
    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid parent node: no tag")
        if self.children is None:
            raise ValueError("Parent node must have children")

        children_html = "".join(child.to_html() for child in self.children)
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"
    
def text_node_to_html_node(text_node:TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text)
        case TextType.NORMAL_TEXT:
            return LeafNode(None, text_node.text)
        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text)
        case TextType.LINKS:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGES:
            return LeafNode(tag="img", value="", props={"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(f"Invalid text_type: {text_node.text_type}")
            
    
    
       
    
        
node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
        ParentNode(
            "a",
            [LeafNode(None, "Google", {"href": "https://www.google.com"})],
        ),
    ],
)


child_node = LeafNode("span", "child")
child2_node = LeafNode("pre", "child2")
parent_node = ParentNode("div", [child_node, child2_node])

print(parent_node.to_html())