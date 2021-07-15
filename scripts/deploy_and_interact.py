from brownie import FirstBrownie, config, accounts
 
def deployContract():
    account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    FirstBrownie.deploy({'from': account})
    firstBrownie = FirstBrownie[-1]
    tx = firstBrownie.setNumber(123456,{'from': account})
    tx.wait(1)
    print("Number is", firstBrownie.getNumber({'from': account}))
 
def main():
    deployContract()
