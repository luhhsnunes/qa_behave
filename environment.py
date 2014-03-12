from browser import my_browser

def before_feature(context, feature):
  context.browser = my_browser()

def after_feature(context, feature):
  context.browser.close()
