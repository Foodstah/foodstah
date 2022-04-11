from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

def start():
    font_config = FontConfiguration()
    html = HTML(filename='/Users/temporaryadmin/DCI_Projects/Foodstah/foodstah/foodstah/post/templates/post/pdf_template.html')
    css = CSS(string='''
        @font-face {
            font-family: Gentium;
            src: url(http://example.com/fonts/Gentium.otf);
        }
        h1 { font-family: Gentium }''', 
        font_config=font_config)
    html.write_pdf(
        '/Users/temporaryadmin/Desktop/example.pdf', stylesheets=[css],
        font_config=font_config)


if __name__ == '__main__':
    start()
