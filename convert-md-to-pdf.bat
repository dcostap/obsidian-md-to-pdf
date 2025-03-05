@echo off
setlocal

if "%~x1" neq ".md" (
    echo ERROR: Input file required and it must be a .md file.
    exit /b 1
)

set "inputfile=%~1"
set "filename=%~n1"

echo Converting to PDF...
mkdir out 2>nul
pandoc  "%inputfile%" -o "out/%filename%.pdf" --pdf-engine=pdflatex --toc --number-sections --from=markdown+lists_without_preceding_blankline --filter pandoc-crossref --include-in-header=latex-header.tex || exit /b 1

start "" "out\%filename%.pdf"
