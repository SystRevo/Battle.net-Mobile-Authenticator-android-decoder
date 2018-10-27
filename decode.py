import base64

# Python version of https://gist.github.com/stbuehler/8616943
# This token can be found at /data/data/com.blizzard.bma/shared_prefs/com.blizzard.bma.AUTH_STORE.xml
# in the property "com.blizzard.bma.AUTH_STORE.HASH" using a rooted android.
# The token is 57 bytes of data in hex form, which is 114 chars in hex form. 
token = ""

# After using xor with each value in masks, the first 40 bytes of the result are the secret data in 
# binary, and the last 17 bytes are the serial number.
# magical mask 
masks = [57,142,39,252,80,39,106,101,96,101,176,229,37,244,192,108,4,198,16,117,40,107,142,\
    122,237,165,157,169,129,59,93,214,200,13,47,179,128,104,119,63,165,155,164,124,23,202,108,\
    100,121,1,92,29,91,139,143,107,154]

def main():
    token = input("Please input your token found on your android: ")
    data = list(bytes.fromhex(token))
    assert len(data) == len(masks)
    # xor every byte with masks
    for i in range(0, len(data)):
        b = data[i]
        m = masks[i]
        b = b ^ m
        data[i] = b
    data_str = bytes(data).decode()
    secret_hex = data_str[:40]
    serial = data_str[40:]
    # use base32 to encode the first 40 bytes to be used in totp
    secret = base64.b32encode(bytes.fromhex(secret_hex)).decode()
    from pyotp import TOTP
    totp = TOTP(secret, digits=8)
    key = totp.now()
    print(secret)
    print(serial)
    print(key)

    url = "otpauth://totp/{0}:{0}?secret={1}&issuer={0}&digits=8".format(serial, secret)
    print(url)

if __name__ == "__main__":
    main()