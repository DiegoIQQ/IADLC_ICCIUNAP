import tweepy

#Detalles personales
consumer_key = "H6z8EvUvLuH0Wh1u5mrHHvixp"
consumer_secret = "Ur5t9drG9WXwHPfNoTVn9bKSwOODbWBCVHQeRYCSHJJFnsAUee"
access_token = "1179862702958809098-eIR9HIviXeOzYpVI3SuJjfmlO4jEjj"
access_token_secret = "i50yVujxc64CXZsPalKeDbjqUr3BEwsxGyBAsb2BlzSV8"

#Autenticacion de clave y consumidor secreto
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
tweet = "DLC IA, Test Tweet"
image_path = "..\\images\\stitch.gif"
  
#Actualizacion del estado
status = api.update_with_media(image_path, tweet)
api.update_status(status = tweet)