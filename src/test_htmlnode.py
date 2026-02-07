import unittest

from htmlnode import HTMLNode, LeafNode


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

if __name__ == "__main__":
    unittest.main()