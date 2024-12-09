import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, mode='r', encoding='utf-8') as file:
           html = file.read()

           text = re.sub(pattern=r'<[^>]+>', repl='', string=html)

           non_empty_lines = [line.strip() for line in text.splitlines() if line.strip() != '']
           cleaned_text = '\n'.join(non_empty_lines)

           with codecs.open(result_file, mode='w', encoding='utf-8') as file:
               file.write(cleaned_text)


delete_html_tags('draft.html')