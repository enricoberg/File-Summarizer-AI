import google.generativeai as genai
from dotenv import load_dotenv
import os
from sumutils import extract_and_format_text,parse_text_file,concatenate_strings,summarize_all,txt_to_docx


extract_and_format_text("example.docx") #SELECT THE NAME OF THE ORIGINAL FILE TO SUMMARIZEGOOGLE_API_KEY=


load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")
results=parse_text_file()
chunks=concatenate_strings(results,3000)
summarize_all(chunks,model)
txt_to_docx("output.docx") #SELECT THE NAME OF THE SUMMARY FILE