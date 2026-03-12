# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

# ---- example index page ----
def index():
    redirect(URL('default', 'home'))

# ---- API (example) -----
@auth.requires_login()
def api_get_user_email():
    if not request.env.request_method == 'GET': raise HTTP(403)
    return response.json({'status':'success', 'email':auth.user.email})

# ---- Smart Grid (example) -----
@auth.requires_membership('admin') # can only be accessed by members of admin groupd
def grid():
    response.view = 'generic.html' # use a generic view
    tablename = request.args(0)
    if not tablename in db.tables: raise HTTP(403)
    grid = SQLFORM.smartgrid(db[tablename], args=[tablename], deletable=False, editable=False)
    return dict(grid=grid)

# ---- Embedded wiki (example) ----
def wiki():
    auth.wikimenu() # add the wiki to the menu
    return auth.wiki() 

# ---- Action for login/register/etc (required for auth) -----
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    

    #se o user estiver conseguir logar, redireciona para a página de listar#
    if auth.is_logged_in():
        redirect(URL('default', 'home'))

    return dict(form=auth())
# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)





def home():
    test='home'
    response.page = 'home'
    return dict(test=test)

def finances():
    test='finances'
    response.page = 'finances'
    return dict(test=test)

def pipeline():
    test='pipeline'
    response.page = 'pipeline'
    return dict(test=test)

def clients():
    test='clients'
    response.page = 'clients'
    return dict(test=test)

def reports():
    test='reports'
    response.page = 'reports'
    return dict(test=test)

def scripts():
    test='scripts'
    response.page = 'scripts'
    return dict(test=test)





# secound section of sidebar
def profile():
    test='profile'
    response.page = 'profile'
    return dict(test=test)

def settings():
    test='settings'
    response.page = 'settings'
    return dict(test=test)

def logout():
    test='logout'
    response.page = 'logout'
    return dict(test=test)





# 3rd section of sidebar
def about():
    test='about'
    response.page = 'about'
    return dict(test=test)