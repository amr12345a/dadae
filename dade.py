from telethon import TelegramClient, events


if __name__ == '__main__':
    client2 = TelegramClient("asdsad", 6284107, "376f444df0fcadd27458653b3f92ed6a")

    print("Start")


    @client2.on(events.NewMessage(-560266164))
    async def my_event_handler(event):
        await client2.forward_messages(-1296890742, event.message)


    client2.start()
    client2.run_until_disconnected()
