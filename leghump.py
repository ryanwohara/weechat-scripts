# -*- coding: utf-8 -*-
#
# Leghump, for #leghump on SwiftIRC
# Latest development version: https://github.com/ryanwohara/weechat_scripts
#
#   A leg humping script that will hump a leg when someone joins #leghump.
#
#
#  Copyright (c) 2018 Ryan W. "Dragon" O'Hara
#   https://github.com/ryanwohara
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
SCRIPT_NAME     = "leghump"
SCRIPT_AUTHOR   = "Ryan W. 'Dragon' O'Hara"
SCRIPT_VERSION  = "0.1"
SCRIPT_LICENSE  = "MIT"
SCRIPT_DESC     = "A script that will automatically hump any legs that join into #leghump."
SCRIPT_CLOSE_CB = "leghump_close"

import_ok = True

try:
  import weechat
except ImportError:
  print("This script must be run under WeeChat.")
  import_ok = False

import re
import random

def on_join_hump(data, signal, signal_data):
  network = signal.split(',')[0]
  msg = weechat.info_get_hashtable("irc_message_parse", {"message": signal_data})

  joined_nick = msg['nick']
  chan_name = msg['channel']

  chan_buffer = weechat.info_get("irc_buffer", "%s,%s" % (network, chan_name))

  if chan_name.lower() == '#leghump':
    for a in range(0, 2):
      output = re.sub('!nick!', joined_nick, random.choice(list(open('leghump.dat'))))
      weechat.command(chan_buffer, "/me %s" % output)

  return weechat.WEECHAT_RC_OK


def leghump_close(*kwargs):
  weechat.unhook_all()

  return weechat.WEECHAT_RC_OK



if __name__ == "__main__" and import_ok:
  if weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION,
                      SCRIPT_LICENSE, SCRIPT_DESC, SCRIPT_CLOSE_CB, ""):

    cs_buffer = weechat.buffer_search("python", "clone_scanner")
    weechat.hook_signal("*,irc_in2_join", "on_join_hump", "")


