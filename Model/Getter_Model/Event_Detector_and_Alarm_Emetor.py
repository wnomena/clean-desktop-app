from plyer.facades import Audio
from itertools import zip_longest
import asyncio

from Model.SQLAlchemy.schema import Contact_Model_without_Pydantic
class Detector_and_Emitter:
    def __init__(self):
        self.Alarm = Audio("path-for-alarm-mp3")
        self.temp_contact:list[Contact_Model_without_Pydantic] = []
 


    async def detector(self,contact:list[Contact_Model_without_Pydantic]):
            for internal_temp in contact:
                for key_2,external_temp in enumerate(self.temp_contact):
                    if internal_temp != external_temp and key_2 == len(self.temp_contact) - 1:
                        self.temp_contact.append(internal_temp)
                        self.Alarm.start()
                        await asyncio.sleep(10)
                        self.Alarm._stop()
                    asyncio.sleep(0)
                asyncio.sleep(0)