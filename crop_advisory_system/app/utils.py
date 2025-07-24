def recommend_fertilizer(data):
    if data['N'] < 20:
        return "Apply Urea (46% N)"
    elif data['P'] < 15:
        return "Apply Single Super Phosphate (16% P2O5)"
    elif data['K'] < 15:
        return "Apply Muriate of Potash (60% K2O)"
    else:
        return "Soil is nutrient-sufficient. No additional fertilizer required."
