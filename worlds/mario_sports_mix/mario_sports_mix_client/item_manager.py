from .memory_addresses import *
import dolphin_memory_engine as dme
from .MSMContext import MSMContext


class ItemManager:
    dme = dme

    def has_item(self):
        current_item = self.dme.read_word(PlayerAddresses.item_held)
        if current_item == -1:
            return False
        else:
            return True

    async def handle_one_time_items(self, filler_to_give):
        current_coins = self.dme.read_word(PlayerAddresses.Score.coins)
        has_item = self.has_item()

        for filler in filler_to_give:
            if filler == "1 Coin":
                if current_coins < 10:
                    self.dme.write_word(PlayerAddresses.Score.coins, current_coins + 1)
                    filler_to_give.remove("1 Coin")
            if filler == "1 Green Shell":
                if not has_item:
                    self.dme.write_word(PlayerAddresses.item_held, 1)
                else:
                    filler_to_give.remove("1 Green Shell")



