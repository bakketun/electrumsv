# ElectrumSV - lightweight Bitcoin SV client
# Copyright (C) 2011 thomasv@gitorious
# Copyright (C) 2017 Neil Booth
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import json
import os

def read_json_dict(filename):
    path = os.path.join(os.path.dirname(__file__), filename)
    with open(path, 'r') as f:
        return json.loads(f.read())

class NetworkConstants:

    # Version numbers for BIP32 extended keys
    # standard: xprv, xpub
    XPRV_HEADERS = {
        'standard': 0x0488ade4,
    }

    XPUB_HEADERS = {
        'standard': 0x0488b21e,
    }

    @classmethod
    def set_mainnet(cls):
        cls.TESTNET = False
        cls.WIF_PREFIX = 0x80
        cls.ADDRTYPE_P2PKH = 0
        cls.ADDRTYPE_P2SH = 5
        cls.CASHADDR_PREFIX = "bitcoincash"
        cls.GENESIS = "000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f"
        cls.DEFAULT_PORTS = {'t': '50001', 's': '50002'}
        cls.DEFAULT_SERVERS = read_json_dict('servers.json')
        cls.TITLE = 'ElectrumSV'

        # Bitcoin Cash fork block specification
        cls.BITCOIN_CASH_FORK_BLOCK_HEIGHT = 478559
        cls.BITCOIN_CASH_FORK_BLOCK_HASH = (
            "000000000000000000651ef99cb9fcbe0dadde1d424bd9f15ff20136191a5eec"
        )

        ## This is a pre-split (BABC/BSV) checkpoint
        #cls.VERIFICATION_BLOCK_MERKLE_ROOT = (
        #    "3848ff6c001ebf78ec1a798c2002f154ace4ba6c0f0a58ccb22f66934eda7143"
        #)
        #cls.VERIFICATION_BLOCK_HEIGHT = 540250

        # A post-split SV checkpoint.
        cls.VERIFICATION_BLOCK_MERKLE_ROOT = (
            "2eb4a1d21caa056385dbedd7743878e481d26052092aba97b319a6459ff6fa1b"
        )
        cls.VERIFICATION_BLOCK_HEIGHT = 557957

    @classmethod
    def set_testnet(cls):
        cls.TESTNET = True
        cls.WIF_PREFIX = 0xef
        cls.ADDRTYPE_P2PKH = 111
        cls.ADDRTYPE_P2SH = 196
        cls.CASHADDR_PREFIX = "bchtest"
        cls.GENESIS = "000000000933ea01ad0ee984209779baaec3ced90fa3f408719526f8d77f4943"
        cls.DEFAULT_PORTS = {'t':'51001', 's':'51002'}
        cls.DEFAULT_SERVERS = read_json_dict('servers_testnet.json')
        cls.TITLE = 'ElectrumSV Testnet'

        # Bitcoin Cash fork block specification
        cls.BITCOIN_CASH_FORK_BLOCK_HEIGHT = 1155876
        cls.BITCOIN_CASH_FORK_BLOCK_HASH = (
            "00000000000e38fef93ed9582a7df43815d5c2ba9fd37ef70c9a0ea4a285b8f5e"
        )

        ## Bitcoin Cash fork block specification
        #cls.VERIFICATION_BLOCK_MERKLE_ROOT = (
        #    "029d920720e864945b8a5f97cd83e78e13fa001349cd1998815bdf2a6996dfa7"
        #)
        #cls.VERIFICATION_BLOCK_HEIGHT = 1248199

        cls.VERIFICATION_BLOCK_MERKLE_ROOT = (
            "2fde3bf6de5266bd7a2c65b6e6971f8aa5e7b839ee18523994309ab42a18a70c"
        )
        cls.VERIFICATION_BLOCK_HEIGHT = 1273000


NetworkConstants.set_mainnet()
