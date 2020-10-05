# -*- coding: utf-8 -*-
import os
"""
Sets the repeat rate for differnt tasks - starcraft rapidfire or reasonable for coding
"""

class Py3status:
    def __init__(self):
        self._set_typing_mode()

    def click_info(self):
        template = 'Typing Mode: {label}'
        data = { 'label': self.label }
        return {
            'full_text': self.py3.safe_format(template, data),
            'cached_until': self.py3.CACHE_FOREVER
        }

    def on_click(self, event):
        self._toggle_mode()

    def _toggle_mode(self):
        if self.label == 'Typing':
            self._set_starcraft_mode()
        else:
            self._set_typing_mode()

    def _set_starcraft_mode(self):
        self.label = 'Starcraft'
        self._set_repeat_rate(150, 100)

    def _set_typing_mode(self):
        self.label = 'Typing'
        self._set_repeat_rate(250, 45)

    def _set_repeat_rate(self, delay, rate):
        os.system(f'xset r rate {delay} {rate}')

