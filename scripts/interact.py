from brownie import FirstBrownie, config, accounts, network

def main():
    account = accounts.add(config["wallets"]["from_key"])
    firstBrownie = FirstBrownie[-1]
    a = firstBrownie.addNum(1)
    tx = firstBrownie.setNumber(a,{'from': account})
    tx.wait(1)
    print("Number is", firstBrownie.getNumber({'from': account}))
 
