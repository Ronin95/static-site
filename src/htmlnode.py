class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        """
        Initializes an HTMLNode.
        
        Args:
            tag (str, optional): The HTML tag (e.g., 'p', 'a').
            value (str, optional): The text content of the node.
            children (list, optional): A list of child HTMLNode objects.
            props (dict, optional): HTML attributes (e.g., {'href': '...'})
        """
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        """
        Converts the node to an HTML string.
        This base method is not implemented.
        """
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        """
        Formats the node's properties (attributes) into an HTML string.
        
        Returns:
            str: A string like ' href="url" target="_blank"'
        """
        if self.props is None or not self.props:
            return ""
        
        # Build a list of ' key="value"' strings
        attr_strings = []
        for key, value in self.props.items():
            attr_strings.append(f' {key}="{value}"')
        
        # Join them all together
        return "".join(attr_strings)

    def __repr__(self):
        """
        Provides a developer-friendly string representation of the node.
        """
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        """
        Initializes a LeafNode.
        A LeafNode cannot have children.
        
        Args:
            tag (str): The HTML tag (e.g., 'p', 'a'). Can be None for raw text.
            value (str): The text content of the node. Required.
            props (dict, optional): HTML attributes.
        """
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        """
        Renders the LeafNode as an HTML string.
        """
        if self.value is None:
            raise ValueError("Invalid HTML: LeafNode requires a value")
        
        if self.tag is None:
            return self.value
        
        attributes = self.props_to_html()
        return f"<{self.tag}{attributes}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        """
        Provides a developer-friendly string representation of the LeafNode.
        """
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


# --- New ParentNode Class ---
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        """
        Initializes a ParentNode.
        A ParentNode must have a tag and children.
        
        Args:
            tag (str): The HTML tag (e.g., 'p', 'a').
            children (list): A list of child HTMLNode objects.
            props (dict, optional): HTML attributes.
        """
        # Call the parent constructor.
        # value is always None for a ParentNode.
        super().__init__(tag, None, children, props)

    def to_html(self):
        """
        Renders the ParentNode and its children as an HTML string.
        This method is recursive.
        """
        # 1. Check for a tag
        if self.tag is None:
            raise ValueError("Invalid HTML: ParentNode requires a tag")
        
        # 2. Check for children
        if self.children is None or not self.children:
            raise ValueError("Invalid HTML: ParentNode requires children")
        
        # 3. Build the inner HTML by calling to_html() on each child
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
            
        # 4. Get attributes from the inherited props_to_html()
        attributes = self.props_to_html()
        
        # 5. Return the full tag with children inside
        return f"<{self.tag}{attributes}>{children_html}</{self.tag}>"

    def __repr__(self):
        """
        Provides a developer-friendly string representation of the ParentNode.
        """
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

