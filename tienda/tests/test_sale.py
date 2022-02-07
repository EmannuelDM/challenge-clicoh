import pytest
from applications.users.models import User
import requests

def test_sale_creation():
    sale_data = {
            "products":[

                {"pk":"2",
                "cuantity":7
                },
                    {"pk":"3",
                "cuantity":4
                },
                {"pk":"2",
                "cuantity":30
                }

            
            ]
        }
    correct_response = {
    "status": "ok",
    "msg": "Successfully created"
}

    response = requests.post("http://127.0.0.1:8000/sales/", json = sale_data, headers={"Authorization": "Token  afbb9b9c2702fd53449171c61524ee88adb06d6a"})

    assert response.json() == correct_response

