

# publish post on facebook page using facebook graph api v2.8 and python 3.6 without importing any library
# import requests
# import json
# import urllib.parse
# import urllib.request
# import urllib.error


# def publish_post_on_facebook_page(page_id, access_token, message, link, picture, name, caption, description):
#     post_url = 'https://graph.facebook.com/v2.8/%s/feed?message=%s&link=%s&picture=%s&name=%s&caption=%s&description=%s&access_token=%s' % (
#         page_id, message, link, picture, name, caption, description, access_token)
#     try:
#         response = urllib.request.urlopen(post_url)
#         response = json.loads(response.read())
#         print(response)
#     except urllib.error.HTTPError as e:
#         print(e.read())


# if __name__ == '__main__':
#     page_id = 'page_id'







# publish post on facebook page using facebook graph api v2.8 and python 3.6 with importing facebook library
# import facebook
# import requests
# import json
# import urllib.parse
# import urllib.request
# import urllib.error


# def publish_post_on_facebook_page(page_id, access_token, message, link, picture, name, caption, description):
#     graph = facebook.GraphAPI(access_token=access_token, version='2.8')
#     try:
#         response = graph.put_object(parent_object=page_id, connection_name='feed', message=message, link=link, picture=picture, name=name, caption=caption, description=description)
#         print(response)
#     except facebook.GraphAPIError as e:
#         print(e.read())


# if __name__ == '__main__':
#     page_id = 'page_id'














