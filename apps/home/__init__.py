# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - present Tuan Tran
"""

from flask import Blueprint

blueprint = Blueprint(
    'home_blueprint',
    __name__,
    url_prefix=''
)
