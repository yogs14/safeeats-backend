from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"messsage": "SafeEats Backend is running!"}

class ProductRequest(BaseModel):
    ingredients_text: str

@app.post("/analyze")
def analyze_product(request: ProductRequest):
    text_to_analyze = request.ingredients_text
    
    analysis_result = run_analysis(text_to_analyze)
    
    return {"received_text": text_to_analyze, "status": "analysis pending"}

def run_analysis(text: str) -> str:
    lower_text = text.lower()
    
    found_allergens = []
    
    allergen_db = {
        "Susu": ["susu", "laktosa", "kasein", "whey"],
        "Telur": ["telur", "ovomucoid", "ovalbumin"],
        "Kacang Tanah": ["kacang tanah", "peanut"],
        "Kacang Kedelai": ["kacang kedelai", "soy"],
        "Gandum": ["gandum", "gluten"],
        "Kerang": ["kerang", "mollusca"],
        "Ikan": ["ikan", "fish"],
        "Serealia": ["serealia", "cereal"],
        "Biji-bijian": ["biji-bijian", "seeds"]
    }
    
    for allergen, keywords in allergen_db.items():
        if any(keyword in lower_text for keyword in keywords):
            found_allergens.append(allergen)
            
    nutri_score = "C"
    if "gula" in lower_text or "sirup" in lower_text:
        nutri_score = "D"
        
    return {
        "allergens": found_allergens,
        "nutri_score": nutri_score,
        "nova_score": 2,
        "eco_score": "B"
    }