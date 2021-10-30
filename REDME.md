pdfcat
======

Python script that concatenates pdf files in group of two using [pdftk](https://gitlab.com/pdftk-java/pdftk) tool.

## Usage

Split original pdf with pdftk

```bash
$ cd data/input
$ pdftk img20211029_09050388.pdf burst output img20211029_09050388_pg_%04d.pdf
```

Remove base filse from input dir
```bash
$ mv img20211029_09050388.pdf ../
```

Then run script
```bash
$ cd ../../
$ ./pdfcat.py
```

Resulting files will be on `./data/output/` directory:

```bash
$ tree
```

```
│   └── output
│       ├── img20211029_09050388_0001.pdf
│       ├── img20211029_09050388_0002.pdf
│       ├── img20211029_09050388_0003.pdf
│       ├── img20211029_09050388_0004.pdf
│       ├── img20211029_09050388_0005.pdf
│       ├── img20211029_09050388_0006.pdf
│       ├── img20211029_09050388_0007.pdf
│       ├── img20211029_09050388_0008.pdf
│       ├── img20211029_09050388_0009.pdf
│       ├── img20211029_09050388_0010.pdf
│       ├── img20211029_09050388_0011.pdf
│       ├── img20211029_09050388_0012.pdf
│       ├── img20211029_09050388_0013.pdf
│       ├── img20211029_09050388_0014.pdf
│       ├── img20211029_09050388_0015.pdf
│       ├── img20211029_09050388_0016.pdf
│       ├── img20211029_09050388_0017.pdf
│       ├── img20211029_09050388_0018.pdf
│       └── img20211029_09050388_0019.pdf
```