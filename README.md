Super simple tool to distribute SPL tokens on Solana.

Distribute easily, quickly and cheaply directly to addresses.


Tested on devnet and mainnet.

But still use at your own risk!

Check transactions before reattempting.




# Installation and prequisities
### Spl token cli
```bash
cargo install spl-token-cli
```


### Python
https://python.org/




# Setting up environment

```bash
solana config set --url https://api.devnet.solana.com
```

OR

```bash
solana config set --url https://api.mainnet-beta.solana.com
```

OR (the best)

```bash
solana config set --url CUSTOM RPC
```


### Setting up wallet
```bash
solana-keygen new --outfile ~/.config/solana/wallet.json
```
You will get wallet address and seed

Be sure to save this to some safe place

### Set keypair
```bash
solana config set --keypair ~/.config/solana/wallet.json
```


### Now check everything is set correctly
```bash
solana config get
```


### If on devnet
```bash
solana airdrop 1
```


### If on mainnet
Funds wallet with mainnet solana


### Check funds on keypair wallet
```bash
solana balance
```
## Important
Each address airdrop will cost approx 0.0021 Sol, so make sure to fund your wallet properly!




# If you don't have any token yet
```bash
spl-token create-token
```
```bash
spl-token create-account "token address here without ("") special characters"
```
```bash
spl-token mint "token address here without ("") special characters" 1000
```



# Airdrop to addresses


Add addresses to airdrop.txt, 1 line = 1 address, no commas, no "".


Open airdrop.py and edit line number 5, add your token address and number of tokens each address shall receive.


Open terminal and run
```bash
python airdrop.py
```



# Final things
Now you can enjoy success.

If this was used to airdrop token to whitelisted addresses, make sure to add corect data to config in metaplex.


If this was useful to you, you can send donation, NFT or your token to our community wallet
DdTMFWstpAdQcWv3qBWEJrJBjqpkziz9dchs87U2661e

Or try solana fee redeemer tool (donations go to our community wallet)
https://solanafeeredeemer.com/

Community wallet belongs to Solana NFT project- R.U.R. World (https://twitter.com/RURWorld ; https://rur.world/links)

NFTs full of utility (https://info.rur.world/)

Our holders receive cut from community wallet and can have custom NFT collection (on Solana, Ethereum, Polygon, Fantom or Avax) with us helping them with marketing, generate, deploy collection, distribute whitelist and build mint web, FREE of initital investment charges (only for % from royalties and mint funds to our community wallet)
