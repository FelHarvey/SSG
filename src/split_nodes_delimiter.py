from htmlnode import HTMLNode
from textnode import text_node_to_html_node, TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)

        else:
            splitted_list = node.text.split(delimiter)
            if len(splitted_list) % 2 == 0:
                raise Exception("Invalid markdown syntax: Missing second delimiter")
            rejoined = []
            for i, s in enumerate(splitted_list):
                
                if i % 2 == 0:
                    if s == "":
                        continue
                    else:
                        new = TextNode(f"{s}", TextType.TEXT)
                else:
                    if s == "":
                        raise Exception("Invalid syntax: Empty formatted section")
                    else:
                        new = TextNode(f"{s}", text_type)
                rejoined.append(new)

            new_nodes.extend(rejoined)

    return new_nodes