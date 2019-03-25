import re
from pdfminer.pdfinterp import PDFResourceManager,process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdffile):
    with open(pdffile,'rb') as fd:
        rsrcmgr=PDFResourceManager()
        retstr=StringIO()
        laparams=LAParams()
        device=TextConverter(rsrcmgr,retstr,laparams=laparams)
        process_pdf(rsrcmgr,device,fd)
        device.close()
        content=retstr.getvalue()
        retstr.close()
        strs = str(content).split('\n')
        for val in strs:
            if val == '':
                strs.remove(val)
        strs = "===".join(strs)
        strs = re.sub('===','<p>',strs)
        print(strs)
        return strs


# pdffile='d:/33.pdf'
# readPDF(pdffile)