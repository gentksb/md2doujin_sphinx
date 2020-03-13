# md2doujin

MarkdownとちょっとのRST記法でB5の同人誌PDFを生成する

関連記事：[Markdownでオフセット同人誌を刷るまで](https://gensobunya-tech.hatenablog.com/entry/2018/12/20/000000)

## 構成

- Python 3.7.x
- Sphinx
- recommonmark
- TeXLive 2018

## Sphinxビルド

```bash
make clean
make latexpdf
```

```powershell
.\make clean
.\make latexpdf
```

### .texファイルをゴニョって出力し直す

1. texファイルをmakeしていろいろやる

```powershell
.\make clean
.\make latex
```

1. ./build/latexで下記コマンドを叩く

```powershell
platex   -kanji=utf8  -recorder  "c95.tex"
dvipdfmx  -o "c95.pdf" "c95.dvi"
```

ファイル名はよろしく変更すること

### lualatexでpdf/x-a1準拠させる(原稿によってはレイアウトが崩れる)

1. conf.pyをいじる(conf_lua.py)

2. 以下のコマンド

```powershell
.\make clean
.\make latex
.\make latex
```

```powershell
lualatex c95.tex
```

### 出てくるもの

目次ページのノンブルが3で始まる「左綴じ」「横書き」「1段組」モノクロPDF原稿（フォント埋め込み済み）  
あとは出版社次第だけどラック出版はページごと分割なので下記分割出力の手順が必要

### ページごと出力する

```Google SpreadSheet
="dvipdfmx -c -V 3 -s "&ROW(A1)+1&"-"&ROW(A1)+1&" -o './indv/"&TEXT(ROW(A1)+2,"00")&".pdf' 'c95.dvi'"
```

```Powershell
mkdir .\build\latex\indv\
cd .\build\latex\
dvipdfmx -c -V 3 -s 2-2 -o './indv/03.pdf' 'c95.dvi'
dvipdfmx -c -V 3 -s 3-3 -o './indv/04.pdf' 'c95.dvi'
dvipdfmx -c -V 3 -s 4-4 -o './indv/05.pdf' 'c95.dvi'
dvipdfmx -c -V 3 -s 5-5 -o './indv/06.pdf' 'c95.dvi'
dvipdfmx -c -V 3 -s 6-6 -o './indv/07.pdf' 'c95.dvi'
dvipdfmx -c -V 3 -s 7-7 -o './indv/08.pdf' 'c95.dvi'

#以下略
```

ファイル名はよろしく変更すること
