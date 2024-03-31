from PyPDF2 import PdfReader
import re

def extract_text_from_pdf(pdf_file: str) -> list[str]:

    with open(pdf_file, 'rb') as pdf:
        reader = PdfReader(pdf, strict = False)
        pdf_text = []

        for page in reader.pages:
            content = page.extract_text()

            cleaned_content = re.sub(r'[^\w\s.,:;%]', '', content)

            text_lines = re.split(r'(?<=[.,:;])\s+|\s{2,}', cleaned_content)
            
            cleaned_text = [re.sub(r'[.,:;]', '', line.strip()) for line in text_lines if line.strip()]

            pdf_text.extend(cleaned_text)

        return pdf_text
    
def count_repetitions(pdf_text: list[str], dict_phrases: list[str]) -> dict[str, int]:
    repeated_phrase: dict[str, int] = {phrase: 0 for phrase in dict_phrases}
    
    for phrase in repeated_phrase:
        for text in pdf_text:
            repeated_phrase[phrase] += text.lower().count(phrase.lower())

    return repeated_phrase

def main() -> None:
    pdf_text: list[str] = extract_text_from_pdf('Sample.pdf')
    dict_phrases: list[str] = extract_text_from_pdf('Sample.pdf')

    phrases_repetitions: dict[str, int] = count_repetitions(pdf_text, dict_phrases)

    for phrase, repetiton in phrases_repetitions.items():
        print(f'"{phrase}" aparece {repetiton}')
    
if __name__ == '__main__':
    main()