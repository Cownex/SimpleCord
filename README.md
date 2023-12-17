# SimpleCord
Simple Python library to send and manage Discord-Bot messages without a big Library.

## Examples

* [Send Message](#send-message)
* [Edit Message](#edit-message)
* [Delete Message](#delete-message)
* [Send simple Embed](#send-simple-embed)
* [Add more attributes to embed](#add-more-attributes-to-embed)
* [Add attachments](#add-attachments)



### Send Message
````python
from SimpleCord.client import SimpleCordClient

client = SimpleCordClient("bot-token")

message = client.send_message("channel-id", "message")
````

### Edit Message
Edit a sent message.
````python
from SimpleCord.client import SimpleCordClient

client = SimpleCordClient("bot-token")

message = client.send_message(channel_id="channel-id", content="Hey, tgis is an Example!")

message.edit_message("Hey, this is an Example!")
````

### Delete Message
Deletes a sent message
````python
from SimpleCord.client import SimpleCordClient

client = SimpleCordClient("bot-token")

message = client.send_message(channel_id="channel-id", content="Hey, this is an Example!")

message.delete_message()
````

### Send simple Embed
Send simple Message with an Embed.
````python
from SimpleCord.client import SimpleCordClient, Embed

client = SimpleCordClient("bot-token")

embed = Embed(title="Embed Example", description="Description of the example Embed", color=1752220)

message = client.send_message(channel_id="channel-id", embed=embed)
````

### Add more Attributes to Embed
Add more Attributes to the Embed. All attributes are optional.
````python
from SimpleCord.client import SimpleCordClient, Embed

client = SimpleCordClient("bot-token")

embed = Embed(title="Embed Example", description="Description of the example Embed", color=1752220)

# set the author of the embed
embed.set_author("Cownex", "https://avatars.githubusercontent.com/u/76699137?v=4")

# set a footer for the embed
embed.set_footer("Example Footer", "https://avatars.githubusercontent.com/u/76699137?v=4")

# set timestamp for the footer
embed.set_timestamp("2023-09-07T-16:00+00")

# set a thumbnail 
embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/76699137?v=4", height=300, width=300)

# set image 
embed.set_image(url="https://avatars.githubusercontent.com/u/76699137?v=4", height=100, width=100)


# add some fields
embed.add_field("Example 1", "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut l")
embed.add_field("Example 2", "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut l")
embed.add_field("Example 3", "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut l")

message = client.send_message(channel_id="channel-id", embed=embed)
````

### Add Attachments
**soon**