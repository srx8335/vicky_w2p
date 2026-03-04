# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------
# This is a sample controller
# this file is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

import requests
from gluon import *
from gluon import current


# ---- example index page ----
def index():
    redirect(URL('default', 'user', args='login'))

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
        redirect(URL('default', 'listar_carros'))
    
    return dict(form=auth())

# ---- action to server uploaded static content (required) ---
@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


# ---- form adicionar carro ---- 
@auth.requires_login()
def adicionar():
    response.files.append(URL('static', 'css/btn.css'))
    
    form = SQLFORM(db.carro).process()
    
    submit_btn = form.element('input', _type='submit')
    if submit_btn:
        submit_btn['_value'] = 'Adicionar Carro'
        submit_btn['_class'] = 'btnAdd' 
    
    botao_voltar = A('<- Voltar', _href=URL('default', 'listar_carros'), _class='btnVoltar')
    form.append(botao_voltar)# adicionar botão no fim

    if form.accepted:
        carro = form.vars

        requests.post("https://ntfy.sh/app_carros", headers={"Priority": "5"},
        data=f"🚗 Carro Adicionado {carro.Marca} {carro.Modelo} ({carro.Ano}) ".encode(encoding='utf-8'))

        response.flash = "Carro adicionado com sucesso!"
        redirect(URL('listar_carros'))  # redireciona após submissão
    elif form.errors:
        response.flash = "Erro ao adicionar Carro"
    
    return dict(form=form)

# ---- listar carros ----
@auth.requires_login()
def listar_carros():
    response.files.append(URL('static', 'css/listar_carros.css'))

    carros = db(db.carro).select()
    return dict(carros=carros)

# ---- editar carros ----
@auth.requires_login()
def editar_carro():
    response.files.append(URL('static', 'css/btn.css'))
    carro_id = request.args(0) or redirect(URL('listar_carros'))
    
    form = SQLFORM(db.carro, carro_id, showid=False).process()
    form.element('input', _type='submit')['_class'] = 'btnAdd'
    form.element('input', _type='submit')['_value'] = 'Guardar Alterações'

    botao_voltar = A('<- Voltar', _href=URL('default', 'listar_carros'), _class='btnVoltar')
    form.append(botao_voltar)      # adicionar botão no fim
    
    if form.accepted:
        carro = form.vars

        requests.post("https://ntfy.sh/app_carros", headers={"Priority": "5"},
        data=f"🚗 Carro Editado {carro.Marca} {carro.Modelo} ({carro.Ano}) ".encode(encoding='utf-8'))

        response.flash = "Carro editado com sucesso!"
        redirect(URL('listar_carros'))  # <- aqui está tudo certo
    elif form.errors:
        response.flash = "Erro ao editar Carro"

    return dict(form=form)

# ---- apagar carros ----
@auth.requires_login()
def apagar_carro():
    carro_id = request.args(0)

    carro = db.carro(carro_id)

    if carro_id:
        deleted = db(db.carro.id == carro_id).delete()
        if deleted == 1:
            requests.post("https://ntfy.sh/app_carros", headers={"Priority": "5"},
            data=f"🚗 Carro Apagado {carro.Marca} {carro.Modelo} ({carro.Ano}) ".encode(encoding='utf-8'))
        redirect(URL('listar_carros'))
    else:
        redirect(URL('listar_carros'))
        response.flash = "Não foi possivel apagar o carro"
 

def cal():
    return dict()
def eventos():
    # eventos = db(db.evento).select()
    # lista = [
    #     dict(
    #         title=e.titulo,
    #         start=e.inicio.isoformat(),
    #         end=e.fim.isoformat()
    #     ) for e in eventos
    # ]
    lista = [
        dict(
            title='titulo',
            start='2025-05-01T00:00:00',
        )
    ]
    return response.json(lista)





# redirect pag olx carro selected
@auth.requires_login()
def pesquisa():
    response.files.append(URL('static', 'css/listar_carros.css'))
    # Se recebeu nova plataforma, guarda e redireciona
    if request.vars.plataforma:
        session.plataforma = request.vars.plataforma
        redirect(URL('default', 'pesquisa'))

    # Se não há nenhuma plataforma na sessão, define uma por defeito
    if not session.plataforma:
        session.plataforma = 'olx'

    carros = db(db.carro).select()

    base_links = {
        "olx": "https://www.olx.pt/ads/q-",
        "standvirtual": "https://www.standvirtual.com/carros/q-",
        "oparking": "https://www.oparking.pt/#!/carros-em-segunda-mao/",
        "custojusto": "https://www.custojusto.pt/portugal/q/",
        "adicionar": "adicionar",
        "listar_carros": "listar_carros",
    }

    link_plataforma = base_links.get(session.plataforma, "#")

    if session.plataforma:
        session.plataforma = ''

    return dict(carros=carros, link_plataforma=link_plataforma)
