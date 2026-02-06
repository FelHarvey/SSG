import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()