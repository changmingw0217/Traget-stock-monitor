import requests
import json
from discord_webhook import DiscordWebhook, DiscordEmbed
import time


if __name__ == '__main__':
    product_id = "81114595"
    zip_code = "14228"
    url = "https://api.target.com/fulfillment_aggregator/v1/fiats/" + product_id + "?key=ff457966e64d5e877fdbad070f276d18ecec4a01&nearby=" + zip_code + "&limit=20&requested_quantity=1&radius=50&fulfillment_test_mode=grocery_opu_team_member_test"

    while True:

        r = requests.get(url)
        dictionary = json.loads(r.text)
        # print(dictionary)
        # print(len(dictionary['products'][0]['locations']))
        store_infos = dictionary['products'][0]['locations']
        for store in store_infos:
            # print(store['order_pickup']['availability_status'])
            # print(store['curbside']['availability_status'])
            # print(store['ship_to_store']['availability_status'])
            # print(store['in_store_only']['availability_status'])

            if store['order_pickup']['availability_status'] != "UNAVAILABLE" and store['order_pickup']['availability_status'] != "OUT_OF_STOCK":
                print("IN_STOCK")
                # urls = "https://discordapp.com/api/webhooks/531169449659727875/mtwi_XVPibEdXURLmj_28RNubT_DG3VdIv45ZNHiXeF8nqsd6UNPDE5MiBnXvDS7oMQt"
                # webhook = DiscordWebhook(url=urls, content='Target Restock')
                # response = webhook.execute()
            if store['curbside']['availability_status'] != "UNAVAILABLE" and store['curbside']['availability_status'] != "OUT_OF_STOCK":
                print("IN_STOCK")
                # urls = "https://discordapp.com/api/webhooks/531169449659727875/mtwi_XVPibEdXURLmj_28RNubT_DG3VdIv45ZNHiXeF8nqsd6UNPDE5MiBnXvDS7oMQt"
                # webhook = DiscordWebhook(url=urls, content='Target Restock')
                # response = webhook.execute()
            if store['ship_to_store']['availability_status'] != "UNAVAILABLE" and store['ship_to_store']['availability_status'] != "OUT_OF_STOCK":
                print("IN_STOCK")
                # urls = "https://discordapp.com/api/webhooks/531169449659727875/mtwi_XVPibEdXURLmj_28RNubT_DG3VdIv45ZNHiXeF8nqsd6UNPDE5MiBnXvDS7oMQt"
                # webhook = DiscordWebhook(url=urls, content='Target Restock')
                # response = webhook.execute()
            if store['in_store_only']['availability_status'] != "UNAVAILABLE" and store['in_store_only']['availability_status'] != "OUT_OF_STOCK":
                print("IN_STOCK")
                # urls = "https://discordapp.com/api/webhooks/531169449659727875/mtwi_XVPibEdXURLmj_28RNubT_DG3VdIv45ZNHiXeF8nqsd6UNPDE5MiBnXvDS7oMQt"
                # webhook = DiscordWebhook(url=urls, content='Target Restock')
                # response = webhook.execute()
        print("No stock. Sleep for 15s")
        time.sleep(15)

