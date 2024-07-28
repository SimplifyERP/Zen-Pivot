app_name = "zen_pivot"
app_title = "Zen Pivot"
app_publisher = "Zen Pivot"
app_description = "Transforming businesses with innovative solutions that harmonize strategy and execution. Elevate your operations with our expert guidance and achieve balance in a dynamic marketplace."
app_email = "zenpivot@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/zen_pivot/css/zen_pivot.css"
# app_include_js = "/assets/zen_pivot/js/zen_pivot.js"

# include js, css files in header of web template
# web_include_css = "/assets/zen_pivot/css/zen_pivot.css"
# web_include_js = "/assets/zen_pivot/js/zen_pivot.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "zen_pivot/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "zen_pivot/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "zen_pivot.utils.jinja_methods",
# 	"filters": "zen_pivot.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "zen_pivot.install.before_install"
# after_install = "zen_pivot.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "zen_pivot.uninstall.before_uninstall"
# after_uninstall = "zen_pivot.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "zen_pivot.utils.before_app_install"
# after_app_install = "zen_pivot.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "zen_pivot.utils.before_app_uninstall"
# after_app_uninstall = "zen_pivot.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "zen_pivot.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"zen_pivot.tasks.all"
# 	],
# 	"daily": [
# 		"zen_pivot.tasks.daily"
# 	],
# 	"hourly": [
# 		"zen_pivot.tasks.hourly"
# 	],
# 	"weekly": [
# 		"zen_pivot.tasks.weekly"
# 	],
# 	"monthly": [
# 		"zen_pivot.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "zen_pivot.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "zen_pivot.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "zen_pivot.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["zen_pivot.utils.before_request"]
# after_request = ["zen_pivot.utils.after_request"]

# Job Events
# ----------
# before_job = ["zen_pivot.utils.before_job"]
# after_job = ["zen_pivot.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"zen_pivot.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

