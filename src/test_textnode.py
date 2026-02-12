import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from split_nodes_delimiter import split_nodes_delimiter


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("Let's try a link", TextType.LINK, "https://www.boot.dev")
        node2 = TextNode("Let's try a link", TextType.LINK, "https://www.boot.dev")
        self.assertEqual(node, node2)

    def test_none_link(self):
        node = TextNode("Setting link to None", TextType.LINK, None)
        node2 = TextNode("Setting link to None", TextType.LINK)
        self.assertEqual(node, node2)

    def test_is_unequal(self):
        node = TextNode("Not equal", TextType.ITALIC)
        node2 = TextNode("Or is it", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_no_match(self):
        node = TextNode("Nothing matches", TextType.BOLD, "https://www.boot.dev")
        node2 = TextNode("Nothing ever will", TextType.CODE, "https://www.google.com")
        self.assertNotEqual(node, node2)

    # Test text to node

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_link(self):
        node = TextNode("Boots Rocks", TextType.LINK, "www.boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "Boots Rocks")
        self.assertEqual(html_node.props, {"href":"www.boot.dev"})

    def test_image(self):
        node = TextNode("Wizard Bear", TextType.IMAGE, "https://www.boot.dev/_nuxt/new_boots_profile.DriFHGho.webp")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src":"https://www.boot.dev/_nuxt/new_boots_profile.DriFHGho.webp","alt":"Wizard Bear" })

    def test_raise_error(self):
        node = TextNode("next", "wrong")
        with self.assertRaises(ValueError):
            html_node = text_node_to_html_node(node)


    # Test Split Nodes function
    def test_split_simple(self):
        assert split_nodes_delimiter([TextNode("This is `code`", TextType.TEXT)], "`", TextType.CODE) == [
    TextNode("This is ", TextType.TEXT),
    TextNode("code", TextType.CODE),
]
    def test_split_simple2(self):
        assert split_nodes_delimiter([TextNode("This is **BOLD** text", TextType.TEXT)], "**", TextType.BOLD) == [
    TextNode("This is ", TextType.TEXT),
    TextNode("BOLD", TextType.BOLD),
    TextNode(" text", TextType.TEXT),
]
        
    def test_split_simple3(self):
        assert split_nodes_delimiter([TextNode("This is _italic_ text _twice_", TextType.TEXT)], "_", TextType.ITALIC) == [
    TextNode("This is ", TextType.TEXT),
    TextNode("italic", TextType.ITALIC),
    TextNode(" text ", TextType.TEXT),
    TextNode("twice", TextType.ITALIC),
]
        
    def test_split_diff_nodes(self):
        assert split_nodes_delimiter([TextNode("Text to **BOLD**", TextType.TEXT), TextNode("**BOLD TEST**", TextType.BOLD)], "**", TextType.BOLD) == [
    TextNode("Text to ", TextType.TEXT),
    TextNode("BOLD", TextType.BOLD),
    TextNode("**BOLD TEST**", TextType.BOLD),
]
    
    def test_split_error(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter([TextNode("This should `error", TextType.TEXT)], "`", TextType.CODE)

    def test_split_error2(self):
        with self.assertRaises(Exception):
            split_nodes_delimiter([TextNode("This should **** error too", TextType.TEXT)], "**", TextType.BOLD)
                                    
if __name__ == "__main__":
    unittest.main()