# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "library_managemnt"
app_title = "Libreria Gestionale"
app_publisher = "Saverio"
app_description = "facile gestione"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "s.petti@italjapan.net"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/library_managemnt/css/library_managemnt.css"
# app_include_js = "/assets/library_managemnt/js/library_managemnt.js"

# include js, css files in header of web template
# web_include_css = "/assets/library_managemnt/css/library_managemnt.css"
# web_include_js = "/assets/library_managemnt/js/library_managemnt.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "library_managemnt.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "library_managemnt.install.before_install"
# after_install = "library_managemnt.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "library_managemnt.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"library_managemnt.tasks.all"
# 	],
# 	"daily": [
# 		"library_managemnt.tasks.daily"
# 	],
# 	"hourly": [
# 		"library_managemnt.tasks.hourly"
# 	],
# 	"weekly": [
# 		"library_managemnt.tasks.weekly"
# 	]
# 	"monthly": [
# 		"library_managemnt.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "library_managemnt.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "library_managemnt.event.get_events"
# }

