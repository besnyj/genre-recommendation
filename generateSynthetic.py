import random
import csv

# List of music genres organized by type
music_genres_by_type = {
    "Rock": ["Rock", "Metal", "Punk", "Grunge", "Alternative"],
    "Pop": ["Pop", "K-pop", "Indie Pop", "Synthpop", "Pop Rock"],
    "Hip Hop": ["Hip Hop", "Rap", "Trap", "R&B", "Trap Soul"],
    "Electronic": ["Electronic", "EDM", "Techno", "House", "Trance"],
    "Country": ["Country", "Folk", "Bluegrass"],
    "Jazz": ["Jazz", "Blues", "Fusion"],
    "Classical": ["Classical", "Orchestral", "Chamber Music"],
    "Reggae": ["Reggae", "Ska", "Dancehall"],
    "Latin": ["Latin", "Salsa", "Bachata", "Reggaeton"],
    "World": ["World", "Ethnic"],
    # Add more genre types and related genres here
}

# Defining more specific relationships between genre types
specific_relationships = [
    ("Rock", "Metal", "Punk"),
    ("Pop", "K-pop", "Indie Pop"),
    ("Hip Hop", "Rap", "Trap"),
    ("Electronic", "EDM", "Techno"),
    ("Country", "Folk", "Bluegrass"),
    ("Jazz", "Blues", "Fusion"),
    ("Classical", "Orchestral", "Chamber Music"),
    ("Reggae", "Ska", "Dancehall"),
    ("Latin", "Salsa", "Bachata", "Reggaeton"),
    # Define more specific relationships here
]

# Flatten the genres for easy random selection
all_music_genres = [genre for genres in music_genres_by_type.values() for genre in genres]

# Generate synthetic data
data = []
for _ in range(20000):  # Generating 2000 rows in total
    age = random.randint(15, 60)
    gender = random.choice(["Male", "Female"])

    if len(data) < 10000:
        # For the first 1000 rows, select specific related genres
        genre_type = random.choice(list(music_genres_by_type.keys()))
        related_genres = music_genres_by_type[genre_type]
        selected_genres = random.sample(related_genres, min(3, len(related_genres)))
    else:
        # For the next 1000 rows, select specific related genres or mix related genres
        relationship = random.choice(specific_relationships)
        selected_genres = random.sample(relationship, min(3, len(relationship)))

    # Suggest a genre based on the selected genres
    suggested_genre = random.choice(selected_genres)

    data.append([age, gender] + selected_genres + [suggested_genre])

# Write data to CSV file
csv_file = "synthetic_music_data.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["age", "gender", "genre1", "genre2", "genre3", "suggested_genre"])
    writer.writerows(data)

print(f"Synthetic data has been generated and saved to {csv_file}.")
