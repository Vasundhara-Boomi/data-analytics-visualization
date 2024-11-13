import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample course data
course_data = {
    'CourseID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Title': [
        'Introduction to Python',
        'Machine Learning Fundamentals',
        'Web Development with Django',
        'Data Science with Python',
        'Artificial Intelligence',
        'Java Programming for Beginners',
        'Deep Learning with TensorFlow',
        'Introduction to Natural Language Processing',
        'Front-end Web Development',
        'Database Design and Management',
    ],
    'Description': [
        'Learn the basics of Python programming.',
        'Explore the fundamentals of machine learning.',
        'Build web applications with Django framework.',
        'Master data science using Python.',
        'Dive into the world of AI and its applications.',
        'Learn Java programming from scratch.',
        'Discover deep learning with TensorFlow.',
        'Explore the basics of NLP and its applications.',
        'Create interactive front-end web applications.',
        'Master database design and management concepts.',
    ],
}

# Create a DataFrame from the course data
courses_df = pd.DataFrame(course_data)

def recommend_courses(user_interests):
    # TF-IDF vectorization
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(courses_df['Description'])

    # Compute the cosine similarity between user interests and course descriptions
    cosine_sim = linear_kernel(tfidf_vectorizer.transform([user_interests]), tfidf_matrix)

    # Get course recommendations based on similarity scores
    course_recommendations = list(enumerate(cosine_sim[0]))
    course_recommendations = sorted(course_recommendations, key=lambda x: x[1], reverse=True)

    # Get the top 3 recommended courses
    top_courses = course_recommendations[1:4]

    # Return recommended courses
    recommended_courses = []
    for i, score in top_courses:
        recommended_courses.append(f"{courses_df['Title'][i]} (Similarity Score: {score:.2f})")

    return recommended_courses

# The script can be used as a module to recommend courses based on user interests.
if __name__ == "__main__":
    # In this block, you can add any additional logic or testing you want to perform when running the script directly.
    # For example, you can take user interests as input and call the recommend_courses function to get recommendations.
    user_interests = input("Enter your interests: ")
    recommendations = recommend_courses(user_interests)
    print("Recommended Courses:")
    for course in recommendations:
        print(course)
