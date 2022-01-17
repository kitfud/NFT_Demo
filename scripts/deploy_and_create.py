from scripts.helpful_scripts import get_account
from brownie import SimpleCollectible

OPENSEA_URL = "https://testnets.opensea.io/{}/{}"

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def main():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(sample_token_uri, {"from": account})
    tx.wait(1)
    print(
        f"Awsome, NFT ready for viewing at {OPENSEA_URL.format(simple_collectible.address,simple_collectible.tokenCounter()-1)}"
    )
