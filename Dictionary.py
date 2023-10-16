crypto_dictionary = {
    "CBDC": "Central Bank Digital Currency",
    "CEX": "Centralized Exchange",
    "DAO": "Decentralized Autonomous Organization",
    "Dapp": "Decentralized application",
    "DEX": "Decentralized Exchange",
    "DeFi": "Decentralized Finance",
    "DYOR": "Do Your Own Research",
    "EIP": "Ethereum Improvement Proposal",
    "EVM": "Ethereum Virtual Machine",
    "ICO": "Initial Coin Offering",
    "IPFS": "Interplanetary File System",
    "LP": "Liquidity Provider",
    "NFT": "Non-Fungible Token",
    "TVL": "Total Value Locked",
    "WAGMI": "We Are All Gonna Make It",
    "ZK": "Zero Knowledge",
}
tech_dictionary = {
    "AI": "Artificial Intelligence",
    "AGI": "Artificial General Intelligence",
    "AR": "Augmented Reality",
    "FTP": "File Transfer Protocol",
    "HTTP": "HyperText Transfer Protocol",
    "IT": "Information Technology",
    "OPSEC": "Operations Security",
    "P2P": "Peer-To-Peer",
    "SSL": "Secure Socket Layer",
    "UI": "User Interface",
    "UX": "User Experience",
    "VM": "Virtal Machine",
    "VPN": "Virtual Private Network",
    "VR": "Virtual Reality",
    "WWW": "World Wide Web",
}
fin_dictionary = {
    "AML": "Anti-Money Laundering",
    "APR": "Annual Percentage Rate",
    "APY": "Annual Percentage Yield",
    "ATH": "All-Time-High",
    "B2B": "Business-To-Business",
    "B2C": "Business-To-Customer",
    "CEO": "Chief Executive Officer",
    "CFO": "Chief Financial Officer",
    "CPI": "Consumer Price Index",
    "ESG": "Environmental Social Governance",
    "ETF": "Exchange-Traded Fund",
    "ETP": "Exchange Traded Products",
    "FA": "Fundamental Analysis",
    "KYC": "Know Your Customer",
    "MLM": "Multi-Level Marketing",
    "MVP": "Minimum Viable Product",
    "OTC": "Over-The-Counter",
    "PPI": "Producer Price Index",
    "RSI": "Relative Strength Index",
    "SPAC": "Special Purpose Aqcuisition Company",
    "TA": "Technical Analysis",
    "VAT": "Value-Added Tax",
    "VP": "Vice Precident",
    "YTD": "Year-To-Date",
}
entities_dictionary = {
    "BIS": "Bank for International Settlements",
    "CFTC": "Commodity Futures Trading Commission",
    "ECB": "European Central Bank",
    "IMF": "International Monetary Fund",
    "SEC": "Securities and Exchange Commission ",
    "WEF": "World Economic Forum",
}
vls = []
brk = ["N", "n"]
while True:
    print("Which of the following dictionaries would you like to access?")
    inp1 = input("A: Cryptocurrency | B: Tech | C: Finance | D: Entities | E: all of the above\n")
    if inp1 == "A" or inp1 == "a":
        for x in crypto_dictionary:
            print(f"{x}: {crypto_dictionary[x]}")
    elif inp1 == "B" or inp1 == "b":
        for x in tech_dictionary:
            print(f"{x}: {tech_dictionary[x]}")
    elif inp1 == "C" or inp1 == "c":
        for x in fin_dictionary:
            print(f"{x}: {fin_dictionary[x]}")
    elif inp1 == "D" or inp1 == "d":
        for x in entities_dictionary:
            print(f"{x}: {entities_dictionary[x]}")
    elif inp1 == "E" or inp1 == "e":
        print("CRYPROCURRENCY:\n")
        for x in crypto_dictionary:
            print(f"{x}: {crypto_dictionary[x]}")
        print("\nTECHNOLOGY:\n")
        for x in tech_dictionary:
            print(f"{x}: {tech_dictionary[x]}")
        print("\nFINANCE:\n")
        for x in fin_dictionary:
            print(f"{x}: {fin_dictionary[x]}")
        print("\nENTITIES:\n")
        for x in entities_dictionary:
            print(f"{x}: {entities_dictionary[x]}")
    else:
        print("Not an accepted answer")
    conf = input("\nPress anything to continue or 'N' to quit. ")
    if conf in brk:
        break
