from markdownify import markdownify
import re

class Markdown:
    """
    A class to convert HTML text to Markdown and clean the resulting text.
    """

    def __init__(self, title, url, text):
        """
        Initialize the Markdown object with the HTML text to be converted.

        Args:
            text (str): The HTML text to be converted to Markdown.
        """
        self.title = title
        self.url = url
        # Convert HTML to Markdown
        self.text = markdownify(str(text))

    def clean(self):
        """
        Convert the HTML text to Markdown and clean the resulting text.

        Returns:
            str: The cleaned Markdown text.
        """
        if self.text:
            # Return the cleaned Markdown text with a title
            return f"--------\nTitle: {self.title}  [Reference: \"{self.url}\"] \n\nContent: {self.clean_markdown(self.text)}\n\n"
        else:
            # Return a message if no text is found
            return f"No body found"

    @staticmethod
    def clean_markdown(text):
        """
        Clean the Markdown text by removing unwanted characters and formatting.

        Args:
            text (str): The Markdown text to be cleaned.

        Returns:
            str: The cleaned Markdown text.
        """
        # # Remove newlines and convert to single spaces
        # text = re.sub(r'\n', ' ', text)
        # # Remove multiple whitespaces
        # text = re.sub(r'\s+', ' ', text)
        # # Remove hyperlinks
        # text = re.sub(r'http\S+', '', text)
        # # Remove escaping characters
        # text = re.sub(r'\\', '', text)
        # # Remove leading and trailing spaces
        # text = text.strip()
        # # Remove empty lines
        # text = re.sub(r'^\s*$', '', text, flags=re.MULTILINE)
        # # Remove special characters like "Â\xa0"
        # text = re.sub(r'[+\*\=]', '', text)
        # text = re.sub(r'[^\x00-\x7F]+', '', text)  # Remove non-ASCII characters

        # text = re.sub(r'\s+', ' ', text)  # Remove multiple whitespace characters
        text = re.sub(r'[\n\\]|http\S+|[+\*\=]|[^\x00-\x7F]+', '', text)  # Remove newlines, escaping characters, hyperlinks, special characters, and non-ASCII characters
        text = re.sub(r'\s+', ' ', text)  # Remove multiple whitespace characters
        text = text.strip()  # Remove leading and trailing whitespace characters
        text = re.sub(r'^\s*$', '', text, flags=re.MULTILINE)  # Remove empty lines

        text = text.strip()  # Remove leading and trailing whitespace characters
    
        return text