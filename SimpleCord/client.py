import requests


class SimpleCordClient(object):
    """SimpleCord Client to send, edit and delete messages."""

    def __init__(self, bot_token):
        self.bot_token = bot_token
        self.base_url = 'https://discord.com/api/v10'

    def send_message(self, channel_id, content=None, embed=None):
        endpoint = f'/channels/{channel_id}/messages'
        url = self.base_url + endpoint
        headers = {
            'Authorization': f'Bot {self.bot_token}',
            'Content-Type': 'application/json'
        }
        if not content and not embed:
            raise Exception("Request dont has any Message or embed!")
        data = {}
        if content:
            data['content'] = content
        if embed:
            data['embeds'] = [embed.json]
        response = requests.post(url, headers=headers, json=data)
        print(response.json())
        response.raise_for_status()
        return Message(self.bot_token, response.json()['id'], channel_id)


class Embed(object):
    """Embed object"""

    def __init__(self, title, description, color, url=None):
        self.timestamp = None
        self.thumbnail_url = None
        self.thumbnail_height = None
        self.thumbnail_width = None
        self.image_url = None
        self.image_height = None
        self.image_width = None
        self.author_name = None
        self.author_url = None
        self.author_icon_url = None
        self.footer_text = None
        self.footer_icon_url = None
        self.fields = []
        self.title = title
        self.description = description
        self.url = url
        self.color = color

    @property
    def json(self):
        r = {
            "title": self.title,
            "description": self.description,
            "url": self.url
        }
        if self.timestamp:
            r['timestamp'] = self.timestamp
        if self.thumbnail_url:
            r['thumbnail'] = {
                "url": self.thumbnail_url,
                "width": self.thumbnail_width,
                "height": self.thumbnail_height
            }
        if self.image_url:
            r['image'] = {
                "url": self.image_url,
                "width": self.image_width,
                "height": self.image_height
            }
        if self.author_name:
            r['author'] = {
                "name": self.author_name,
                "url": self.author_url,
                "icon_url": self.author_icon_url
            }
        if self.footer_text:
            r['footer'] = {
                "text": self.footer_text,
                "icon_url": self.footer_icon_url
            }
        if self.fields:
            r['fields'] = self.fields
        return {key: value for key, value in r.items() if value is not None}

    def set_timestamp(self, timestamp):
        """
        add a timestamp to embed
        :param timestamp: ISO8601 timestamp
        """
        self.timestamp = timestamp

    def set_thumbnail(self, url: str, height: int, width: int):
        """
        set embed thumbnail
        :param url: source url of thumbnail (only supports http(s) and attachments)
        :param height: height of thumbnail
        :param width: width of thumbnail
        """
        self.thumbnail_url = url
        self.thumbnail_width = width,
        self.thumbnail_height = height

    def set_image(self, url: str, height: int, width: int):
        """
        set embed author
        :param url: source url of image (only supports http(s) and attachments)
        :param height: height of image
        :param width: width of image
        """
        self.image_url = url
        self.image_width = width,
        self.image_height = height

    def set_author(self, name: str, url: str, icon_url: str):
        """
        set embed author
        :param name: name of author
        :param url: url of author (only supports http(s))
        :param icon_url: url of author icon (only supports http(s) and attachments)
        """
        self.author_url = url
        self.author_name = name
        self.author_icon_url = icon_url

    def set_footer(self, text: str, icon_url: str):
        """
        set embed footer
        :param text: footer text
        :param icon_url: url of footer icon (only supports http(s) and attachments)
        """
        self.footer_text = text
        self.footer_icon_url = icon_url

    def add_field(self, name: str, value: str, inline: bool = False):
        """
        add field to embed
        :param name: name of the field
        :param value: value of the field
        :param inline: whether or not this field should display inline
        :return:
        """
        self.fields.append({"name": name, "value": value, "inline": inline})


class Message(object):
    """Message object"""
    def __init__(self, bot_token, message_id, channel_id):
        self.channel_id = channel_id
        self.message_id = message_id
        self.bot_token = bot_token
        self.base_url = 'https://discord.com/api/v10'


    def edit_message(self, new_content, embed=None):
        """
        edits the message
        :param new_content: Edited Message
        :param embed: Edited Embed
        """
        endpoint = f'/channels/{self.channel_id}/messages/{self.message_id}'
        url = self.base_url + endpoint
        headers = {
            'Authorization': f'Bot {self.bot_token}',
            'Content-Type': 'application/json'
        }
        data = {
            'content': new_content
        }
        if embed:
            data['embeds'] = [embed.json()]
        response = requests.patch(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()

    def delete_message(self):
        """Deletes the Message"""
        endpoint = f'/channels/{self.channel_id}/messages/{self.message_id}'
        url = self.base_url + endpoint
        headers = {
            'Authorization': f'Bot {self.bot_token}'
        }
        response = requests.delete(url, headers=headers)
        response.raise_for_status()
        del self

