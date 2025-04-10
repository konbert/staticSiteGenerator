from textnode import TextType, TextNode 

def main():
    node = TextNode("lorem ipsum", TextType.LINK, "https://mainframe.de" )
    print(node)


if __name__ == "__main__":
    main()

