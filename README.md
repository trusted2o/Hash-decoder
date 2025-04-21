# 🔐 Hash Decoder Tool (Python)

A simple Python script to crack MD5, SHA1, and SHA256 hashes using a wordlist.

## ⚙️ Usage

python hash_decoder.py --hash <HASH> --type md5 --wordlist wordlist.txt

# Options:
--hash: The target hash you want to crack (required)

--type: md5, sha1, or sha256 (default: md5)

--wordlist: Path to the wordlist (required)

--verbose: Show each attempt

# 🔍 Example
# Basic Crack:
python hash_decoder.py --hash 5f4dcc3b5aa765d61d8327deb882cf99 --wordlist wordlist.txt
# Crack SHA1:
python hash_decoder.py --hash 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8 --type sha1 --wordlist wordlist.txt
# Verbose Mode (see each guess):
python hash_decoder.py --hash e3afed0047b08059d0fada10f400c1e5 --type md5 --wordlist wordlist.txt --verbose


