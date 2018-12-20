# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import recommonmark
from recommonmark.parser import CommonMarkParser
from recommonmark.transform import AutoStructify

# recommonmark の拡張利用
github_doc_root = 'https://github.com/rtfd/recommonmark/tree/master/doc/'
def setup(app):
    app.add_config_value('recommonmark_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)

# -- Project information -----------------------------------------------------

project = 'C95'
copyright = '2018, gen'
author = 'ゲン'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# コードブロックモノクロ
pygments_style = 'bw'

# 図表番号

number_figures = False

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
]
# Add any paths that contain templates here, relative to this directory.
templates_path = ['Ytemplates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = ['.rst', '.md']
# source_suffix = '.rst'

source_parsers = {
    '.md' : 'recommonmark.parser.CommonMarkParser'
}

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ja'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["build"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = None


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['Ystatic']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
# htmlhelp_basename = 'c95doc'


# -- Options for LaTeX output ------------------------------------------------
#latex_engine = 'platex'
latex_engine = 'lualatex'

latex_elements = {
    'pointsize': '10pt',
    'papersize': 'b5j',
    'extraclassoptions': 'openany,twoside',
    'babel': r'''
\usepackage[japanese]{babel}
''',
    'tableofcontents': r'''
%normalで目次ページを出力しつつSphinxスタイルをやめさせる
\tableofcontents
    ''',
    'preamble': r'''
%フォント
%TexLive側コマンドで制御kanji-config-updmap-user [kozka|kozuka-pr6n|ipaex|yu-win10|status|他]
%luatexで
\usepackage[kozuka-pr6n]{luatexja-preset}

%pdf/x使うための設定
\usepackage[x-1a1]{pdfx}

%レイアウト
\renewcommand{\plainifnotempty}{\thispagestyle{plain}}
\setlength{\textheight}{\paperheight}
\setlength{\topmargin}{-5.4truemm}
\addtolength{\topmargin}{-\headheight}
\addtolength{\topmargin}{-\headsep}
\addtolength{\textheight}{-40truemm}
\setlength{\textwidth}{\paperwidth}
\setlength{\oddsidemargin}{-5.4truemm}
\setlength{\evensidemargin}{-5.4truemm}
\addtolength{\textwidth}{-40truemm}

% ハイパーリンクモノクロ
\hypersetup{colorlinks=false}

% 字下げ
%\setlength\parindent{1zw}

% パラグラフ間空白
%\setlength{\parskip}{0pt}

% タイトル装飾
\usepackage{titlesec}
\usepackage{picture}

% chapter
\titleformat{\chapter}[block]
{}{}{0pt}{
  \fontsize{30pt}{30pt}\selectfont\filleft
}[
  \hrule \Large{\filleft 第 \thechapter 章}
]

% section
\titleformat{\section}[block]
{}{}{0pt}
{
  \hspace{0pt}
  \normalfont \Large\bfseries{ \thesection }
  \hspace{-4pt}
}

% subsection
\titleformat{\subsection}[block]
{}{}{0pt}
{
  \hspace{0pt}
  \normalfont \large\bfseries{ \thesubsection }
  \hspace{-4pt}
}

''',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'c95.tex', '泥輪事情',
    'ゲン', 'manual'),
]

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False
#latex_use_parts = True

# -- Options for Epub output -------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = '泥輪事情'

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#
# epub_identifier = ''

# A unique identification for the text.
#
# epub_uid = ''

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']


# -- Extension configuration -------------------------------------------------

# LaTeX の docclass 設定

#lualatex用(デフォルトはjsbookになってる)
latex_docclass = {'manual': 'ltjsbook'}