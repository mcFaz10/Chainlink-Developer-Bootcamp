from brownie import FirstBrownie, config, accounts
 
def deployContract():
    account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    FirstBrownie.deploy({'from': account})
 
def main():
    deployContract()
