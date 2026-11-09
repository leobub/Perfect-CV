#!/usr/bin/env python3
"""CV Tailor renderer: HTML -> one-page A4 PDF, with verification and preview.

Usage:
  python render.py embed <image_path>               Print a data: URI for a photo
  python render.py build <input.html> <output.pdf>  Render + verify 1 page + preview PNG

Dependencies: weasyprint (required), pdfplumber + pdf2image (optional, for checks).
"""
import sys
import base64
import mimetypes
import pathlib


def embed(img_path: str) -> None:
    p = pathlib.Path(img_path)
    mime = mimetypes.guess_type(p.name)[0] or "image/jpeg"
    data = base64.b64encode(p.read_bytes()).decode()
    print(f"data:{mime};base64,{data}")


def build(in_html: str, out_pdf: str) -> None:
    import weasyprint
    weasyprint.HTML(in_html).write_pdf(out_pdf)

    pages = None
    try:
        import pdfplumber
        with pdfplumber.open(out_pdf) as pdf:
            pages = len(pdf.pages)
    except Exception as e:
        print(f"[warn] page check skipped: {e}", file=sys.stderr)

    if pages is not None:
        print(f"{out_pdf}: {pages} page(s)")
        if pages != 1:
            print("[warn] expected 1 page — trim content until it fits.", file=sys.stderr)

    try:
        from pdf2image import convert_from_path
        png = str(pathlib.Path(out_pdf).with_suffix(".preview.png"))
        convert_from_path(out_pdf, dpi=90)[0].save(png)
        print(f"preview: {png}")
    except Exception as e:
        print(f"[warn] preview skipped: {e}", file=sys.stderr)


def main() -> None:
    args = sys.argv[1:]
    if len(args) == 2 and args[0] == "embed":
        embed(args[1])
    elif len(args) == 3 and args[0] == "build":
        build(args[1], args[2])
    else:
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
