# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    (T('Home'), False, URL('default', 'home'), [])
    (T('Finances'), False, URL('default', 'finances'), [])
    (T('Pipeline'), False, URL('default', 'pipeline'), [])
    (T('Clients'), False, URL('default', 'clients'), [])
    (T('Tasks'), False, URL('default', 'tasks'), [])
    (T('Reports'), False, URL('default', 'reports'), [])
    (T('Scripts'), False, URL('default', 'scripts'), [])
]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ---------------------------------------------------------------------------------------------------------------------«~~«