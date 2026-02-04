from textnode import TextNode, TextType

def main():
    test_a = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    test_b = TextNode("Bold test", TextType.BOLD)
    test_c = TextNode("Codelink", TextType.CODE, "https://www.boot.dev")
    print(test_a, test_b, test_c)
    return

main()