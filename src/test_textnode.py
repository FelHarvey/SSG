import unittest

from textnode import TextNode, TextType


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



if __name__ == "__main__":
    unittest.main()