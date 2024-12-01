# coding: utf8

from fastapi import FastAPI
from pydantic import BaseModel

# Create the FastAPI instance
app = FastAPI()



# Abjad values for Sindhi/Arabic characters
abjad_dict = {
    'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9,
    'ي': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80,
    'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600,
    'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000
}

# Allah's 99 names and their Abjad values
Allah_Names = {
    'الرَّحْمَن': 329, 'الرَّحِيم': 258, 'الْمَلِك': 90, 'الْقُدُّوس': 170,
    'السَّلَام': 131, 'الْمُؤْمِن': 136, 'الْمُهَيْمِن': 150, 'الْعَزِيز': 94,
    'الْجَبَّار': 206, 'الْمُتَكَبِّر': 662, 'الْخَالِق': 731, 'الْبَارِئ': 213,
    'الْمُصَوِّر': 336, 'الْغَفَّار': 1281, 'الْقَهَّار': 306, 'الْوَهَّاب': 14,
    'الرَّزَّاق': 308, 'الْفَتَّاح': 489, 'اﻟْعَلِيم': 150, 'الْقَابِض': 903,
    'الْبَاسِط': 72, 'الْخَافِض': 1481, 'الرَّافِع': 351, 'الْمُعِز': 117,
    'المُذِل': 770, 'السَّمِيع': 180, 'الْبَصِير': 302, 'الْحَكَم': 68,
    'الْعَدْل': 104, 'اللَّطِيف': 129, 'الْخَبِير': 812, 'الْحَلِيم': 150,
    'الْعَظِيم': 1020, 'الْغَفُور': 1286, 'الشَّكُور': 526, 'الْعَلِيّ': 110,
    'الْكَبِير': 232, 'الْحَفِيظ': 998, 'المُقيِت': 550, 'الْحسِيب': 80,
    'الْجَلِيل': 73, 'الْكَرِيم': 270, 'الرَّقِيب': 312, 'الْمُجِيب': 55,
    'الْوَاسِع': 137, 'الْحَكِيم': 78, 'الْوَدُود': 20, 'الْمَجِيد': 48,
    'الْبَاعِث': 573, 'الشَّهِيد': 319, 'الْحَق': 108, 'الْوَكِيل': 66,
    'الْقَوِيّ': 116, 'الْمَتِين': 500, 'الْوَلِي': 46, 'الْحَمِيد': 62,
    'الْمُحْصِي': 148, 'الْمُبْدِئ': 68, 'المُعيد': 124, 'الْمُحْيِي': 68,
    'اَلْمُمِيت': 490, 'الْحَي': 18, 'الْقَيُّوم': 156, 'الْوَاجِد': 14,
    'الْمَاجِد': 48, 'الْواحِد': 19, 'اَلاَحَد': 13, 'الصَّمَد': 134,
    'الْقَادِر': 305, 'الْمُقْتَدِر': 744, 'الْمُقَدِّم': 184, 'الْمُؤَخِّر': 846,
    'الأوَّل': 37, 'الآخِر': 801, 'الظَّاهِر': 1106, 'البَاطِن': 62,
    'الْوَالِي': 47, 'المتعالِي': 551, 'الْبَرّ': 202, 'التَّوَاب': 409,
    'المُنْتَقِم': 630, 'العَفُو': 156, 'الرؤوف': 318, 'مَالِكُ ٱلْمُلْك': 211,
    'ذُوالْجَلاَلِ وَالإكْرَام': 1201, 'المُقْسِط': 209, 'الْجَامِع': 114,
    'ٱلْغَني': 1060, 'ٱلْمُغْني': 1100, 'اﻟﻤﺎﻧﻊ': 161, 'الضَّار': 1001,
    'النَّافِع': 351, 'النُّور': 256, 'الْهَادِي': 20, 'الْبَدِيع': 116,
    'ٱلْبَاقِي': 113, 'ٱلْوَارِث': 707, 'الرَّشِيد': 514, 'ٱلصَّبُور': 298
}

def calculate_abjad_value(text):
    """Calculate the abjad value of a given text."""
    value = 0
    for char in text:
        value += abjad_dict.get(char, 0)  # Default to 0 if the character is not found
    return value

def find_matching_names(target_sum):
    """Find two names from Allah's 99 names whose sum equals the target sum."""
    names = list(Allah_Names.keys())
    values = list(Allah_Names.values())
    matches = []
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] + values[j] == target_sum:
                matches.append((names[i], names[j]))
    return matches

class InputModel(BaseModel):
    text: str

@app.get("/")
async def health_check():
    """Health check endpoint to confirm API is running."""
    return {"status": "healthy", "message": "hey LXI, API is running successfully!"}

@app.post("/abjad/")
async def get_abjad_details(input_data: InputModel):
    """API to calculate Abjad value and find matching names."""
    abjad_value = calculate_abjad_value(input_data.text)
    matching_names = find_matching_names(abjad_value)
    return {
        "abjad_value": abjad_value,
        "matching_names": matching_names
    }
