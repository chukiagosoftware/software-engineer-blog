#!/usr/bin/env python3.10

import requests
import json
from markdown.inlinepatterns import InlineProcessor
import xml.etree.ElementTree as etree
from markdown.extensions import Extension


SOURCE = "https://api.github.com/emojis"

# let there be +1
EMOJI_RE = r'(:)((?:[\+\-])?[_0-9a-zA-Z]*?):'


class GheEmoji(Extension):

    def __init__(self, **kwargs):
        self.config = {
            'emoji': [{}, 'Dict emojiname : url ']
        }
        super(GheEmoji, self).__init__(**kwargs)

    def extendMarkdown(self, md):
        pattern = EmojiInlineProcessor(EMOJI_RE, self.getConfig('emoji'))
        # Insert del pattern into markdown parser
        md.inlinePatterns.register(pattern, 'emoji', 100)

    @staticmethod
    def load_from_github():
        try:
            resp = requests.get(SOURCE)
            payload = resp.content
            data = json.loads((payload.decode('utf-8')))
            return GheEmoji(emoji=data)
        except Exception as e:
            print(e)


class EmojiInlineProcessor(InlineProcessor):
    def __init__(self, pattern, emoji):
        super(EmojiInlineProcessor, self).__init__(pattern)
        self.emoji = emoji

    def handleMatch(self, m, data):
        tag = m.group(2)
        url = self.emoji.get(tag, '')
        if not url:
            return None, None, None
        div = etree.Element("div")
        div.attrib["class"] = "ghe_emoji"
        el = etree.SubElement(div, "img")
        el.attrib["class"] = "ghe_emoji"
        el.set("src", url)
        el.set("title", tag)
        el.set("alt", tag)
        return div, m.start(0), m.end(0)


if __name__ == '__main__':
    print("This is an extension to Markdown please import it.")
