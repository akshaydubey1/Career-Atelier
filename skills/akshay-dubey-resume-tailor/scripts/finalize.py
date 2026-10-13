#!/usr/bin/env python3
"""Resume Tailor by Akshay Dubey (MIT). Finalize a .docx: set owner-only metadata, convert to PDF, clean the PDF.

Usage: python finalize.py <file.docx> "<Full Name>" <resume|cover> [--keep-docx]
Writes <file>.pdf next to the .docx. Needs: python-docx, pikepdf, and either LibreOffice (soffice) or docx2pdf (Word).
"""
import shutil, subprocess, sys
from pathlib import Path


def need(mod, pkg):
    try:
        return __import__(mod)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", pkg])
        return __import__(mod)


def clean_docx(path, name, title):
    docx = need("docx", "python-docx")
    d = docx.Document(path)
    p = d.core_properties
    p.author = name
    p.last_modified_by = name
    p.title = title
    p.comments = p.keywords = p.subject = p.category = ""
    p.revision = 1
    d.save(path)


def to_pdf(path):
    out = path.with_suffix(".pdf")
    soffice = shutil.which("soffice") or shutil.which("libreoffice") or (
        "/Applications/LibreOffice.app/Contents/MacOS/soffice"
        if Path("/Applications/LibreOffice.app").exists() else None)
    if soffice:
        subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", str(path.parent), str(path)],
                       check=True, capture_output=True)
    else:
        need("docx2pdf", "docx2pdf").convert(str(path), str(out))
    if not out.exists():
        sys.exit("PDF conversion failed: install LibreOffice or Microsoft Word.")
    return out


def clean_pdf(path, name, title):
    pikepdf = need("pikepdf", "pikepdf")
    with pikepdf.open(path, allow_overwriting_input=True) as pdf:
        if "/Metadata" in pdf.Root:
            del pdf.Root.Metadata
        info = pdf.docinfo
        for k in list(info.keys()):
            del info[k]
        info["/Author"] = name
        info["/Creator"] = name
        info["/Title"] = title
        from xml.sax.saxutils import escape
        n, t = escape(name), escape(title)
        xmp = ('<?xpacket begin="﻿" id="W5M0MpCehiHzreSzNTczkc9d"?>'
               '<x:xmpmeta xmlns:x="adobe:ns:meta/"><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">'
               '<rdf:Description rdf:about="" xmlns:dc="http://purl.org/dc/elements/1.1/">'
               f'<dc:creator><rdf:Seq><rdf:li>{n}</rdf:li></rdf:Seq></dc:creator>'
               f'<dc:title><rdf:Alt><rdf:li xml:lang="x-default">{t}</rdf:li></rdf:Alt></dc:title>'
               '</rdf:Description></rdf:RDF></x:xmpmeta><?xpacket end="w"?>')
        pdf.Root.Metadata = pdf.make_stream(xmp.encode("utf-8"), Type=pikepdf.Name.Metadata, Subtype=pikepdf.Name.XML)
        pdf.save(path)


def main():
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    path, name, kind = Path(sys.argv[1]).expanduser(), sys.argv[2], sys.argv[3].lower()
    title = f"{name} — {'Cover Letter' if kind.startswith('c') else 'Resume'}"
    clean_docx(path, name, title)
    pdf = to_pdf(path)
    clean_pdf(pdf, name, title)
    print(pdf)


if __name__ == "__main__":
    main()
