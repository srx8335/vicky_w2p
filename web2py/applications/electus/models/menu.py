# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------
response.main_menu = [
    (XML('<span class="material-icons">dashboard</span><span> Home</span>'), False, URL('default', 'home'), []),
    (XML('<span class="material-icons">payments</span><span> Finances</span>'), False, URL('default', 'Finances'), []),
    (XML('<span class="material-icons">timeline</span><span> Pipeline</span>'), False, URL('default', 'pipeline'), []),
    (XML('<span class="material-icons">groups</span><span> Clients</span>'), False, URL('default', 'clients'), []),
    (XML('<span class="material-icons">task</span><span> Tasks</span>'), False, URL('default', 'tasks'), []),
    (XML('<span class="material-icons">bar_chart</span><span> Reports</span>'), False, URL('default', 'reports'), []),
    (XML('<span class="material-icons">code</span><span> Scripts</span>'), False, URL('default', 'scripts'), []),
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