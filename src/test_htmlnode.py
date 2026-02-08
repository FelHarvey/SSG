import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode("a", "Link check", None, {"href": "https://www.google.com"})
        result = node.props_to_html()
        self.assertEqual(result, ' href="https://www.google.com"')

    def test_no_props(self):
        node = HTMLNode("p", "Paragraph check", None, {})
        result = node.props_to_html()
        self.assertEqual(result, "")

    def test_multi_props(self):
        node = HTMLNode("a", "Multi Links", "A child", {"Key1": "value1", "browser": "operagx"})
        result = node.props_to_html()
        self.assertEqual(result, ' Key1="value1" browser="operagx"')

# Leaf Node Tests

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_no_value(self):
        node = LeafNode("b", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_no_tag(self):
        node = LeafNode(None, "No tags")
        self.assertEqual(node.to_html(), "No tags")

    def test_with_link(self):
        node = LeafNode("a", "Learn to code!", {"href": "www.boot.dev"})
        self.assertEqual(node.to_html(), '<a href="www.boot.dev">Learn to code!</a>')

    def test_leaf_multiple_props(self):
        node = LeafNode("a", "Link", {"href": "www.boot.dev", "target": "_blank"})
        html = node.to_html()
        self.assertIn('<a ', html)
        self.assertIn('href="www.boot.dev"', html)
        self.assertIn('target="_blank"', html)
        self.assertTrue(html.endswith('>Link</a>'))

    def test_leaf_empty_string_value(self):
        node = LeafNode("p", "")
        self.assertEqual(node.to_html(), "<p></p>")

# Parent Node Tests

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_parent_no_tag(self):
        node = ParentNode(None, ["No tag"])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_no_children(self):
        node = ParentNode("b", None)
        with self.assertRaises(ValueError):
            node.to_html()

    def test_parent_multi_children(self):
        child1 = LeafNode("b", "Bold Text")
        child2 = LeafNode("i", "Italics Text")
        node = ParentNode("a", [child1, child2], {"href":"Font Embellishments"})
        self.assertEqual(node.to_html(), '<a href="Font Embellishments"><b>Bold Text</b><i>Italics Text</i></a>')

    def test_parent_empty_children(self):
        node = ParentNode("div", [])
        self.assertEqual(node.to_html(), "<div></div>")

if __name__ == "__main__":
    unittest.main()