from pypdf import PdfReader


def extract_text(pdf_path):

    text = ""

    reader = PdfReader(pdf_path)

    for page in reader.pages:
        text += page.extract_text()

    return text



def extract_skills(text):

    skills = [
        "Python",
        "Java",
        "SQL",
        "Machine Learning",
        "Flask",
        "HTML",
        "CSS",
        "JavaScript",
        "React",
        "Data Science"
    ]


    found_skills = []


    for skill in skills:

        if skill.lower() in text.lower():
            found_skills.append(skill)


    return found_skills