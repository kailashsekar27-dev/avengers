from parser import extract_text, extract_skills


pdf_path = "uploads/KAILASH2.pdf"


text = extract_text(pdf_path)


print("Resume Content:")
print(text)


skills = extract_skills(text)


print("Skills Found:")
print(skills)