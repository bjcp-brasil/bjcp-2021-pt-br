#!/usr/bin/env node
// Converte os .tex (fonte original) em Markdown para o Docusaurus consumir.
// Roda sempre a partir do .tex — nunca edite os arquivos gerados em
// website/docs/, eles são recriados do zero a cada execução (ver
// website/README.md).
//
// Diferente do piloto de sidra, aqui a ordem e a estrutura são lidas
// automaticamente a partir de main.tex (parseando os \input{...} em
// ordem) e do index.tex de cada categoria — sem lista manual, já que
// esse guia tem 34 categorias + apêndices.
import {execFileSync} from 'node:child_process';
import {mkdirSync, rmSync, writeFileSync, readFileSync, copyFileSync} from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '../..');
const docsDir = path.join(__dirname, '../docs');
const tmpTexPath = path.join(repoRoot, '.generate-docs-tmp.tex');

function sh(cmd, args) {
  return execFileSync(cmd, args, {encoding: 'utf8'});
}

function pandocLatexToMd(absTexPath) {
  const rel = path.relative(repoRoot, absTexPath);
  // O entrypoint da imagem pandoc/core só repassa pro `pandoc` quando o
  // primeiro argumento começa com "-"; senão tenta dar exec no arquivo.
  // Por isso as flags vêm antes do nome do arquivo aqui.
  const out = sh('docker', [
    'run',
    '--rm',
    '-v',
    `${repoRoot}:/data`,
    '-w',
    '/data',
    'pandoc/core:2.9',
    '-f',
    'latex',
    '-t',
    'gfm',
    rel,
  ]);
  // Artefato do pandoc: número de página do LaTeX vazando como texto solto
  // (só aparece em arquivos com \clearpage, ex.: capa e apêndices).
  return out.replace(/<p><span>\d+<\/span><\/p>\n?/g, '');
}

// Pandoc resolve \input{} aninhado sozinho (testado), então pra converter
// uma string modificada (ex.: um arquivo sem os \input dos estilos-filho)
// precisamos gravar num arquivo temporário dentro do repo, já que o
// Docker monta repoRoot inteiro.
function pandocLatexStringToMd(texContent) {
  writeFileSync(tmpTexPath, texContent);
  try {
    return pandocLatexToMd(tmpTexPath);
  } finally {
    rmSync(tmpTexPath, {force: true});
  }
}

function extractTitle(absTexPath) {
  const content = readFileSync(absTexPath, 'utf8');
  const match = content.match(/\\(?:sub)?section\*\{([^}]*)\}/);
  if (!match) {
    throw new Error(`Não encontrei \\section*{} ou \\subsection*{} em ${absTexPath}`);
  }
  return match[1].replace(/\\break/g, ' ').trim();
}

function extractInputs(absTexPath) {
  const content = readFileSync(absTexPath, 'utf8');
  const re = /\\input\{([^}]+)\}/g;
  const out = [];
  let m;
  while ((m = re.exec(content))) out.push(m[1].trim());
  return out;
}

function yamlEscape(value) {
  if (typeof value !== 'string') return String(value);
  return `"${value.replace(/\\/g, '\\\\').replace(/"/g, '\\"')}"`;
}

function writeMdWithFrontmatter(targetPath, title, body, extraFrontmatter = {}) {
  // O título já vem do frontmatter (Docusaurus renderiza como <h1>), então
  // tira o heading duplicado que o pandoc gera a partir do \section*/\subsection*.
  const withoutHeading = body.replace(/^#{1,2} .*\n+/, '');
  const lines = [`title: ${yamlEscape(title)}`];
  for (const [key, value] of Object.entries(extraFrontmatter)) {
    lines.push(`${key}: ${yamlEscape(value)}`);
  }
  const frontmatter = `---\n${lines.join('\n')}\n---\n\n`;
  writeFileSync(targetPath, frontmatter + withoutHeading);
}

console.log('Limpando website/docs/ ...');
rmSync(docsDir, {recursive: true, force: true});
mkdirSync(docsDir, {recursive: true});

// frontpage.tex não segue o padrão \section*/\subsection* dos demais
// arquivos (é a página de capa: título, logo, créditos de tradução,
// versão, data, contato) — por isso é tratada à parte, e vira a home do
// site ('/').
console.log('[capa] frontpage.tex -> capa.md');
const frontpageMd = pandocLatexToMd(path.join(repoRoot, 'frontpage.tex'))
  // artefato do pandoc pra referência de figura do LaTeX, sem equivalente em markdown
  .replace(/<span id="fig:bjcp-logo"[^>]*>.*?<\/span>\n?/, '')
  // As 3 linhas de título da capa (hoje só bold, sem hierarquia) viram
  // headings de verdade. Tag HTML literal (não `#`/`##` do markdown) de
  // propósito: assim não entra no TOC lateral autogerado do Docusaurus.
  .replace(/<span>\*\*BEER JUDGE CERTIFICATION PROGRAM\*\*<\/span>\s*/, '<h1>BEER JUDGE CERTIFICATION PROGRAM</h1>\n\n')
  .replace(/<span>\*\*Guia de Estilos 2021\*\*\s*<\/span>\s*/, '<h2>Guia de Estilos 2021</h2>\n\n')
  .replace(/<span>\*\*Guia de Estilos de Cerveja\*\*<\/span>\s*/, '<h3>Guia de Estilos de Cerveja</h3>\n\n')
  // O resto dos <span> sem classe/estilo é o que sobra do
  // \fontsize{}{}\selectfont do LaTeX (pandoc não tem pra onde mapear o
  // tamanho de fonte). Como <span> é HTML inline, o MDX não separa em
  // parágrafos as linhas em branco entre eles — tudo flui grudado em vez
  // de virar blocos distintos. Como não carregam nenhum estilo de
  // verdade, removemos e deixamos markdown puro, que respeita linha em
  // branco = parágrafo novo.
  .replace(/<\/?span[^>]*>/g, '')
  // a imagem é referenciada como assets/bjcp-logo.png (relativo à raiz do
  // repo); copiamos o arquivo pra perto do .md gerado e reescrevemos o
  // caminho, pra o bundler do Docusaurus resolver o asset corretamente
  // (inclusive respeitando o baseUrl) em vez de um link absoluto quebrado.
  .replace('assets/bjcp-logo.png', './bjcp-logo.png');
copyFileSync(path.join(repoRoot, 'assets/bjcp-logo.png'), path.join(docsDir, 'bjcp-logo.png'));
writeMdWithFrontmatter(
  path.join(docsDir, 'capa.md'),
  'BJCP - Diretrizes de Estilo 2021',
  frontpageMd,
  {
    slug: '/',
    sidebar_position: 0,
    sidebar_label: 'Capa',
    // O próprio conteúdo da capa já traz o título em destaque (replica o
    // layout do frontpage.tex); um <h1> automático em cima ficaria redundante.
    hide_title: true,
  },
);

function generateCategory(dir, position) {
  const srcDir = path.join(repoRoot, dir);
  const targetDir = path.join(docsDir, dir);
  mkdirSync(targetDir, {recursive: true});

  const headerPath = path.join(srcDir, 'header.tex');
  const label = extractTitle(headerPath);

  writeFileSync(
    path.join(targetDir, '_category_.json'),
    JSON.stringify({label, position}, null, 2) + '\n',
  );

  console.log(`[categoria] ${dir} ("${label}")`);

  const headerMd = pandocLatexToMd(headerPath);
  writeMdWithFrontmatter(path.join(targetDir, 'index.md'), label, headerMd);

  const contentFiles = extractInputs(path.join(srcDir, 'index.tex'))
    .map((p) => path.basename(p))
    .filter((f) => f !== 'header.tex');

  contentFiles.forEach((file, i) => {
    const absPath = path.join(srcDir, file);
    const slug = file.replace(/\.tex$/, '');
    const title = extractTitle(absPath);
    const md = pandocLatexToMd(absPath);
    // Ordem alfabética do nome do arquivo nem sempre bate com a ordem real
    // do guia (ex.: 21b-specialty-ipa.tex vem antes de
    // 21b-specialty-ipa-belgian-ipa.tex no index.tex, mas "-" < "." faria
    // o alfabético inverter). sidebar_position explícito, na ordem em que
    // aparece no \input do index.tex, evita esse tipo de bug.
    writeMdWithFrontmatter(path.join(targetDir, `${slug}.md`), title, md, {
      sidebar_position: i + 1,
    });
    console.log(`    ${file} -> ${dir}/${slug}.md ("${title}")`);
  });
}

// Arquivo "solto" referenciado direto em main.tex (não é uma categoria com
// header.tex/index.tex) — hoje só os apêndices. Se o arquivo tiver \input
// aninhado pra outros .tex (ex.: appendix/b-appendix.tex, que inclui 5
// estilos regionais), tratamos como pseudo-categoria: cada \input aninhado
// vira página própria, igual um estilo normal. Sem \input aninhado
// (ex.: appendix/a-appendix.tex), vira uma página única.
function generateStandalone(inputPath, position) {
  const absPath = path.join(repoRoot, inputPath);
  const slug = path.basename(inputPath, '.tex');
  const title = extractTitle(absPath);
  const nestedInputs = extractInputs(absPath);

  if (nestedInputs.length === 0) {
    console.log(`[standalone] ${inputPath} -> ${slug}.md ("${title}")`);
    const md = pandocLatexToMd(absPath);
    writeMdWithFrontmatter(path.join(docsDir, `${slug}.md`), title, md, {
      sidebar_position: position,
    });
    return;
  }

  console.log(`[pseudo-categoria] ${inputPath} -> ${slug}/ ("${title}", ${nestedInputs.length} sub-páginas)`);
  const targetDir = path.join(docsDir, slug);
  mkdirSync(targetDir, {recursive: true});
  writeFileSync(
    path.join(targetDir, '_category_.json'),
    JSON.stringify({label: title, position}, null, 2) + '\n',
  );

  // Conteúdo antes de \begin{multicols*} é a introdução (mesmo padrão dos
  // header.tex de categoria); o que vem depois são só os \input das
  // sub-páginas, já convertidas individualmente abaixo.
  const rawContent = readFileSync(absPath, 'utf8');
  const [introTex] = rawContent.split('\\begin{multicols*}');
  const introMd = pandocLatexStringToMd(introTex);
  writeMdWithFrontmatter(path.join(targetDir, 'index.md'), title, introMd);

  nestedInputs.forEach((nestedRelPath, i) => {
    const nestedAbsPath = path.join(repoRoot, nestedRelPath);
    const nestedSlug = path.basename(nestedRelPath, '.tex');
    const nestedTitle = extractTitle(nestedAbsPath);
    const nestedMd = pandocLatexToMd(nestedAbsPath);
    writeMdWithFrontmatter(path.join(targetDir, `${nestedSlug}.md`), nestedTitle, nestedMd, {
      sidebar_position: i + 1,
    });
    console.log(`    ${nestedRelPath} -> ${slug}/${nestedSlug}.md ("${nestedTitle}")`);
  });
}

const mainInputs = extractInputs(path.join(repoRoot, 'main.tex')).filter(
  (p) => p !== 'frontpage.tex',
);

let position = 1;
mainInputs.forEach((inputPath) => {
  if (inputPath.endsWith('/index.tex')) {
    generateCategory(inputPath.slice(0, -'/index.tex'.length), position++);
  } else {
    generateStandalone(inputPath, position++);
  }
});

console.log('Pronto. website/docs/ gerado a partir dos .tex.');
