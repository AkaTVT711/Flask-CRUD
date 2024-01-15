# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - present Tuan Tran
"""

from flask import Blueprint

blueprint = Blueprint(
    'products_blueprint',
    __name__,
    url_prefix=''
)
