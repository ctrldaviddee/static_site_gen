from enum import Enum

class TextType(Enum):
    NORMAL_TEXT="n_text"
    BOLD_TEXT="b_text"
    ITALIC_TEXT="i_text"
    CODE_TEXT="c_text"
    LINKS="link"
    IMAGES="image"

class TextNode():
    def __init__(self, text, text_type:TextType,  url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text
                and self.text_type == other.text_type
                and self.url == other.url
                )


    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
