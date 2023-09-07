# Missing "Authorization" header when redirecting in nginx with aiohttp web client

This is a test environment for diagnosing the above fault as was [raised in the Pythonista server](https://canary.discord.com/channels/490948346773635102/1140594789918715966).

Current [findings] indicate that the "Authorization" header is stripped during a redirect (`return` nginx directive) as a security measure.

[findings]: https://stackoverflow.com/q/72870611
