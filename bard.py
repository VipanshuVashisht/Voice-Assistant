from bardapi import BardCookies
import datetime
cookie_dict = {
    "__Secure-IPSID" : "pyBUwfQwUqPP3hTj/AjT4Dzwg2TUxP3HeA",
    "__Secure-IPSIDTS" : "sidts-CjEBPVxjSuRHEy2KC6Ye3hVBGw41DPGuKSu3k6d69Js7sEI28Cl2qHffCMP5tywr1HKnEAA",
    "__Secure-IPSIDCC" : "ACA-OxMUH39COASliRxUioVEuCtTFVs4RrMVkzVp0lzdAc2S74D0ZbvIkvnr5jsolYcQ4bxdxEo",
}

bard = BardCookies(cookie_dict=cookie_dict)

while True:
    Query = input("Enter your query: ")
    Reply = bard.get_answer(Query)['content']
    print(Reply)
