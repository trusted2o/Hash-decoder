import argparse
import hashlib

def get_hash(word, hash_type):
    word_bytes = word.encode()
    if hash_type == "md5":
        return hashlib.md5(word_bytes).hexdigest()
    elif hash_type == "sha1":
        return hashlib.sha1(word_bytes).hexdigest()
    elif hash_type == "sha256":
        return hashlib.sha256(word_bytes).hexdigest()
    else:
        raise ValueError("Unsupported hash type.")

def crack_hash(target_hash, hash_type, wordlist, verbose=False):
    try:
        with open(wordlist, "r", encoding="utf-8", errors="ignore") as file:
            for word in file:
                word = word.strip()
                hashed = get_hash(word, hash_type)

                if verbose:
                    print(f"Trying: {word} -> {hashed}")

                if hashed == target_hash.lower():
                    print(f"\n[+] Hash cracked! Password: {word}")
                    return
        print("[-] No match found in the wordlist.")
    except FileNotFoundError:
        print(f"[!] Wordlist file not found: {wordlist}")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-Algorithm Hash Cracker")
    parser.add_argument("--hash", required=True, help="The hash to crack")
    parser.add_argument("--type", choices=["md5", "sha1", "sha256"], default="md5", help="Hash type")
    parser.add_argument("--wordlist", required=True, help="Path to wordlist file")
    parser.add_argument("--verbose", action="store_true", help="Show each attempt")

    args = parser.parse_args()
    crack_hash(args.hash, args.type, args.wordlist, args.verbose)
