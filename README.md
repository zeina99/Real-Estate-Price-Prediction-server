# Real-Estate-rent-price-prediction-server

Backend Application to serve model responses to the react native application

### App frontend: https://github.com/zeina99/Real-Estate-Price-Prediction-App


# Routes
`/` [ POST ] 

-  Gets the predicted price according to real estate property inputs 

Body content: 

`bedrooms`: (int) number of bedrooms

`bathrooms`: (int) number of bathrooms

`area`: (int) arae of the real estate property

`location`: (String) neighborhood location in Dubai 

`Description`: (String) description of the real estate property 



Sample response: 
```json
{
    "price": 593299.0
}
  ```
