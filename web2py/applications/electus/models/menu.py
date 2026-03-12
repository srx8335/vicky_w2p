# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------
response.menu = [

    (XML('<li class="nav-header"></li>'), False, None, []),

    (XML('<span class="material-icons">home</span><span> Home</span>'), request.function=='home', URL('default','home'), []),
    (XML('<span class="material-icons">payments</span><span> Finances</span>'), False, URL('default','finances'), []),
    (XML('<span class="material-icons">timeline</span><span> Pipeline</span>'), False, URL('default','pipeline'), []),
    (XML('<span class="material-icons">groups</span><span> Clients</span>'), request.function=='clients', URL('default','clients'), []),
    (XML('<span class="material-icons">task</span><span> Tasks</span>'), False, URL('default','tasks'), []),
    (XML('<span class="material-icons">bar_chart</span><span> Reports</span>'), False, URL('default','reports'), []),
    (XML('<span class="material-icons">code</span><span> Scripts</span>'), False, URL('default','scripts'), []),

    (XML('<li class="nav-header">  </li>'), False, None, []),

    (XML('<span class="material-icons">person</span><span> Profile</span>'), False, URL('default','profile'), []),
    (XML('<span class="material-icons">settings</span><span> Settings</span>'), False, URL('default','settings'), []),
    (XML('<span class="material-icons">logout</span><span> Logout</span>'), False, URL('default','logout'), []),

    (XML('<li class="nav-header sidebar-bottom">  </li>'), False, None, []),

    (XML('<span class="material-icons">info</span><span> About Us</span>'), False, URL('default','about'), []),
]
# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ---------------------------------------------------------------------------------------------------------------------«~~«