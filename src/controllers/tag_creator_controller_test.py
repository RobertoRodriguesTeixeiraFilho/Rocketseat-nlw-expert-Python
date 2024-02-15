from unittest.mock import patch
from src.drivers.barcode_handler import BarcodeHandler
from .tag_creator_controller import TagCreatorController

@patch.object(BarcodeHandler, 'create_barcode') # Criação de espelhos
def test_create(mock_create_barcode):
    mock_value = "image_path" # Nome da imagem/tag criada
    mock_create_barcode.return_value = mock_value # Não acessa mais o barcode, mas um "espelho" do mesmo
    tag_creator_controller = TagCreatorController()

    result = tag_creator_controller.create(mock_value)

    assert isinstance(result, dict)
    assert "data" in result
    assert "type" in result["data"] # Confere se as propriedades estão sempre retornando
    assert "count" in result["data"]
    assert "path" in result["data"]

    assert result["data"]["type"] == "Tag image"
    assert result["data"]["count"] == 1
    assert result["data"]["path"] == f"{mock_value}.png"
