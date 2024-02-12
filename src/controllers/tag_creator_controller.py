from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler

class TagCreatorController:
    '''
        responsability for implementing businnes rules
    '''

    def create(self, product_code: str) -> Dict:
        path_from_tag = self.__create_tag(product_code)
        formatted_response = self.__format_reponse(path_from_tag)
        return formatted_response

    # Metodos privados:
    def __create_tag(self, product_code: str) -> str:
        barcode_handler = BarcodeHandler()
        path_from_tag = barcode_handler.create_barcode(product_code)
        return path_from_tag
    

    def __format_reponse(self, path_from_tag:str) -> Dict:
        return {
            "data":{
                "type": "Tag image",
                "count": 1,
                "path": f"{path_from_tag}.png"
            }
        }