# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# AppConfig configuration made easy. Look inside private/appconfig.ini
# Auth is for authenticaiton and access control
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Auth
import os
import re

import gluon

REQUIRED_WEB2PY_VERSION = "3.0.10"

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

web2py_version_string = request.global_settings.web2py_version.split("-")[0]
web2py_version = list(map(int, web2py_version_string.split(".")[:3]))
if web2py_version < list(map(int, REQUIRED_WEB2PY_VERSION.split(".")[:3])):
    raise HTTP(500, f"Requires web2py version {REQUIRED_WEB2PY_VERSION} or newer, not {web2py_version_string}")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
# request.requires_https()

# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
configuration = AppConfig(reload=True)

if "GAE_APPLICATION" not in os.environ:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(configuration.get("db.uri"),
             pool_size=configuration.get("db.pool_size"),
             migrate_enabled=configuration.get("db.migrate"),
             check_reserved=["all"])
else:
    # ---------------------------------------------------------------------
    # connect to Google Firestore
    # ---------------------------------------------------------------------
    db = DAL("firestore")
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be "controller/function.extension"
# -------------------------------------------------------------------------
response.generic_patterns = [] 
if request.is_local and not configuration.get("app.production"):
    response.generic_patterns.append("*")

# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = "bootstrap4_inline"
response.form_label_separator = ""

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = "concat,minify,inline"
# response.optimize_js = "concat,minify,inline"

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = "0.0.0"

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=configuration.get("host.names"))

# -------------------------------------------------------------------------
# create all tables needed by auth, maybe add a list of extra fields
# -------------------------------------------------------------------------
auth.settings.extra_fields["auth_user"] = []
auth.define_tables(username=False, signature=False)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = "logging" if request.is_local else configuration.get("smtp.server")
mail.settings.sender = configuration.get("smtp.sender")
mail.settings.login = configuration.get("smtp.login")
mail.settings.tls = configuration.get("smtp.tls") or False
mail.settings.ssl = configuration.get("smtp.ssl") or False

# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

# -------------------------------------------------------------------------  
# read more at http://dev.w3.org/html5/markup/meta.name.html               
# -------------------------------------------------------------------------
response.meta.author = configuration.get("app.author")
response.meta.description = configuration.get("app.description")
response.meta.keywords = configuration.get("app.keywords")
response.meta.generator = configuration.get("app.generator")
response.show_toolbar = configuration.get("app.toolbar")

# -------------------------------------------------------------------------
# your http://google.com/analytics id                                      
# -------------------------------------------------------------------------
response.google_analytics_id = configuration.get("google.analytics_id")

# -------------------------------------------------------------------------
# maybe use the scheduler
# -------------------------------------------------------------------------
if configuration.get("scheduler.enabled"):
    from gluon.scheduler import Scheduler
    scheduler = Scheduler(db, heartbeat=configuration.get("scheduler.heartbeat"))

# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table("mytable", Field("myfield", "string"))
#
# Fields can be "string","text","password","integer","double","boolean"
#       "date","time","datetime","blob","upload", "reference TABLENAME"
# There is an implicit "id integer autoincrement" field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield="value")
# >>> rows = db(db.mytable.myfield == "value").select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------
db.define_table("client",
                 Field("name", "string", max_length=50),
                 Field("status", "string", requires=IS_IN_SET(["Past", "Lead", "Active"])),
                 Field("phone",
                       "string",
                       length=16,
                       requires=IS_MATCH(
                            r"^\+[1-9]\d{7,14}$",
                            error_message="Use formato E.164: +351912345678"
                       )
                      ),
                 Field("email", "string"),
                 Field("ltv", "double"),
                 Field("lead_src", "string", requires=IS_IN_SET(["Past", "Lead", "Active"])),
                )

#torna todos os campos obrigatórios
for field in db.client.fields:
     db.client[field].requires = IS_NOT_EMPTY



db.define_table("service",
                 Field("name", "string", max_length=50),
                 Field("base_price", "double"),
                 Field("type", "string", requires=IS_IN_SET(["Retainer(monthly)", "One-off Project"])),
                 Field("deliverables", "string", max_lenght=30),
                 Field("description", "text", max_length=1000),
                 Field("status", "string", requires=IS_IN_SET(["Active", "Experimental"])),
                )

#torna todos os campos obrigatórios menos Descricao
for field in db.client.fields:
     db.client[field].requires = IS_NOT_EMPTY



db.define_table("project",
                 Field("name", "string", max_length=50),
                 Field("client_id", "reference client"),
                 Field("service_id", "reference service"),
                 Field("deadline", "date"),
                 Field("value", "double"),
                 Field("progress" "double", default=0.0),
                 Field("description", "text", max_length=1000),
                 Field("status", "string", requires=IS_IN_SET(["In Progress", "Done", "Not Started"])),
                )


# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)
