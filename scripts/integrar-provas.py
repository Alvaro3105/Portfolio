#!/usr/bin/env python3
"""Integra duas revisões acadêmicas ao portfólio existente, sem recriar o site."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / 'index.html'
JS = ROOT / 'assets/js/main.js'
README = ROOT / 'README.md'

projects = [
    ('05', 'Python', 'projPythonTitle', 'pythonExamDesc', 'Prova de Python — MVC e Repository', 'Refatoração pós-prova de uma API Flask de gerenciamento de projetos. Separação entre Controller, Service e Repository, preservação do legado e testes de regressão.', 'Python · Flask · SQLAlchemy · MVC · pytest', 'Prova-de-python'),
    ('06', 'TPA', 'projTpaTitle', 'tpaExamDesc', 'Prova de TPA — API de Pedidos', 'Revisão pós-prova de uma API REST em Laravel. CRUD de pedidos com Eloquent, migrations, validação, códigos HTTP e testes automatizados.', 'PHP · Laravel · Eloquent · REST · PHPUnit', 'Prova-final-de-TPA-2etapa'),
]

def replace_once(text, old, new, label):
    count = text.count(old)
    if count != 1:
        raise AssertionError(f'{label}: esperado 1 marcador, encontrado {count}')
    return text.replace(old, new, 1)

html = HTML.read_text(encoding='utf-8')
if 'data-i18n="projPythonTitle"' not in html:
    cards = []
    for num, _, title_key, desc_key, title, desc, tags, repo in projects:
        chips = ''.join(f'<span>{tag.strip()}</span>' for tag in tags.split(' · '))
        cards.append(f'''          <article class="project-card reveal">
            <div class="project-top"><span class="project-number">{num}</span><span class="project-label" data-i18n="examRevision">Revisão pós-prova</span></div>
            <h3 data-i18n="{title_key}">{title}</h3>
            <p data-i18n="{desc_key}">{desc}</p>
            <div class="project-tags">{chips}</div>
            <a class="project-link" href="https://github.com/Alvaro3105/{repo}" target="_blank" rel="noopener" data-i18n="repoLink">Abrir repositório →</a>
          </article>''')
    start = html.index('<section class="section alt" id="projetos">')
    end = html.index('<section class="section" id="formacao">', start)
    section = html[start:end]
    section = replace_once(section, '        </div>\n      </div>\n    </section>', '\n\n'.join(cards) + '\n        </div>\n      </div>\n    </section>', 'fim da grade de projetos')
    html = html[:start] + section + html[end:]
    HTML.write_text(html, encoding='utf-8')

js = JS.read_text(encoding='utf-8')
if 'projPythonTitle:' not in js:
    pt = '''    examRevision: "Revisão pós-prova",
    projPythonTitle: "Prova de Python — MVC e Repository",
    pythonExamDesc: "Refatoração pós-prova de uma API Flask de gerenciamento de projetos. Separação entre Controller, Service e Repository, preservação do legado e testes de regressão.",
    projTpaTitle: "Prova de TPA — API de Pedidos",
    tpaExamDesc: "Revisão pós-prova de uma API REST em Laravel. CRUD de pedidos com Eloquent, migrations, validação, códigos HTTP e testes automatizados.",
'''
    en = '''    examRevision: "Post-exam revision",
    projPythonTitle: "Python Exam — MVC and Repository",
    pythonExamDesc: "Post-exam refactoring of a Flask project-management API. Controller, Service and Repository separation, legacy preservation and regression tests.",
    projTpaTitle: "TPA Exam — Orders REST API",
    tpaExamDesc: "Post-exam revision of a Laravel REST API. Order CRUD with Eloquent, migrations, validation, HTTP status codes and automated tests.",
'''
    js = replace_once(js, '    projHelpdeskTitle: "Helpdesk API",', pt + '    projHelpdeskTitle: "Helpdesk API",', 'traduções PT')
    js = replace_once(js, '    projHelpdeskTitle: "Helpdesk API",', en + '    projHelpdeskTitle: "Helpdesk API",', 'traduções EN') if False else js
    # O mesmo título ocorre nos dois idiomas; o segundo bloco recebe as traduções EN.
    marker = '    projHelpdeskTitle: "Helpdesk API",'
    first = js.index(marker)
    second = js.index(marker, first + len(marker))
    js = js[:second] + en + js[second:]
    JS.write_text(js, encoding='utf-8')

readme = README.read_text(encoding='utf-8')
if 'Prova-de-python' not in readme:
    readme += '''\n## Revisões acadêmicas da 2ª etapa\n\nAs duas provas foram revisadas depois da avaliação, com apoio do ChatGPT. A documentação diferencia a entrega original das alterações posteriores.\n\n- [Python — MVC, Service e Repository](https://github.com/Alvaro3105/Prova-de-python): refatoração de uma API Flask, preservação dos endpoints e testes de regressão.\n- [TPA — API REST de Pedidos](https://github.com/Alvaro3105/Prova-final-de-TPA-2etapa): CRUD Laravel com Eloquent, validação, migrations e testes de integração.\n\nOs repositórios são projetos acadêmicos de estudo, não experiências profissionais nem aplicações publicadas em produção.\n'''
    README.write_text(readme, encoding='utf-8')

# Verificações de integração: dois cards, links corretos e chaves nos dois idiomas.
html = HTML.read_text(encoding='utf-8')
js = JS.read_text(encoding='utf-8')
for _, _, title_key, desc_key, _, _, _, repo in projects:
    assert html.count(f'data-i18n="{title_key}"') == 1
    assert html.count(f'https://github.com/Alvaro3105/{repo}') == 1
    assert js.count(title_key + ':') == 2
    assert js.count(desc_key + ':') == 2
assert html.count('class="project-card reveal"') == 6
assert html.count('data-i18n="examRevision"') == 2
print('Integração validada: 6 projetos, 2 novos cards e traduções PT/EN.')
