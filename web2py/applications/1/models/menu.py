# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

page = request.function

response.menu += [
    (T('Página Inicial (Listar Carros)'), page == 'listar_carros', URL('default', 'listar_carros'),[
        (T('Adicionar Carro'), page == 'adicionar', URL('default', 'adicionar'))
        ])
    ]

# ----------------------------------------------------------------------------------------------------------------------
# provide shortcuts for development. you can remove everything below in production
# ----------------------------------------------------------------------------------------------------------------------

plataforma = session.plataforma or ''

is_pesquisa_active = plataforma in ['olx', 'standvirtual', 'oparking', 'custojusto']

if not configuration.get('app.production'):
    _app = request.application
    response.menu += [
        (T('Pesquisa'), is_pesquisa_active, '#', [
            (T('OLX'), plataforma == 'olx', URL('default', 'pesquisa', vars={'plataforma': 'olx'})),
            (T('Standvirtual'), plataforma == 'standvirtual', URL('default', 'pesquisa', vars={'plataforma': 'standvirtual'})),
            (T('oParking'), plataforma == 'oparking', URL('default', 'pesquisa', vars={'plataforma': 'oparking'})),
            (T('CustoJusto'), plataforma == 'custojusto', URL('default', 'pesquisa', vars={'plataforma': 'custojusto'}))
        ])
    ]


