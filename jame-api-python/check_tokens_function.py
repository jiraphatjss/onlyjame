from lib import *

def aCARDdogeduel1_json():
    request_url = "https://cryptoknights.games/assets/tokens/aCARDdogeduel1.json"
    response = requests.get(request_url)
    response_json = json.loads(response.text)
    schema = {
        "type":"object",
        "required": [
            "name",
            "description",
            "image",
            "external_url",
            "attributes"
        ],
        "properties": {
            "name":{
                "type":"string"
            },
            "description": {
                "type":"string"
            },
            "image": {
                "type":"string"
            },
            "external_url":{
                "type":"string"
            },
            "attributes":{
                "type":"array",
                "items": [
                    {
                        "type":"object",
                        "required": [
                            "trait_type",
                            "value"
                        ],
                        "properties": {
                            "trait_type": {
                                "type":"string",
                                "enum":["Artist"]
                            },
                            "value": {
                                "type":"string",
                                "enum":["CryptoKnights"]
                            }
                        }
                    },
                    {
                        "type":"object",
                        "required": [
                            "trait_type",
                            "value"
                        ],
                        "properties": {
                            "trait_type": {
                                "type":"string",
                                "enum":["Event"]
                            },
                            "value": {
                                "type":"string",
                                "enum":["DogeDuel"]
                            }
                        }
                    },
                    {
                        "type":"object",
                        "required": [
                            "trait_type",
                            "value"
                        ],
                        "properties": {
                            "trait_type": {
                                "type":"string",
                                "enum":["Magic Level"]
                            },
                            "value": {
                                "type":"string",
                                "enum":["XX"]
                            }
                        }
                    }
                ]
            }
        }
    }
    validate(instance=response_json, schema=schema)            
    assert response.status_code == 200



