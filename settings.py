import os
import tornado.options

tornado.options.define("environment", default="dev", help="environment")

active_theme = "usv"
site_title = "Union Square Ventures"
site_description ="Union Square Ventures (USV) is a New York City-based venture capital firm. We invest in networks that transform existing industries"

options = {
  'dev' : {
    'mongo_database' : {'host' : os.environ.get('MONGODB_URL'), 'port' : 27017, 'db' : os.environ.get('DB_NAME')},
    'base_url' : 'localhost:8001',
  },
  'test' : {
    'mongo_database' : {'host' : os.environ.get('MONGODB_URL'), 'port' : 27017, 'db' : os.environ.get('DB_NAME')},
    'base_url' : os.environ.get('BASE_URL'),
  },
  'prod' : {
    'mongo_database' : {'host' : os.environ.get('MONGODB_URL'), 'port' : 27017, 'db' : os.environ.get('DB_NAME')},
    'base_url' : 'www.usv.com',
  }
}

default_options = {
  # twiter details (using knowabout.it keys for testing)
  'twitter_consumer_key' : os.environ.get("TWITTER_CONSUMER_KEY"),
  'twitter_consumer_secret' : os.environ.get("TWITTER_CONSUMER_SECRET"),

  # disqus details (using greentile keys for testing)
  'disqus_public_key': os.environ.get("DISQUS_PUBLIC_KEY"),
  'disqus_secret_key': os.environ.get("DISQUS_SECRET_KEY"),
  'disqus_short_code': os.environ.get("DISQUS_SHORTNAME"),

  # sendgrid details
  'sendgrid_user': os.environ.get("SENDGRID_USER"),
  'sendgrid_secret': os.environ.get("SENDGRID_SECRET"),

  # hackpad details
  'hackpad_oauth_client_id': os.environ.get("HACKPAD_OAUTH_CLIENT_ID"), 
  'hackpad_oauth_secret': os.environ.get("HACKPAD_OAUTH_SECRET"), 
  'hackpad_domain': os.environ.get("HACKPAD_DOMAIN"),

  # google api key
  'google_api_key': os.environ.get("GOOGLE_API_KEY"),

  # bitly access token
  'bitly_access_token': os.environ.get("BITLY_ACCESS_TOKEN"),

  # other control variables
  'tinymce_valid_elements': '',
  'post_char_limit': 1000,
  'sticky': None,
  'read_only' : False,
  'max_simultaneous_connections' : 10,
  'hot_post_set_count': 200,
  'staff':[
    "a-staff-member's-username"
  ],

  # define the various roles and what capabilities they support
  'staff_capabilities': [
    'see_admin_link',
    'delete_users',
    'delete_posts',
    'post_rich_media',
    'feature_posts',
    'edit_posts',
    'upvote_multiple_times',
    'super_upvote_posts',
    'downvote_posts'
  ],
  'user_capabilities': []
}

def get(key):
  # check for an environmental variable (used w Heroku) first
  if os.environ.get('ENVIRONMENT'):
    env = os.environ.get('ENVIRONMENT')
  else:
    env = tornado.options.options.environment
  
  if env not in options:
    raise Exception("Invalid Environment (%s)" % tornado.options.options.environment)

  v = options.get(env).get(key) or default_options.get(key)

  if callable(v):
    return v

  if v is not None:
    return v

  return default_options.get(key)

