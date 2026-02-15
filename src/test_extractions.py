import unittest

from extraction import extract_markdown_links, extract_markdown_images


class TestExtraction(unittest.TestCase):
#test images
    def test_extract_markdown_images(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_multi(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![image2](https://image.com)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image2", "https://image.com")], matches)

    def test_extract_markdown_images_plus_links(self):
        matches = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and a link [to boot dev](https://www.boot.dev)")
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_images_empty(self):
        matches = extract_markdown_images(" ")
        self.assertListEqual([], matches)

    def test_extract_markdown_images_punctuated(self):
        matches = extract_markdown_images("![obi wan kenobi](https://i.imgur.com/fJRm4Vk.jpeg)")
        self.assertListEqual([("obi wan kenobi", "https://i.imgur.com/fJRm4Vk.jpeg")], matches)

    #test links
    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_var1(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev")], matches)

    def test_extract_markdown_links_multi(self):
        matches = extract_markdown_links("This is text with a link [to boot dev](https://www.boot.dev) and another [link elsewhere](https://imgur.com)")
        self.assertListEqual([("to boot dev", "https://www.boot.dev"), ("link elsewhere","https://imgur.com")], matches)

    def test_extract_markdown_links_empty(self):
        matches = extract_markdown_links(" ")
        self.assertListEqual([], matches)

    def test_extract_markdown_links_punctuatded(self):
        matches = extract_markdown_links("See [Boot.dev docs!](https://www.boot.dev/docs)")
        self.assertListEqual([("Boot.dev docs!", "https://www.boot.dev/docs")], matches)

if __name__ == "__main__":
    unittest.main()