# Battle.net-Mobile-Authenticator-android-decoder
Decode the Battle.net mobile authenticator's token so you can generate it's TOTP code using other TOTP generator like Google Authenticator. A rooted android is required.
Python version of https://gist.github.com/stbuehler/8616943.

# Requirement 
pyotp
A rooted android with battle.net mobile authenticator installed and login.
A TOTP client that support 8 digit code.

# Usage
The token can be found at /data/data/com.blizzard.bma/shared_prefs/com.blizzard.bma.AUTH_STORE.xml in the property "com.blizzard.bma.AUTH_STORE.HASH" using a rooted android.
Run the script, input the token, and copy the TOTP secret to your TOTP client.
