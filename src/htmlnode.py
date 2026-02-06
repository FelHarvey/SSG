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
