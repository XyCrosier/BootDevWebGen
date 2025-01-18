
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html = ""
        if self.props:
            for prop, value in self.props.items():
                html += f' {prop}="{value}"'
        return html
    
    def __repr__(self):
        return(f"HTMLNode(TAG: {self.tag}, VALUE: {self.value}, PROPS: {self.props}, CHILDREN: {self.children})")
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Value cannot be None -- Leaf nodes must have content.")
        if self.tag:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return self.value
        
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent nodes must have a tag.")
        if self.children == None:
            raise ValueError("Parent nodes must have children.")
        children = "".join([child.to_html() for child in self.children])
        return f"<{self.tag}{self.props_to_html()}>{children}</{self.tag}>"