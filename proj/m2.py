from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample course data
courses = [
    "Introduction to Python",
    "Machine Learning Fundamentals",
    "Web Development with Django",
    "Data Science with Python",
    "Artificial Intelligence",
    "Java Programming for Beginners",
    "Deep Learning with TensorFlow",
    "Introduction to Natural Language Processing",
    "Front-end Web Development",
    "Database Design and Management",
]

# Take user interest input
user_interest = input("Enter your interests: ")

# Create a TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer()

# Fit and transform the course descriptions
tfidf_matrix = tfidf_vectorizer.fit_transform(courses)

# Transform the user interest input
user_interest_vector = tfidf_vectorizer.transform([user_interest])

# Calculate cosine similarity between user input and course descriptions
cosine_similarities = linear_kernel(user_interest_vector, tfidf_matrix)

# Get course recommendations
recommendations = list(enumerate(cosine_similarities[0]))

# Sort courses by similarity
recommendations.sort(key=lambda x: x[1], reverse=True)

# Display recommended courses
print("Recommended Courses:")
for idx, similarity in recommendations[:5]:  # Display the top 5 recommendations
    print(f"{courses[idx]} (Similarity: {similarity:.2f})")
