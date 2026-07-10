// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Guia de Estilos de Cerveja BJCP - 2021',
  tagline: 'Diretrizes de Estilo de Cerveja do BJCP - Tradução PT-BR',
  favicon: 'img/bjcp-logo.png',

  future: {
    v4: true,
  },

  url: 'https://bjcp-brasil.github.io',
  baseUrl: '/bjcp-2021-pt-br/',

  organizationName: 'bjcp-brasil',
  projectName: 'bjcp-2021-pt-br',

  onBrokenLinks: 'throw',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  i18n: {
    defaultLocale: 'pt-BR',
    locales: ['pt-BR'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.js',
          editUrl:
            'https://github.com/bjcp-brasil/bjcp-2021-pt-br/tree/main/',
          // Por padrão o Docusaurus tira prefixo numérico (ex.: "21-ipa"
          // -> "/ipa/") pra usar em ordenação. Aqui os números são a
          // numeração oficial de categoria do BJCP (ex.: "Categoria 21"),
          // então queremos eles na URL — e a ordem já vem explícita via
          // `position` no _category_.json (gerado a partir do main.tex),
          // não precisamos do parser de prefixo pra isso.
          numberPrefixParser: false,
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themes: [
    [
      // Busca local, indexada no build — sem depender de serviço externo
      // (Algolia exige cadastro/aprovação e uma API key de terceiro).
      '@easyops-cn/docusaurus-search-local',
      /** @type {import('@easyops-cn/docusaurus-search-local').PluginOptions} */
      ({
        hashed: true,
        language: ['pt'],
        indexDocs: true,
        indexBlog: false,
        docsRouteBasePath: '/',
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: 'img/bjcp-logo.png',
      docs: {
        sidebar: {
          hideable: true,
        },
      },
      colorMode: {
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: 'Guia de Estilos de Cerveja BJCP - 2021',
        logo: {
          alt: 'Logo do BJCP',
          src: 'img/bjcp-logo.png',
        },
        items: [
          {
            href: 'https://github.com/bjcp-brasil/bjcp-2021-pt-br',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [],
        copyright: `BJCP Diretrizes de Estilo de Cerveja - Edição 2021 - Tradução PT-BR mantida por BJCP Brasil`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
