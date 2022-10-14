import requests, os
import matplotlib.pyplot as plt
import numpy as np

url = "https://bravenewcoin.p.rapidapi.com/market-cap"
coinToID = {
    'BTC' : 'f1ff77b6-3ab4-4719-9ded-2fc7e71cff1f',
    'RISE' : '2686a8d9-ac25-491c-9638-e4a58e63cfe6',

}

coinName = 'BTC'

querystring = {"assetId":coinToID[coinName]}

headers = {
	"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5EVXhNRGhHT0VReE56STVOelJCTTBJM1FrUTVOa0l4TWtRd1FrSTJSalJFTVRaR1F6QTBOZyJ9.eyJpc3MiOiJodHRwczovL2F1dGguYnJhdmVuZXdjb2luLmNvbS8iLCJzdWIiOiJvQ2RRb1pvSTk2RVJFOUhZM3NRN0ptYkFDZkJmNTVSWUBjbGllbnRzIiwiYXVkIjoiaHR0cHM6Ly9hcGkuYnJhdmVuZXdjb2luLmNvbSIsImlhdCI6MTY2NTY0ODMxNiwiZXhwIjoxNjY1NzM0NzE2LCJhenAiOiJvQ2RRb1pvSTk2RVJFOUhZM3NRN0ptYkFDZkJmNTVSWSIsInNjb3BlIjoicmVhZDppbmRleC10aWNrZXIgcmVhZDpyYW5raW5nIHJlYWQ6bXdhIHJlYWQ6Z3dhIHJlYWQ6YWdncmVnYXRlcyByZWFkOm1hcmtldCByZWFkOmFzc2V0IHJlYWQ6b2hsY3YgcmVhZDptYXJrZXQtY2FwIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.noynjbonQs7qmHe-7WH0DMngAQ6JezWGpS2QXscemwcg1VsLZHgUASppWfCk233k-dGVptzmfPEO7uFxyDD6uaTx8X6W2eKnRhY0y9WAtunUCK_tj-DssB7vdvnHYKff5Vmcj0YCQDlfr3T82YtzLGD-b_lo2oHZXRDXuQZB0F6AJjWzSsfhbyUMQd-8vSUDo0itG5i6hwgJYhZPlOex780-q58zBDTVV75T7Gehf7Jgq4JegxkcQF7h6cXX2EIifttEWOfYxEFlo-8v1M76ULANK-ljEISz0_iVFkQXW8PtmPsccWBgyoC4DlghtirkWCJy5qXGbeU5qmyqt7H5OQ",
	"X-RapidAPI-Key": "93295dd330msh36f1be01e7edc34p17282ejsnc478a05c162e",
	"X-RapidAPI-Host": "bravenewcoin.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)


# new variable
# a list of a dictionary 
coinDataJson = response.json()['content']

# creating a dictionary with each piece of data
coinDict = coinDataJson[0]

# The Data:
#     id
#     assetID
#     timestamp
#     marketCapRank
#     volumeRank
#     price
#     volume
#     totalSupply
#     freeFloatSupply
#     marketCap
#     totalMarketCap

# clear screen
os.system('cls' if os.name == 'nt' else 'clear')

# grabbing variables
price = coinDict['price']
marketCap = coinDict['marketCap']

# print
print('Price of '+coinName+' is:\n'+str(price))

fig, ax = plt.subplots()
ax.bar(2, price, label=coinName, color='green')
ax.legend(title='Coins')

# plt.plot([-1000, price, price], 'g^')
plt.ylabel('Value of '+coinName+' (in USD)')
plt.grid('true','both','y')
plt.axis([0, 6, 0, price*1.3])
plt.show()
plt.xticks([1])


response.close()