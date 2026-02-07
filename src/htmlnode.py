class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise Exception(NotImplementedError)
    
    def props_to_html(self):
        if not self.props:
            return ""
        
        html_string = ""

        for key, value in self.props.items():
            html_string += f' {key}="{value}"'

        return html_string
    
    def __repr__(self):
        return f"HTMLNode (tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag=tag, value=value, children = None, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError
        
        if self.tag is None:
            return self.value
        
        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

        else:        
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
    def __repr__(self):
        return f"HTMLNode (tag={self.tag}, value={self.value}, props={self.props})"