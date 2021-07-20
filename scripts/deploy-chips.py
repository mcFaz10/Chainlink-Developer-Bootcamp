from brownie import ChocChips, config, accounts
 
def deployContract():
    account1 = accounts[0]
    account2 = accounts[1]
    account = accounts.add(config["wallets"]["from_key"]) or accounts[0]
    ChocChips.deploy(1000000000000000000, {'from': account})
    tx = account1.transfer(account2,0)
    
    #ChocChips[0].transferFrom(0x5787D401f16C33932c68CAd522996445D4Ef4Bef,0xd36e903Ad861DdC94B88Ec27605c08716AA401D3,500000000000000000,{'from': account})
def main():
    deployContract()
    


