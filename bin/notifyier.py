#!/usr/bin/python3

from requests import get
import config


def request(method_name, params={}):
  get(f'https://api.telegram.org/bot{config.BOT_TOKEN}/{method_name}', params)


def send_message(message):
  message_params = {
      'chat_id': config.CHAT_ID,
      'text': message,
      'parse_mode': 'MARKDOWN'
  }
  request('sendMessage', message_params)
