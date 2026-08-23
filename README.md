# Álvaro Pires de Souza — Portfólio

Portfólio pessoal desenvolvido para apresentar minha formação técnica em TI, projetos, competências, certificações e experiências ligadas à tecnologia.

## Sobre o projeto

A proposta do site é reunir em um único lugar as informações mais relevantes do meu perfil profissional, com foco na busca pela primeira oportunidade em Tecnologia da Informação.

O design segue uma identidade visual escura e moderna, com azul e roxo como cores de destaque. O projeto prioriza leitura, responsividade, acessibilidade e uma apresentação profissional, evitando excesso de efeitos visuais.

## Principais recursos

- layout responsivo para desktop, tablet e celular;
- navegação fixa e menu adaptado para dispositivos móveis;
- versão em Português e Inglês com preferência salva no navegador;
- animação de terminal discreta;
- animações de entrada utilizando `IntersectionObserver`;
- suporte a `prefers-reduced-motion`;
- seção de projetos selecionados;
- seção de formação, comunidade, voluntariado e certificações;
- botão "Ver todos" para cursos e certificações, com link direto para o PDF de cada certificado;
- currículo em PDF disponível para download;
- foco visível (`:focus-visible`) para navegação por teclado;
- favicon, canonical e Open Graph/Twitter Card configurados para SEO;
- links diretos para GitHub, LinkedIn e e-mail;
- um toque discreto de aviação (interesse pessoal): uma rota de voo pontilhada com um pequeno avião animado no fundo do Hero, o interesse citado em "Interesses" e um ✈ pequeno no rodapé — tudo decorativo e sutil, sem disputar espaço com o conteúdo técnico.

## Tecnologias

- HTML5
- CSS3
- JavaScript Vanilla
- Git e GitHub
- compatível com publicação no GitHub Pages

Não foi utilizado framework JavaScript porque a complexidade atual do projeto não exige React, Vue ou outra biblioteca. A proposta é manter o portfólio simples, rápido e fácil de manter.

## Estrutura

```text
Portfolio/
├── assets/
│   ├── css/
│   │   └── style.css
│   ├── images/
│   │   ├── perfil.jpg
│   │   ├── google-io.jpg
│   │   ├── minas-summit.jpg
│   │   ├── world-creativity-day.jpg
│   │   └── favicon.svg
│   ├── docs/
│   │   ├── Curriculo_Alvaro_Pires_de_Souza.pdf
│   │   └── certificados/
│   │       ├── cisco-fundamentos-hardware.pdf
│   │       ├── cisco-conscientizacao-digital.pdf
│   │       ├── cisco-introducao-ia-moderna.pdf
│   │       ├── cisco-using-computer-mobile-devices.pdf
│   │       ├── fundacao-bradesco-site-simples.pdf
│   │       ├── coletivo-coca-cola-jovem.pdf
│   │       └── google-io-extended-participacao.pdf
│   └── js/
│       └── main.js
├── index.html
└── README.md
```

## Projetos apresentados

O portfólio destaca atualmente:

- **Helpdesk API** — Python, Flask, SQLAlchemy e API REST;
- **Projeto CRUD Varejo** — C# e Windows Forms;
- **API REST de Questões** — PHP, Laravel e MySQL;
- **CRUD de Veículos** — PHP, PDO e MySQL.

Todos são apresentados de acordo com seu contexto real, incluindo a identificação de projetos acadêmicos.

## Executar localmente

Clone o repositório:

```bash
git clone https://github.com/Alvaro3105/Portfolio.git
cd Portfolio
```

Depois abra `index.html` no navegador ou inicie um servidor local:

```bash
python -m http.server 8000
```

Acesse:

```text
http://localhost:8000
```

## Contato

**Álvaro Pires de Souza**

- GitHub: [Alvaro3105](https://github.com/Alvaro3105)
- LinkedIn: [alvaro-pires-de-souza](https://www.linkedin.com/in/alvaro-pires-de-souza/)


## Fotos desta versão

- `perfil.jpg` — foto principal no Hero;
- `google-io.jpg` — Google I/O Extended Belo Horizonte;
- `minas-summit.jpg` — Minas Summit;
- `world-creativity-day.jpg` — registro de voluntariado no World Creativity Day.

Esta pasta pode ser aberta diretamente no VS Code. Para visualizar com caminhos locais funcionando corretamente, use a extensão Live Server ou rode `python -m http.server 8000` na raiz do projeto.
