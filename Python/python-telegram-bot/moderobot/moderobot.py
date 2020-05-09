#!/usr/bin/env python

from moderobot.messages.eng import BOT_MESSAGES

class ModeroBot:
    def __init__(self, logger, bot):
        """Initialize instance."""
        self._logger = logger  # bot is injected
        self._bot = bot  # bot is injected


    def greet_new_members(self, message):
        self._logger.debug('on_user_joins')
        new_chat_members = message.new_chat_members

        for new_member in new_chat_members:
            name = new_member.first_name
            if hasattr(new_member, 'last_name') and new_member.last_name is not None:
                name += u" {}".format(new_member.last_name)

            if hasattr(new_member, 'username') and new_member.username is not None:
                name += u" (@{})".format(new_member.username)

            self._bot.reply_to(message, BOT_MESSAGES['welcome'].format(name=name))