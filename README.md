#Chamadas para API

### Create Propertie with correct data

curl -X POST http://localhost:5000/ -d '{"x":220, "y":500,
"title":"Imóvel código novo, com 3 quartos e 1 banheiro", "price":550000,
"description":"Casao danado sit amet, consectetur adipiscing elit.",
"beds":3, "baths":1, "squareMeters":210}' -H "Content-Type: application/json"

### Create Propertie with wrong data

curl -X POST "http://localhost:5000/api/v1/properties/" -d '{"y": "eite preula",
"title":"Apezao da horona, com 3 quartos e 1 banheiro", "price":450000,
"description":"Coordenadas numericas sem headers.",
"beds":3, "baths":1, "squareMeters":110}' -H "Content-Type: application/json" -v

### Get Propertie by ID

curl -X GET http://localhost:5000/api/v1/properties/ -v
