import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def detect_category(product_name):

    product_name = product_name.lower()

    if "refrigerator" in product_name or "fridge" in product_name:
        return "Fridge"

    if "tv" in product_name or "television" in product_name:
        return "TV"

    if "laptop" in product_name:
        return "Laptop"

    if "kurti" in product_name:
        return "Women Clothing"

    if "shirt" in product_name or "jeans" in product_name:
        return "Men Clothing"

    if "watch" in product_name:
        return "Watch"

    if "headphone" in product_name or "earphone" in product_name:
        return "Headphones"

    if (
        "iphone" in product_name
        or "redmi" in product_name
        or "oneplus" in product_name
        or "realme" in product_name
        or "samsung galaxy" in product_name
        or "mobile" in product_name
        or "phone" in product_name
        or "smartphone" in product_name
    ):
        return "Mobile"

    if (
        "nike" in product_name
        or "adidas" in product_name
        or "puma" in product_name
        or "shoe" in product_name
        or "shoes" in product_name
    ):
        return "Shoes"

    if (
        "bag" in product_name
        or "backpack" in product_name
        or "skybags" in product_name
        or "wildcraft" in product_name
        or "safari" in product_name
    ):
        return "Bags"

    return None


def get_recommendations(product_name, user_history=[]):

    df = pd.read_csv("dataset/products.csv")

    if "Tags" not in df.columns:
        df["Tags"] = ""

    df["Tags"] = df["Tags"].fillna("")
    df["Product_Name"] = df["Product_Name"].fillna("")
    df["Category"] = df["Category"].fillna("")
    df["Brand"] = df["Brand"].fillna("")
    df["Description"] = df["Description"].fillna("")

    df["combined"] = (
        df["Product_Name"].astype(str)
        + " "
        + df["Category"].astype(str)
        + " "
        + df["Brand"].astype(str)
        + " "
        + df["Tags"].astype(str)
        + " "
        + df["Description"].astype(str)
    )

    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(df["combined"])
    search_vector = tfidf.transform([product_name])

    similarity_scores = cosine_similarity(search_vector, tfidf_matrix)
    df["Similarity"] = similarity_scores[0]

    category = detect_category(product_name)
    print("Detected Category =", category)
    search_lower = product_name.lower()

    detected_brand = ""

    brands = [
        "apple", "samsung", "xiaomi", "oneplus", "realme",
        "nothing", "vivo", "oppo", "motorola", "iqoo",
        "poco", "google", "dell", "hp", "lenovo",
        "asus", "acer", "msi", "sony", "lg",
        "whirlpool", "godrej", "haier", "bosch",
        "titan", "fastrack", "casio", "fossil",
        "boat", "jbl", "noise", "sennheiser"
    ]

    for brand in brands:
        if brand in search_lower:
            detected_brand = brand
            break

    scores = []

    for _, row in df.iterrows():

        score = 0

        if category and row["Category"] == category:
            score += 50

        if detected_brand and detected_brand.lower() == str(row["Brand"]).lower():
            score += 30

        score += float(row["Rating"]) * 5
        score += float(row["Similarity"]) * 40

        scores.append(score)

    df["FinalScore"] = scores

    if category:
        recommendations = df[df["Category"] == category].copy()
        print(recommendations[["Product_Name","Category"]])
    else:
        recommendations = df.copy()

    recommendations = recommendations.sort_values(by="FinalScore", ascending=False)
    recommendations = recommendations.drop_duplicates(subset=["Product_Name"])
    recommendations = recommendations.reset_index(drop=True)

    # Ensure we have enough data
    if len(recommendations) == 0:
        return ([], [], [])

    # BEST MATCH
    best_match = recommendations.head(1)

    # REMOVE BEST
    rest = recommendations.iloc[1:].reset_index(drop=True)

    # BETTER OPTIONS
    better_options = rest.head(3)

    # OTHER OPTIONS (JUST NEXT ITEMS, NO DELETION LOGIC)
    other_options = rest.iloc[3:7]

    #  FINAL SAFETY FALLBACK
    if len(other_options) == 0:
        other_options = recommendations.sample(
            min(4, len(recommendations))
        )

    return (
        best_match.to_dict("records"),
        better_options.to_dict("records"),
        other_options.to_dict("records")
    )