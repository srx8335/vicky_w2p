# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.main_menu = [
    (XML('<span class="material-icons">dashboard</span><span> Home</span>'), False, URL('default', 'home'), []),
    (T('Finances'), False, URL('default', 'finances'), []),
    (T('Pipeline'), False, URL('default', 'pipeline'), []),
    (T('Clients'), False, URL('default', 'clients'), []),
    (T('Tasks'), False, URL('default', 'tasks'), []),
    (T('Reports'), False, URL('default', 'reports'), []),
    (T('Scripts'), False, URL('default', 'scripts'), []),
]

response.acc_menu = [
    (T('Profile'), False, URL('default', 'profile'), []),
    (T('Settings'), False, URL('default', 'settings'), []),
    (T('Logout'), False, URL('default', 'logout'), []),
]

response.info_menu =[
    (T('About Us'), False, URL('default', 'logout'), []),
]
# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ---------------------------------------------------------------------------------------------------------------------«~~«