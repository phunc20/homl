01. `pdfunite p380.pdf recurrent-neurons.pdf out.pdf`
  - `pdfunite` is a command from the `poppler` package (which can be installed by `pacman -S poppler` on arch-based distros)
02. [https://stackoverflow.com/questions/2739159/inserting-a-pdf-file-in-latex](https://stackoverflow.com/questions/2739159/inserting-a-pdf-file-in-latex)
  ```tex
  \usepackage{pdfpages}
  % include all pages from a pdf file
  \includepdf[pages=-]{myfile.pdf}
  % include the 1st pages from a pdf file
  \includepdf[pages={1}]{myfile.pdf}
  ```

For more info on extracting and merging pdf files, [please visit here](https://github.com/phunc20/linux/tree/master/troubleshoot/pdf).

