from telethon import TelegramClient, events


if __name__ == '__main__':
    client2 = TelegramClient("asdsad", 6284107, "376f444df0fcadd27458653b3f92ed6a")

    print("Start")


    @client2.on(events.NewMessage(1152540314))
    async def my_event_handler(event):
        await client2.forward_messages(1484261573, event.message)
        sender = await event.get_sender()
        print(sender.id)


    client2.start()
    client2.run_until_disconnected()
