import tweepy

#Detalles personales
consumer_key = "H6z8EvUvLuH0Wh1u5mrHHvixp"
consumer_secret = "Ur5t9drG9WXwHPfNoTVn9bKSwOODbWBCVHQeRYCSHJJFnsAUee"
access_token = "1179862702958809098-eIR9HIviXeOzYpVI3SuJjfmlO4jEjj"
access_token_secret = "i50yVujxc64CXZsPalKeDbjqUr3BEwsxGyBAsb2BlzSV8"

#Autenticacion de clave y consumidor secreto
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
#Autenticacion del acceso del token y el secreto 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth) 
  
#Actualizacion del estado
api.update_status(status ="DLC IA, Hello world !  #DLCIA") 