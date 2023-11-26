class Shop:

    @staticmethod
    def get_result():
        strings_count = int(input('Enter number of buyers: '))
        buys = []
        for item in range(strings_count):
            buys.append(input('Enter Name | What he/she had buy | count:\n'))

        buyers = []
        shop_dict = {}

        for purchase in buys:
            items = purchase.split()
            has_buyer = False
            for buyer in buyers:
                if buyer == items[0]:
                    has_buyer = True

            if not has_buyer:
                buyers.append(items[0])
                
        # Need create a method what will fill this dict
